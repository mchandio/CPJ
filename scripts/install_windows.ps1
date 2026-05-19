[CmdletBinding()]
param(
    [string]$InstallDir = (Join-Path $env:LOCALAPPDATA "CPJ"),
    [string]$PackageDir = "dist\cpj-windows",
    [switch]$NoPath,
    [switch]$SkipPythonPackages
)

$ErrorActionPreference = "Stop"
$RepoRoot = (Resolve-Path -LiteralPath (Join-Path $PSScriptRoot "..")).Path
Set-Location -LiteralPath $RepoRoot

function Resolve-SourcePackage {
    param([Parameter(Mandatory = $true)][string]$Path)
    if ([System.IO.Path]::IsPathRooted($Path)) {
        return [System.IO.Path]::GetFullPath($Path)
    }
    return [System.IO.Path]::GetFullPath((Join-Path $RepoRoot $Path))
}

$sourcePackage = Resolve-SourcePackage $PackageDir
if (-not (Test-Path -LiteralPath (Join-Path $sourcePackage "bin\cpj.exe"))) {
    Write-Host "[CPJ] Package not found; building it first..."
    & (Join-Path $PSScriptRoot "build_windows.ps1") -PackageDir $PackageDir -SkipPythonPackages:$SkipPythonPackages
}

if (-not (Test-Path -LiteralPath (Join-Path $sourcePackage "bin\cpj.exe"))) {
    throw "CPJ Windows package is missing: $sourcePackage"
}

$resolvedInstallDir = [System.IO.Path]::GetFullPath($InstallDir)
New-Item -ItemType Directory -Force -Path $resolvedInstallDir | Out-Null
Copy-Item -Path (Join-Path $sourcePackage "*") -Destination $resolvedInstallDir -Recurse -Force

if (-not $SkipPythonPackages) {
    $python = Get-Command python.exe -ErrorAction SilentlyContinue
    if (-not $python) {
        throw "Python is required. Install Python for Windows, then rerun this script."
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
    $userPath = [Environment]::GetEnvironmentVariable("Path", "User")
    $parts = @()
    if ($userPath) {
        $parts = $userPath -split ";" | Where-Object { $_ }
    }
    $alreadyPresent = $parts | Where-Object { $_.TrimEnd("\") -ieq $binDir.TrimEnd("\") }
    if (-not $alreadyPresent) {
        $newPath = ($parts + $binDir) -join ";"
        [Environment]::SetEnvironmentVariable("Path", $newPath, "User")
        Write-Host "[CPJ] Added CPJ to your user PATH. Open a new terminal to use 'cpj' globally."
    }
}

Write-Host "[CPJ] Installed native Windows CPJ:"
Write-Host "  Install: $resolvedInstallDir"
Write-Host "  Command: $binDir\cpj.cmd"
Write-Host "  Try:     cpj --help"
