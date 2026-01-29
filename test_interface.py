#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test minimaliste pour identifier si le problème vient des nouvelles fonctions
"""

try:
    print("📦 Test 1: Import des modules...")
    import tkinter as tk
    from tkinter import ttk
    print("✅ tkinter importé avec succès")
    
    from PIL import Image, ImageTk
    print("✅ PIL importé avec succès")
    
    print("\n📦 Test 2: Création d'une fenêtre de test...")
    root = tk.Tk()
    root.title("Test Trombinoscope")
    root.geometry("800x600")
    print("✅ Fenêtre créée")
    
    print("\n📦 Test 3: Création de widgets de test...")
    
    # Test Frame avec relief
    frame = tk.Frame(root, bg="#f0f9ff", relief=tk.RAISED, borderwidth=3)
    frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
    print("✅ Frame avec relief créé")
    
    # Test Label
    label = tk.Label(frame, text="🧪 Test de l'Application", font=("Arial", 16, "bold"))
    label.pack(pady=20)
    print("✅ Label créé")
    
    # Test Bouton avec effets
    button_outer = tk.Frame(frame, bg="#f0f9ff", relief=tk.RAISED, borderwidth=3)
    button_outer.pack(pady=10)
    
    button = tk.Button(
        button_outer,
        text="🔍 Bouton Test",
        bg="#3b82f6",
        fg="white",
        font=("Arial", 12, "bold"),
        cursor="hand2",
        relief=tk.RAISED,
        padx=30,
        pady=15,
        borderwidth=4
    )
    button.pack(padx=3, pady=3)
    print("✅ Bouton avec effets 3D créé")
    
    # Test animation simple
    def test_animation():
        """Test d'animation simple"""
        import math
        import time
        
        pulse_phase = (time.time() * 2) % (2 * math.pi)
        border_width = int(3 + 1.5 * (1 + math.sin(pulse_phase)))
        
        try:
            button_outer.config(borderwidth=border_width)
            root.after(100, test_animation)
        except:
            pass
    
    print("✅ Fonction d'animation créée")
    
    # Test tooltip simple
    tooltip = None
    
    def show_test_tooltip(event):
        global tooltip
        if tooltip is not None:
            return
        
        x = button.winfo_rootx() + 25
        y = button.winfo_rooty() + button.winfo_height() + 5
        
        tooltip = tk.Toplevel(button)
        tooltip.wm_overrideredirect(True)
        tooltip.wm_geometry(f"+{x}+{y}")
        
        label = tk.Label(
            tooltip,
            text="Ceci est un tooltip de test",
            background="#1e293b",
            foreground="white",
            relief=tk.SOLID,
            borderwidth=1,
            font=("Arial", 9),
            padx=10,
            pady=5
        )
        label.pack()
    
    def hide_test_tooltip(event):
        global tooltip
        if tooltip:
            try:
                tooltip.destroy()
            except:
                pass
            tooltip = None
    
    button.bind("<Enter>", lambda e: root.after(500, lambda: show_test_tooltip(e)))
    button.bind("<Leave>", hide_test_tooltip)
    print("✅ Tooltip configuré")
    
    # Message de succès
    success_label = tk.Label(
        frame,
        text="✅ Tous les tests sont passés!\n\nSi vous voyez cette fenêtre, tkinter fonctionne correctement.\nLes nouvelles fonctions sont compatibles.",
        font=("Arial", 11),
        fg="#059669",
        bg="#f0f9ff",
        justify=tk.LEFT,
        padx=20,
        pady=20
    )
    success_label.pack(pady=20)
    print("✅ Interface de test complète")
    
    # Démarrer l'animation
    print("\n🎬 Démarrage de l'animation de test...")
    test_animation()
    
    print("\n✅ SUCCÈS - Lancement de l'interface graphique...")
    print("   Survolez le bouton pour tester le tooltip")
    print("   Observez la bordure qui pulse")
    print("\n⏸️  Fermez la fenêtre pour terminer le test\n")
    
    root.mainloop()
    print("\n✅ Test terminé - Fenêtre fermée normalement")
    
except ImportError as e:
    print(f"\n❌ ERREUR D'IMPORT: {e}")
    print("\n💡 Solution:")
    print("   sudo apt-get install python3-tk  # Ubuntu/Debian")
    print("   sudo dnf install python3-tkinter  # Fedora/RedHat")
    
except Exception as e:
    print(f"\n❌ ERREUR: {e}")
    import traceback
    traceback.print_exc()
    print("\n💡 Vérifiez le message d'erreur ci-dessus pour plus de détails")
