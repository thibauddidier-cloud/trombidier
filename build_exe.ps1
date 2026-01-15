# Script PowerShell pour compiler le Trombinoscope
# Encodage UTF-8 avec BOM
[Console]::OutputEncoding = [System.Text.Encoding]::UTF8

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "Générateur de Trombinoscope" -ForegroundColor Cyan
Write-Host "Conversion en exécutable (.exe)" -ForegroundColor Cyan
Write-Host "Version PowerShell" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# ===================================================
# Étape 1 : Recherche de Python
# ===================================================
Write-Host "[1/5] Recherche de Python..." -ForegroundColor Yellow

$pythonCmd = $null
$pythonFound = $false

# Tester python dans le PATH
try {
    $version = & python --version 2>&1
    if ($LASTEXITCODE -eq 0) {
        $pythonCmd = "python"
        $pythonFound = $true
        Write-Host "✓ Python trouvé dans le PATH : $version" -ForegroundColor Green
    }
} catch {}

# Tester py launcher si python n'est pas trouvé
if (-not $pythonFound) {
    try {
        $version = & py --version 2>&1
        if ($LASTEXITCODE -eq 0) {
            $pythonCmd = "py"
            $pythonFound = $true
            Write-Host "✓ Python trouvé via py launcher : $version" -ForegroundColor Green
        }
    } catch {}
}

# Tester chemins courants
if (-not $pythonFound) {
    $pythonPaths = @(
        "C:\Python311\python.exe",
        "C:\Python310\python.exe",
        "C:\Python39\python.exe",
        "$env:LOCALAPPDATA\Programs\Python\Python311\python.exe",
        "$env:LOCALAPPDATA\Programs\Python\Python310\python.exe"
    )
    
    foreach ($path in $pythonPaths) {
        if (Test-Path $path) {
            try {
                $version = & $path --version 2>&1
                if ($LASTEXITCODE -eq 0) {
                    $pythonCmd = $path
                    $pythonFound = $true
                    Write-Host "✓ Python trouvé : $path" -ForegroundColor Green
                    Write-Host "  Version : $version" -ForegroundColor Gray
                    break
                }
            } catch {}
        }
    }
}

if (-not $pythonFound) {
    Write-Host ""
    Write-Host "❌ ERREUR : Python n'est pas installé ou introuvable." -ForegroundColor Red
    Write-Host ""
    Write-Host "Solutions :" -ForegroundColor Yellow
    Write-Host "1. Téléchargez Python sur : https://www.python.org/downloads/" -ForegroundColor White
    Write-Host "2. Lors de l'installation, cochez 'Add Python to PATH'" -ForegroundColor White
    Write-Host "3. Relancez ce script après installation" -ForegroundColor White
    Write-Host ""
    Write-Host "Ou consultez : GUIDE_RESOLUTION_PROBLEMES.md" -ForegroundColor Cyan
    Write-Host ""
    Read-Host "Appuyez sur Entrée pour quitter"
    exit 1
}

Write-Host ""

# ===================================================
# Étape 2 : Vérification de PyInstaller
# ===================================================
Write-Host "[2/5] Vérification de PyInstaller..." -ForegroundColor Yellow

$pyinstallerInstalled = $false
try {
    & $pythonCmd -c "import PyInstaller" 2>&1 | Out-Null
    if ($LASTEXITCODE -eq 0) {
        $pyinstallerInstalled = $true
    }
} catch {}

if (-not $pyinstallerInstalled) {
    Write-Host "PyInstaller n'est pas installé. Installation en cours..." -ForegroundColor Yellow
    Write-Host "Cela peut prendre 1-2 minutes..." -ForegroundColor Gray
    
    & $pythonCmd -m pip install pyinstaller
    
    if ($LASTEXITCODE -ne 0) {
        Write-Host ""
        Write-Host "❌ ERREUR : Impossible d'installer PyInstaller" -ForegroundColor Red
        Write-Host ""
        Write-Host "Essayez manuellement :" -ForegroundColor Yellow
        Write-Host "$pythonCmd -m pip install --upgrade pip" -ForegroundColor White
        Write-Host "$pythonCmd -m pip install pyinstaller" -ForegroundColor White
        Write-Host ""
        Read-Host "Appuyez sur Entrée pour quitter"
        exit 1
    }
    Write-Host "✓ PyInstaller installé avec succès" -ForegroundColor Green
} else {
    Write-Host "✓ PyInstaller est déjà installé" -ForegroundColor Green
}
Write-Host ""

# ===================================================
# Étape 3 : Vérification des dépendances
# ===================================================
Write-Host "[3/5] Vérification des dépendances..." -ForegroundColor Yellow

& $pythonCmd -m pip install -q Pillow python-docx 2>&1 | Out-Null
if ($LASTEXITCODE -ne 0) {
    Write-Host "⚠ Avertissement : Erreur lors de l'installation des dépendances" -ForegroundColor Yellow
} else {
    Write-Host "✓ Dépendances installées" -ForegroundColor Green
}
Write-Host ""

# ===================================================
# Étape 4 : Création du dossier de sortie
# ===================================================
Write-Host "[4/5] Création du dossier de sortie..." -ForegroundColor Yellow

if (Test-Path "dist") {
    Write-Host "Nettoyage de l'ancien dossier dist..." -ForegroundColor Gray
    Remove-Item -Recurse -Force "dist"
}
if (Test-Path "build") {
    Remove-Item -Recurse -Force "build"
}

New-Item -ItemType Directory -Force -Path "dist" | Out-Null
Write-Host "✓ Dossier de sortie créé" -ForegroundColor Green
Write-Host ""

# ===================================================
# Étape 5 : Compilation de l'application
# ===================================================
Write-Host "[5/5] Compilation de l'application..." -ForegroundColor Yellow
Write-Host "Cela peut prendre 2-5 minutes..." -ForegroundColor Gray
Write-Host "Veuillez patienter..." -ForegroundColor Gray
Write-Host ""

& $pythonCmd -m PyInstaller trombinoscope.spec

if ($LASTEXITCODE -ne 0) {
    Write-Host ""
    Write-Host "❌ ERREUR lors de la compilation" -ForegroundColor Red
    Write-Host ""
    Write-Host "Vérifiez les erreurs ci-dessus et consultez :" -ForegroundColor Yellow
    Write-Host "GUIDE_RESOLUTION_PROBLEMES.md" -ForegroundColor Cyan
    Write-Host ""
    Read-Host "Appuyez sur Entrée pour quitter"
    exit 1
}

Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "✅ Compilation réussie !" -ForegroundColor Green
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Vérifier que le fichier .exe existe
$exePath = Join-Path $PSScriptRoot "dist\Trombinoscope_Generator.exe"
if (Test-Path $exePath) {
    Write-Host "Votre exécutable se trouve dans :" -ForegroundColor Green
    Write-Host $exePath -ForegroundColor White
    Write-Host ""
    Write-Host "Caractéristiques de votre .exe :" -ForegroundColor Cyan
    Write-Host "• Icône Psyduck 🦆" -ForegroundColor White
    Write-Host "• 10 élèves par ligne" -ForegroundColor White
    Write-Host "• Page de couverture avec année dynamique" -ForegroundColor White
    Write-Host "• Fonctionne sans Python installé" -ForegroundColor White
    Write-Host ""
    Write-Host "Vous pouvez maintenant distribuer ce fichier .exe" -ForegroundColor Green
    Write-Host ""
    
    # Proposer d'ouvrir le dossier
    $openFolder = Read-Host "Voulez-vous ouvrir le dossier dist ? (O/N)"
    if ($openFolder -eq "O" -or $openFolder -eq "o") {
        explorer (Join-Path $PSScriptRoot "dist")
    }
} else {
    Write-Host "⚠ Le fichier .exe n'a pas été trouvé dans dist\" -ForegroundColor Yellow
    Write-Host "Vérifiez les erreurs ci-dessus" -ForegroundColor Yellow
}

Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan
Read-Host "Appuyez sur Entrée pour quitter"
