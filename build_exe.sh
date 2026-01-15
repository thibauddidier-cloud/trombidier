#!/bin/bash

echo "========================================"
echo "Generateur de Trombinoscope"
echo "Conversion en executable"
echo "========================================"
echo ""

# Verification de PyInstaller
echo "[1/4] Verification de PyInstaller..."
if ! pip show pyinstaller > /dev/null 2>&1; then
    echo "PyInstaller n'est pas installe. Installation en cours..."
    pip install pyinstaller
fi

echo ""
echo "[2/4] Creation du dossier de sortie..."
mkdir -p dist
mkdir -p build

echo ""
echo "[3/4] Compilation de l'application..."
echo "Cela peut prendre quelques minutes..."
echo ""

pyinstaller --onefile \
    --windowed \
    --name="Trombinoscope_Generator" \
    --add-data="assets:assets" \
    --add-data="sample_data:sample_data" \
    trombinoscope_app.py

echo ""
echo "[4/4] Nettoyage..."
rm -f Trombinoscope_Generator.spec

echo ""
echo "========================================"
echo "Conversion terminee !"
echo ""
echo "Votre executable se trouve dans :"
echo "$(pwd)/dist/Trombinoscope_Generator"
echo "========================================"
echo ""
