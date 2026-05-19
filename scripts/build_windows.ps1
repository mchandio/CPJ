[CmdletBinding()]
param(
    [string]$OutDir = "build\windows\bin",
    [string]$PackageDir = "dist\cpj-windows",
    [switch]$SkipPythonPackages
)

$ErrorActionPreference = "Stop"
$RepoRoot = (Resolve-Path -LiteralPath (Join-Path $PSScriptRoot "..")).Path
Set-Location -LiteralPath $RepoRoot

function Resolve-InRepo {
    param([Parameter(Mandatory = $true)][string]$Path)
    $fullPath = [System.IO.Path]::GetFullPath((Join-Path $RepoRoot $Path))
    if (-not $fullPath.StartsWith($RepoRoot, [System.StringComparison]::OrdinalIgnoreCase)) {
        throw "Path must stay inside the CPJ repository: $Path"
    }
    return $fullPath
}

function Remove-TreeInRepo {
    param([Parameter(Mandatory = $true)][string]$Path)
    $fullPath = Resolve-InRepo $Path
    if (Test-Path -LiteralPath $fullPath) {
        Remove-Item -LiteralPath $fullPath -Recurse -Force
    }
}

function Ensure-PythonPackages {
    if ($SkipPythonPackages) {
        Write-Host "[CPJ] Skipping Python package installation."
        return
    }
    $python = Get-Command python.exe -ErrorAction SilentlyContinue
    if (-not $python) {
        throw "Python is required. Install Python for Windows, then rerun this script."
    }
    Write-Host "[CPJ] Installing Windows Python requirements..."
    & $python.Source -m pip install --upgrade pip
    & $python.Source -m pip install -r (Join-Path $RepoRoot "requirements.txt")
}

function Ensure-W64Devkit {
    $localGpp = Join-Path $RepoRoot ".tools\w64devkit-extract\w64devkit\bin\g++.exe"
    if (Test-Path -LiteralPath $localGpp) {
        return $localGpp
    }

    $existing = Get-Command g++.exe -ErrorAction SilentlyContinue
    if ($existing) {
        return $existing.Source
    }

    Write-Host "[CPJ] Downloading portable w64devkit toolchain..."
    $cache = Join-Path $RepoRoot ".tools\cache"
    $extractRoot = Join-Path $RepoRoot ".tools\w64devkit-extract"
    New-Item -ItemType Directory -Force -Path $cache, $extractRoot | Out-Null

    $release = Invoke-RestMethod -Uri "https://api.github.com/repos/skeeto/w64devkit/releases/latest" -Headers @{ "User-Agent" = "CPJ-Windows-Build" }
    $asset = $release.assets | Where-Object { $_.name -like "w64devkit-x64-*.7z.exe" } | Select-Object -First 1
    if (-not $asset) {
        throw "Could not find the latest w64devkit x64 release asset."
    }

    $archive = Join-Path $cache $asset.name
    if (-not (Test-Path -LiteralPath $archive)) {
        Invoke-WebRequest -Uri $asset.browser_download_url -OutFile $archive -Headers @{ "User-Agent" = "CPJ-Windows-Build" }
    }

    & $archive -y "-o$extractRoot" | Out-Host
    if (-not (Test-Path -LiteralPath $localGpp)) {
        throw "w64devkit extraction completed, but g++.exe was not found."
    }
    return $localGpp
}

Ensure-PythonPackages
$gpp = Ensure-W64Devkit
$toolBin = Split-Path -Parent $gpp
$env:PATH = "$toolBin;$env:PATH"

$resolvedOutDir = Resolve-InRepo $OutDir
New-Item -ItemType Directory -Force -Path $resolvedOutDir | Out-Null

Write-Host "[CPJ] Building native Windows binary..."
& $gpp -std=c++20 -O2 -static -DWIN32_LEAN_AND_MEAN -o (Join-Path $resolvedOutDir "cpj.exe") (Join-Path $RepoRoot "cpj_compiler.cpp")
if ($LASTEXITCODE -ne 0) {
    Write-Host "[CPJ] Static build failed; retrying dynamic build..."
    & $gpp -std=c++20 -O2 -DWIN32_LEAN_AND_MEAN -o (Join-Path $resolvedOutDir "cpj.exe") (Join-Path $RepoRoot "cpj_compiler.cpp")
}
if ($LASTEXITCODE -ne 0) {
    throw "Native Windows CPJ build failed."
}

Remove-TreeInRepo $PackageDir
$resolvedPackageDir = Resolve-InRepo $PackageDir
New-Item -ItemType Directory -Force -Path (Join-Path $resolvedPackageDir "bin") | Out-Null

Copy-Item -LiteralPath (Join-Path $resolvedOutDir "cpj.exe") -Destination (Join-Path $resolvedPackageDir "bin\cpj.exe") -Force
Set-Content -LiteralPath (Join-Path $resolvedPackageDir "bin\cpj.cmd") -Encoding ASCII -Value @(
    "@echo off",
    "setlocal",
    '"%~dp0cpj.exe" %*',
    "exit /b %ERRORLEVEL%"
)

foreach ($dir in @("tools", "python", "stdlib", "samples", "docs", "grammar", "include", "java")) {
    $source = Join-Path $RepoRoot $dir
    if (Test-Path -LiteralPath $source) {
        Copy-Item -LiteralPath $source -Destination (Join-Path $resolvedPackageDir $dir) -Recurse -Force
    }
}

foreach ($file in @("README.md", "requirements.txt", "LANGUAGE_SPEC.md", "CPJ_Guide.md", "CMakeLists.txt")) {
    $source = Join-Path $RepoRoot $file
    if (Test-Path -LiteralPath $source) {
        Copy-Item -LiteralPath $source -Destination (Join-Path $resolvedPackageDir $file) -Force
    }
}

Set-Content -LiteralPath (Join-Path $resolvedPackageDir "install.ps1") -Encoding ASCII -Value @'
[CmdletBinding()]
param(
    [string]$InstallDir = (Join-Path $env:LOCALAPPDATA "CPJ"),
    [switch]$NoPath,
    [switch]$SkipPythonPackages
)

$ErrorActionPreference = "Stop"
$PackageRoot = $PSScriptRoot
$resolvedInstallDir = [System.IO.Path]::GetFullPath($InstallDir)
$resolvedPackageRoot = [System.IO.Path]::GetFullPath($PackageRoot)
if ($resolvedInstallDir.TrimEnd("\") -ieq $resolvedPackageRoot.TrimEnd("\")) {
    throw "The install directory cannot be the package source directory."
}

New-Item -ItemType Directory -Force -Path $resolvedInstallDir | Out-Null
Get-ChildItem -LiteralPath $PackageRoot -Force | ForEach-Object {
    Copy-Item -LiteralPath $_.FullName -Destination $resolvedInstallDir -Recurse -Force
}

if (-not $SkipPythonPackages) {
    $python = Get-Command python.exe -ErrorAction SilentlyContinue
    if (-not $python) {
        throw "Python is required. Install Python for Windows, then rerun this script."
    }
    $requirements = Join-Path $resolvedInstallDir "requirements.txt"
    if (Test-Path -LiteralPath $requirements) {
        & $python.Source -m pip install --upgrade pip
        & $python.Source -m pip install -r $requirements
    }
}

$binDir = Join-Path $resolvedInstallDir "bin"
if (-not $NoPath) {
    $userPath = [Environment]::GetEnvironmentVariable("Path", "User")
    $parts = @()
    if ($userPath) {
        $parts = $userPath -split ";" | Where-Object { $_ }
    }
    $alreadyPresent = $parts | Where-Object { $_.TrimEnd("\") -ieq $binDir.TrimEnd("\") }
    if (-not $alreadyPresent) {
        [Environment]::SetEnvironmentVariable("Path", (($parts + $binDir) -join ";"), "User")
    }
}

Write-Host "[CPJ] Installed native Windows CPJ to $resolvedInstallDir"
Write-Host "[CPJ] Open a new terminal, then run: cpj --help"
'@

Set-Content -LiteralPath (Join-Path $resolvedPackageDir "uninstall.ps1") -Encoding ASCII -Value @'
[CmdletBinding()]
param(
    [string]$InstallDir = (Join-Path $env:LOCALAPPDATA "CPJ"),
    [switch]$KeepPath
)

$ErrorActionPreference = "Stop"
$resolvedInstallDir = [System.IO.Path]::GetFullPath($InstallDir)
$root = [System.IO.Path]::GetPathRoot($resolvedInstallDir)
if ($resolvedInstallDir -eq $root -or $resolvedInstallDir.Length -lt 6) {
    throw "Refusing to remove unsafe install directory: $resolvedInstallDir"
}

$binDir = Join-Path $resolvedInstallDir "bin"
if (-not $KeepPath) {
    $userPath = [Environment]::GetEnvironmentVariable("Path", "User")
    if ($userPath) {
        $parts = $userPath -split ";" | Where-Object {
            $_ -and ($_.TrimEnd("\") -ine $binDir.TrimEnd("\"))
        }
        [Environment]::SetEnvironmentVariable("Path", ($parts -join ";"), "User")
    }
}

if (Test-Path -LiteralPath $resolvedInstallDir) {
    Remove-Item -LiteralPath $resolvedInstallDir -Recurse -Force
}

Write-Host "[CPJ] Uninstalled CPJ from $resolvedInstallDir"
'@

$zipPath = Join-Path (Split-Path -Parent $resolvedPackageDir) "cpj-windows.zip"
if (Test-Path -LiteralPath $zipPath) {
    Remove-Item -LiteralPath $zipPath -Force
}
Compress-Archive -Path (Join-Path $resolvedPackageDir "*") -DestinationPath $zipPath -Force

Write-Host "[CPJ] Windows package ready:"
Write-Host "  Binary:  $(Join-Path $resolvedOutDir "cpj.exe")"
Write-Host "  Package: $resolvedPackageDir"
Write-Host "  Zip:     $zipPath"
