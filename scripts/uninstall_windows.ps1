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
