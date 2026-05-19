# Native Windows Install

CPJ can be built as a native Windows executable (`cpj.exe`) and installed with
PowerShell scripts from the repository root.

## Build

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\build_windows.ps1
```

The build script:

- installs Python packages from `requirements.txt`
- provisions a portable w64devkit C++ toolchain when no `g++.exe` is available
- compiles `cpj_compiler.cpp` into `build\windows\bin\cpj.exe`
- stages an installable CPJ layout in `dist\cpj-windows`
- creates `dist\cpj-windows.zip`

To create a single-file Windows setup script that embeds the package:

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\create_windows_installer.ps1
```

This writes:

```text
dist\CPJ-Setup-Windows.ps1
dist\CPJ-Setup-Windows.cmd
```

To skip Python package installation:

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\build_windows.ps1 -SkipPythonPackages
```

## Install

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\install_windows.ps1
```

By default CPJ installs to:

```text
%LOCALAPPDATA%\CPJ
```

The installer copies the native binary, CPJ runtime tools, standard library,
samples, and docs. It also adds `%LOCALAPPDATA%\CPJ\bin` to the user PATH.
Open a new terminal after installation, then run:

```powershell
cpj --help
cpj --web-only -o generated samples\web_app.cpj
```

For a local test install without modifying PATH:

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\install_windows.ps1 -InstallDir .\build\cpj-install-test -NoPath
.\build\cpj-install-test\bin\cpj.cmd --help
```

The standalone installer can be run directly:

```powershell
powershell -ExecutionPolicy Bypass -File .\dist\CPJ-Setup-Windows.ps1
```

## Uninstall

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\uninstall_windows.ps1
```

Use `-InstallDir` if CPJ was installed to a custom directory.
