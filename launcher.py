#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Lanceur simplifié pour l'application Trombinoscope
Installe automatiquement les dépendances si nécessaire
"""

import sys
import subprocess
import os

def check_and_install_dependencies():
    """Vérifie et installe les dépendances nécessaires"""
    
    required_packages = {
        'PIL': 'Pillow',
        'docx': 'python-docx',
    }
    
    missing_packages = []
    
    print("🔍 Vérification des dépendances...")
    
    for module, package in required_packages.items():
        try:
            __import__(module)
            print(f"   ✓ {package}")
        except ImportError:
            print(f"   ✗ {package} (manquant)")
            missing_packages.append(package)
    
    if missing_packages:
        print(f"\n📦 Installation de {len(missing_packages)} package(s) manquant(s)...")
        for package in missing_packages:
            print(f"   Installation de {package}...")
            try:
                subprocess.check_call([sys.executable, "-m", "pip", "install", package, "-q"])
                print(f"   ✓ {package} installé")
            except subprocess.CalledProcessError:
                print(f"   ✗ Erreur lors de l'installation de {package}")
                print(f"\n❌ Installation échouée. Essayez manuellement :")
                print(f"   pip install {package}")
                return False
    
    print("\n✅ Toutes les dépendances sont installées !\n")
    return True


def launch_app():
    """Lance l'application Trombinoscope"""
    
    print("="*60)
    print("🎓 LANCEUR D'APPLICATION TROMBINOSCOPE")
    print("="*60)
    print()
    
    # Vérification de Python
    if sys.version_info < (3, 8):
        print("❌ Python 3.8 ou supérieur est requis.")
        print(f"   Version actuelle : Python {sys.version_info.major}.{sys.version_info.minor}")
        print("\n   Téléchargez Python sur : https://www.python.org/downloads/")
        input("\nAppuyez sur Entrée pour quitter...")
        sys.exit(1)
    
    print(f"✓ Python {sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}")
    print()
    
    # Installation des dépendances
    if not check_and_install_dependencies():
        input("\nAppuyez sur Entrée pour quitter...")
        sys.exit(1)
    
    # Vérification de l'interface graphique
    try:
        import tkinter
        print("✓ Interface graphique disponible")
    except ImportError:
        print("❌ Tkinter n'est pas disponible.")
        print("   Sur Linux, installez : sudo apt-get install python3-tk")
        print("   Sur Mac, réinstallez Python depuis python.org")
        input("\nAppuyez sur Entrée pour quitter...")
        sys.exit(1)
    
    print()
    print("🚀 Lancement de l'application...")
    print("="*60)
    print()
    
    # Import et lancement
    try:
        from trombinoscope_app import main
        main()
    except FileNotFoundError:
        print("❌ Fichier trombinoscope_app.py introuvable.")
        print("   Assurez-vous d'être dans le bon dossier.")
        input("\nAppuyez sur Entrée pour quitter...")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Erreur lors du lancement : {e}")
        import traceback
        traceback.print_exc()
        input("\nAppuyez sur Entrée pour quitter...")
        sys.exit(1)


if __name__ == "__main__":
    try:
        launch_app()
    except KeyboardInterrupt:
        print("\n\n👋 Application fermée par l'utilisateur.")
        sys.exit(0)
