[CmdletBinding()]
param(
    [string]$PackageDir = "dist\cpj-windows",
    [string]$ZipPath = "dist\cpj-windows.zip",
    [string]$InstallerPath = "dist\CPJ-Setup-Windows.ps1",
    [switch]$SkipBuild
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

if (-not $SkipBuild) {
    & (Join-Path $PSScriptRoot "build_windows.ps1") -PackageDir $PackageDir
}

$resolvedZipPath = Resolve-InRepo $ZipPath
if (-not (Test-Path -LiteralPath $resolvedZipPath)) {
    throw "Package zip does not exist: $resolvedZipPath"
}

$resolvedInstallerPath = Resolve-InRepo $InstallerPath
New-Item -ItemType Directory -Force -Path (Split-Path -Parent $resolvedInstallerPath) | Out-Null

$payload = [Convert]::ToBase64String([System.IO.File]::ReadAllBytes($resolvedZipPath))
$payloadLines = ($payload -replace "(.{76})", "`$1`n").Trim()

$stub = @'
[CmdletBinding()]
param(
    [string]$InstallDir = (Join-Path $env:LOCALAPPDATA "CPJ"),
    [switch]$NoPath,
    [switch]$SkipPythonPackages,
    [switch]$KeepTemp
)

$ErrorActionPreference = "Stop"

function Add-UserPath {
    param([Parameter(Mandatory = $true)][string]$BinDir)
    $userPath = [Environment]::GetEnvironmentVariable("Path", "User")
    $parts = @()
    if ($userPath) {
        $parts = $userPath -split ";" | Where-Object { $_ }
    }
    $alreadyPresent = $parts | Where-Object { $_.TrimEnd("\") -ieq $BinDir.TrimEnd("\") }
    if (-not $alreadyPresent) {
        [Environment]::SetEnvironmentVariable("Path", (($parts + $BinDir) -join ";"), "User")
        Write-Host "[CPJ] Added CPJ to your user PATH. Open a new terminal to use 'cpj' globally."
    }
}

$payload = @"
__CPJ_ZIP_BASE64__
"@

$tempRoot = Join-Path ([System.IO.Path]::GetTempPath()) ("cpj-installer-" + [Guid]::NewGuid().ToString("N"))
$zipFile = Join-Path $tempRoot "cpj-windows.zip"
$extractRoot = Join-Path $tempRoot "package"
New-Item -ItemType Directory -Force -Path $extractRoot | Out-Null

try {
    [System.IO.File]::WriteAllBytes($zipFile, [Convert]::FromBase64String(($payload -replace "\s", "")))
    Expand-Archive -LiteralPath $zipFile -DestinationPath $extractRoot -Force

    $packageRoot = $extractRoot
    if (-not (Test-Path -LiteralPath (Join-Path $packageRoot "bin\cpj.exe"))) {
        $candidate = Get-ChildItem -LiteralPath $extractRoot -Directory | Where-Object {
            Test-Path -LiteralPath (Join-Path $_.FullName "bin\cpj.exe")
        } | Select-Object -First 1
        if ($candidate) {
            $packageRoot = $candidate.FullName
        }
    }
    if (-not (Test-Path -LiteralPath (Join-Path $packageRoot "bin\cpj.exe"))) {
        throw "Installer payload is missing bin\cpj.exe."
    }

    $resolvedInstallDir = [System.IO.Path]::GetFullPath($InstallDir)
    New-Item -ItemType Directory -Force -Path $resolvedInstallDir | Out-Null
    Get-ChildItem -LiteralPath $packageRoot -Force | ForEach-Object {
        Copy-Item -LiteralPath $_.FullName -Destination $resolvedInstallDir -Recurse -Force
    }

    if (-not $SkipPythonPackages) {
        $python = Get-Command python.exe -ErrorAction SilentlyContinue
        if (-not $python) {
            throw "Python is required. Install Python for Windows, then rerun this installer."
        }
        $requirements = Join-Path $resolvedInstallDir "requirements.txt"
        if (Test-Path -LiteralPath $requirements) {
            Write-Host "[CPJ] Installing CPJ Python requirements..."
            & $python.Source -m pip install --upgrade pip
            & $python.Source -m pip install -r $requirements
        }
    }

    $binDir = Join-Path $resolvedInstallDir "bin"
    if (-not $NoPath) {
        Add-UserPath -BinDir $binDir
    }

    Write-Host "[CPJ] Native Windows CPJ installed."
    Write-Host "  Install: $resolvedInstallDir"
    Write-Host "  Command: $binDir\cpj.cmd"
    Write-Host "  Verify:  cpj --help"
}
finally {
    if (-not $KeepTemp -and (Test-Path -LiteralPath $tempRoot)) {
        Remove-Item -LiteralPath $tempRoot -Recurse -Force
    }
}
'@

$installer = $stub.Replace("__CPJ_ZIP_BASE64__", $payloadLines)
Set-Content -LiteralPath $resolvedInstallerPath -Encoding ASCII -Value $installer

$cmdPath = [System.IO.Path]::ChangeExtension($resolvedInstallerPath, ".cmd")
Set-Content -LiteralPath $cmdPath -Encoding ASCII -Value @(
    "@echo off",
    "powershell -NoProfile -ExecutionPolicy Bypass -File ""%~dp0$([System.IO.Path]::GetFileName($resolvedInstallerPath))"" %*"
)

Write-Host "[CPJ] Standalone Windows installer created:"
Write-Host "  $resolvedInstallerPath"
Write-Host "  $cmdPath"
