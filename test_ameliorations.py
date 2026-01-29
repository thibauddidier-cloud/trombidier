#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script de test pour vérifier les améliorations de l'application trombinoscope
"""

import ast
import sys

def test_syntax():
    """Tester la syntaxe du fichier principal"""
    print("🔍 Test de la syntaxe du code Python...")
    try:
        with open('trombinoscope_app.py', 'r', encoding='utf-8') as f:
            code = f.read()
        ast.parse(code)
        print("✅ Syntaxe Python valide")
        return True
    except SyntaxError as e:
        print(f"❌ Erreur de syntaxe : {e}")
        return False

def test_functions_exist():
    """Vérifier que les nouvelles fonctions existent"""
    print("\n🔍 Vérification des nouvelles fonctions...")
    
    with open('trombinoscope_app.py', 'r', encoding='utf-8') as f:
        code = f.read()
    
    functions_to_check = [
        'create_tooltip',
        'start_psyduck_bounce',
        'stop_psyduck_bounce',
        'animate_psyduck_bounce',
        'pulse_generate_button'
    ]
    
    all_found = True
    for func in functions_to_check:
        if f"def {func}(" in code:
            print(f"✅ Fonction '{func}' trouvée")
        else:
            print(f"❌ Fonction '{func}' manquante")
            all_found = False
    
    return all_found

def test_button_improvements():
    """Vérifier que les améliorations des boutons sont présentes"""
    print("\n🔍 Vérification des améliorations des boutons...")
    
    with open('trombinoscope_app.py', 'r', encoding='utf-8') as f:
        code = f.read()
    
    improvements = {
        'Bouton Parcourir amélioré': 'browse_container = tk.Frame(path_frame, bg="white", relief=tk.RAISED',
        'Bouton Analyser avec relief': 'analyze_outer = tk.Frame(action_frame, bg=self.color_bg, relief=tk.RAISED',
        'Bouton Générer avec pulse': 'self.generate_btn = tk.Button(',
        'GIF repositionné': 'psyduck_gif_container = tk.Frame(action_frame, bg=self.color_bg, relief=tk.GROOVE',
        'Tooltips ajoutés': 'self.create_tooltip(',
        'Animation rebond': 'self.animate_psyduck_bounce()',
        'Effet pulse': 'self.pulse_generate_button()'
    }
    
    all_found = True
    for name, pattern in improvements.items():
        if pattern in code:
            print(f"✅ {name}")
        else:
            print(f"❌ {name} - non trouvé")
            all_found = False
    
    return all_found

def test_gif_position():
    """Vérifier que le GIF est bien positionné entre les deux boutons"""
    print("\n🔍 Vérification de la position du GIF Psyduck...")
    
    with open('trombinoscope_app.py', 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    # Trouver les lignes des boutons et du GIF
    analyze_line = None
    psyduck_line = None
    generate_line = None
    
    for i, line in enumerate(lines):
        if 'Analyser les classes' in line:
            analyze_line = i
        elif 'psyduck_gif_container = tk.Frame(action_frame' in line:
            psyduck_line = i
        elif 'Générer le Trombinoscope' in line and 'text=' in line:
            generate_line = i
    
    if analyze_line and psyduck_line and generate_line:
        if analyze_line < psyduck_line < generate_line:
            print(f"✅ GIF Psyduck bien positionné entre les boutons")
            print(f"   Ordre : Analyser (ligne {analyze_line}) → Psyduck (ligne {psyduck_line}) → Générer (ligne {generate_line})")
            return True
        else:
            print(f"❌ Position incorrecte du GIF")
            print(f"   Analyser: ligne {analyze_line}, Psyduck: ligne {psyduck_line}, Générer: ligne {generate_line}")
            return False
    else:
        print(f"⚠️  Impossible de déterminer les positions")
        return False

def main():
    """Exécuter tous les tests"""
    print("=" * 60)
    print("🧪 TESTS DES AMÉLIORATIONS DE L'APPLICATION TROMBINOSCOPE")
    print("=" * 60)
    
    results = []
    results.append(("Syntaxe Python", test_syntax()))
    results.append(("Nouvelles fonctions", test_functions_exist()))
    results.append(("Améliorations boutons", test_button_improvements()))
    results.append(("Position du GIF", test_gif_position()))
    
    print("\n" + "=" * 60)
    print("📊 RÉSUMÉ DES TESTS")
    print("=" * 60)
    
    all_passed = True
    for name, result in results:
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"{status} - {name}")
        if not result:
            all_passed = False
    
    print("=" * 60)
    if all_passed:
        print("🎉 TOUS LES TESTS SONT PASSÉS !")
        print("L'application est prête à être utilisée.")
        return 0
    else:
        print("⚠️  CERTAINS TESTS ONT ÉCHOUÉ")
        print("Veuillez vérifier les erreurs ci-dessus.")
        return 1

if __name__ == "__main__":
    sys.exit(main())
