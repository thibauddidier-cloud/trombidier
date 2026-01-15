@echo off
chcp 65001 >nul
setlocal enabledelayedexpansion

echo ========================================
echo Générateur de Trombinoscope
echo Conversion en exécutable (.exe)
echo Version améliorée - Détection automatique
echo ========================================
echo.

REM ===================================================
REM Étape 1 : Recherche de Python
REM ===================================================
echo [1/5] Recherche de Python...

set PYTHON_CMD=
set PYTHON_FOUND=0

REM Tester python dans le PATH
python --version >nul 2>&1
if !errorlevel! equ 0 (
    set PYTHON_CMD=python
    set PYTHON_FOUND=1
    echo ✓ Python trouvé dans le PATH
    goto :python_found
)

REM Tester py launcher
py --version >nul 2>&1
if !errorlevel! equ 0 (
    set PYTHON_CMD=py
    set PYTHON_FOUND=1
    echo ✓ Python trouvé via py launcher
    goto :python_found
)

REM Tester chemins courants
set "PYTHON_PATHS=C:\Python311\python.exe;C:\Python310\python.exe;C:\Python39\python.exe;%LOCALAPPDATA%\Programs\Python\Python311\python.exe;%LOCALAPPDATA%\Programs\Python\Python310\python.exe"

for %%P in (%PYTHON_PATHS%) do (
    if exist "%%P" (
        "%%P" --version >nul 2>&1
        if !errorlevel! equ 0 (
            set PYTHON_CMD=%%P
            set PYTHON_FOUND=1
            echo ✓ Python trouvé : %%P
            goto :python_found
        )
    )
)

:python_found
if !PYTHON_FOUND! equ 0 (
    echo.
    echo ❌ ERREUR : Python n'est pas installé ou introuvable.
    echo.
    echo Solutions :
    echo 1. Téléchargez Python sur : https://www.python.org/downloads/
    echo 2. Lors de l'installation, cochez "Add Python to PATH"
    echo 3. Relancez ce script après installation
    echo.
    echo Ou consultez : GUIDE_RESOLUTION_PROBLEMES.md
    echo.
    pause
    exit /b 1
)

REM Afficher la version de Python
echo.
!PYTHON_CMD! --version
echo.

REM ===================================================
REM Étape 2 : Vérification de PyInstaller
REM ===================================================
echo [2/5] Vérification de PyInstaller...

!PYTHON_CMD! -c "import PyInstaller" >nul 2>&1
if !errorlevel! neq 0 (
    echo PyInstaller n'est pas installé. Installation en cours...
    echo Cela peut prendre 1-2 minutes...
    !PYTHON_CMD! -m pip install pyinstaller
    if !errorlevel! neq 0 (
        echo.
        echo ❌ ERREUR : Impossible d'installer PyInstaller
        echo.
        echo Essayez manuellement :
        echo !PYTHON_CMD! -m pip install --upgrade pip
        echo !PYTHON_CMD! -m pip install pyinstaller
        echo.
        pause
        exit /b 1
    )
    echo ✓ PyInstaller installé avec succès
) else (
    echo ✓ PyInstaller est déjà installé
)
echo.

REM ===================================================
REM Étape 3 : Vérification des dépendances
REM ===================================================
echo [3/5] Vérification des dépendances...

!PYTHON_CMD! -m pip install -q Pillow python-docx
if !errorlevel! neq 0 (
    echo ⚠ Avertissement : Erreur lors de l'installation des dépendances
) else (
    echo ✓ Dépendances installées
)
echo.

REM ===================================================
REM Étape 4 : Création du dossier de sortie
REM ===================================================
echo [4/5] Création du dossier de sortie...

if exist "dist" (
    echo Nettoyage de l'ancien dossier dist...
    rmdir /s /q dist
)
if exist "build" (
    rmdir /s /q build
)

mkdir dist >nul 2>&1
echo ✓ Dossier de sortie créé
echo.

REM ===================================================
REM Étape 5 : Compilation de l'application
REM ===================================================
echo [5/5] Compilation de l'application...
echo Cela peut prendre 2-5 minutes...
echo Veuillez patienter...
echo.

!PYTHON_CMD! -m PyInstaller trombinoscope.spec

if !errorlevel! neq 0 (
    echo.
    echo ❌ ERREUR lors de la compilation
    echo.
    echo Vérifiez les erreurs ci-dessus et consultez :
    echo GUIDE_RESOLUTION_PROBLEMES.md
    echo.
    pause
    exit /b 1
)

echo.
echo ========================================
echo ✅ Compilation réussie !
echo ========================================
echo.

REM Vérifier que le fichier .exe existe
if exist "dist\Trombinoscope_Generator.exe" (
    echo Votre exécutable se trouve dans :
    echo %CD%\dist\Trombinoscope_Generator.exe
    echo.
    echo Caractéristiques de votre .exe :
    echo • Icône Psyduck 🦆
    echo • 10 élèves par ligne
    echo • Page de couverture avec année dynamique
    echo • Fonctionne sans Python installé
    echo.
    echo Vous pouvez maintenant distribuer ce fichier .exe
    echo.
    
    REM Proposer d'ouvrir le dossier
    set /p OPEN_FOLDER="Voulez-vous ouvrir le dossier dist ? (O/N) : "
    if /i "!OPEN_FOLDER!"=="O" (
        explorer "%CD%\dist"
    )
) else (
    echo ⚠ Le fichier .exe n'a pas été trouvé dans dist\
    echo Vérifiez les erreurs ci-dessus
)

echo.
echo ========================================
pause
