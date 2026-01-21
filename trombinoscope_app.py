#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Application de Génération de Trombinoscope
Lycée Toulouse Lautrec
Version 2.0 - Corrigée par Thibaud DIDIER
"""

import os
import re
import tkinter as tk
from tkinter import ttk, filedialog, messagebox, scrolledtext
from PIL import Image, ImageTk
from pathlib import Path
from docx import Document
from docx.shared import Inches, Pt, RGBColor, Cm
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn
from docx.oxml import OxmlElement
import shutil
from datetime import datetime
import random


class TrombinoscopeApp:
    """Application principale de génération de trombinoscope"""
    
    def __init__(self, root):
        self.root = root
        self.root.title("Générateur de Trombinoscope - Lycée Toulouse Lautrec")
        self.root.geometry("900x750")
        
        # Variables
        self.classe_jpg_path = tk.StringVar()
        self.output_format = tk.StringVar(value="word")
        self.school_name = tk.StringVar(value="Lycée Toulouse Lautrec")
        self.school_year = tk.StringVar(value="2024-2025")
        self.classes_data = {}
        
        # Couleurs institutionnelles
        self.color_blue = "#000000"  # Noir (bandeau)
        self.color_green = "#059669"  # Vert
        self.color_light_blue = "#3b82f6"  # Bleu clair
        self.color_bg = "#f0f9ff"  # Fond bleu très clair
        
        # Messages Easter Egg
        self.easter_messages = [
            "La bouffe du self est dégueulasse.",
            "Le saviez-vous ? Sophian est l'AED ayant passé le plus de temps dans mon bureau, estimant que c'est sa planque.",
            "Spéciale dédicace à Karen qui anime la vie lycéenne !",
"La légende raconte qu'un certain Quentin Monnier serait directeur de colo ( et pas que ! )",
"Christophe Pagis est l'enseignant avec les plus belles cravattes du lycée.",
"Jarod peut remonter le temps grace à sa montre pendentif, seulement pendant son sommeil.",
"Un certain S est en concurence avec C pour la séduction des enseignants.",
"Larbi, ancien agent à Lautrec, a voulu se battre avec l'AED TICE et s'est fait virer depuis",
"Les cookies de la cafet sont délicieux.",
"Chose la plus insolite retrouvée dans un casier de prof : Un trognon de pomme et un dentier.",
"Non Sarah, ce n'est pas à moi de changer la cartouche de ton imprimante.",
"Les élèves de Mr Tempier semblent avoir le droit de faire un baseball en plein cours.",
"Regardez le top 10 des élèves sanctionnés sur pronote, c'est surprenant. ",
"En 2025, 2 AED ont vécu des choses pationnantes dans une salle de cours. Plusieurs fois.",
"Mr Maiurano, ancien CPE, avait comme mot de passe pomme de pain ",
"Cathy Condy a été ma maman spirituelle.",
"Clement est un futur pompier, qui n'éteint pas que le feu des batiments.",
"Non ECE, je ne te donnerai pas les identifiants admin pour que tu installes Paint.net ",
"Econocom est vraiment la pire boite.",
"Jarod, ta bien-pensance est appréciable, ta non-tolérance l'est moins, mais je t'aime.",
"Maryse fait la gueule toute la matinée ( sauf si Clément est présent ).",
"Une AED a déjà fait un resto basket au 100 couvert pour la saint valentin !",
"Une pièce souterraine avec des poupées et des rituels vaudous a existé au lycée",
"Le tacos aux légumes de la cafet est sous-coté mais il est très bon.",
"Julien Pharos fait pleuvoir lorsqu'il chante au Boulis.",
"Chaque année, des dizaines de rats crevés sont découverts dans les faux-plafonds.",
"En Octobre 2025, quelqu'un a chié au niveau de la passerelle #cacagate",
"Des lacrymos ont été entierement vidées dans les WC en 2025",
"Marc Touya , arrête la clope mon champion.",
"Des AED qui chopent des profs ? Oui ça s'est déjà fait.",
"Des AED qui chopent des AED ? Oui, ça s'est déjà fait. Le Chene est dans la Scierie.",
"Un élève a donné comme devoir PETE MOI LA CHATTE , en se connectant au Pronote d'une prof.",
"La prof qui s'est fait 'pirater' son Pronote, a admis qu'elle s'était absentée 15mn du cours.",
"Julien Pharos est l'enseignant avec le plus de retard au lycée, environ 15 mn par cours.",
"Pauline , l'agent d'entretien a été ma seconde maman spirituelle, hein St Antoine de Padou !",
"Certains contacts du téléphone pro ont été renommé avant l'arrivée de Paul.",
"Mmr Novoa est objectivement l'une des personnes les plus humaines de l'établissement. ",
"Julien pharos a reçu un tracte de reconquête dans son casier par pure provocation.",
"Marc Andral a été la personne la moins pédagogique de l'établissement, comble d'un prof.",
"Edouard Romera & Mylene Fournier sont les profs en couple les plus cools !",
"Le bourrage papier de l'imprimante de Davina était en fait un sachet de beuh coincé.",
"Brigitte de la Cafet a écrit un livre.",
"Sirine est l'AED a qui vous ne pouvez confier aucun secret.",
"Sophian investi dans des paris sportifs grâce à ChatGPT, mais reste en négatif.",
            "Marc Andral est un CONNARD :-) . Pardon, un GROS CONNARD !"
        ]
        self.easter_message_index = 0  # Index pour messages séquentiels
        
        # Messages de chargement aléatoires
        self.loading_messages = [
            "Ajout d'accusation des mérovingiens",
            "Suppression des organes de Marc Andral",
            "Correction colorimétrique de Cheveux de feu",
            "Redimensionnement de MimiMathy.png",
            "Ajout de pépites de chocolat sur les photos de classe",
            "Conversion des photos au format .fdp",
            "Mise en surtension de Michel Chaboy",
            "Téléchargement du DLC « France du tiers monde »",
            "Le saviez-vous ? Les pieuvres ont trois cœurs et leur sang est bleu.",
            "Le saviez-vous ? Les vaches ont des meilleures amies et stressent quand elles sont séparées.",
            "Le saviez-vous ? Les escargots peuvent dormir jusqu'à trois ans.",
            "Le saviez-vous ? Les manchots demandent leur partenaire en mariage avec un caillou.",
            "Le saviez-vous ? Les requins ne peuvent pas tomber malades du cancer.",
            "Le saviez-vous ? Au Japon, il existe des îles entières peuplées de chats.",
            "Le saviez-vous ? La France possède le plus grand nombre de fuseaux horaires au monde.",
            "Le saviez-vous ? En Écosse, il existe 421 mots pour dire « neige ».",
            "Le saviez-vous ? En Australie, il y a plus de kangourous que d'humains.",
            "Le saviez-vous ? En Bolivie, il existe un marché de sorcellerie totalement légal.",
            "Le saviez-vous ? Au Danemark, on casse de la vaisselle devant la porte des amis pour leur porter chance.",
            "Le saviez-vous ? En Corée du Sud, l'âge commence traditionnellement à un an dès la naissance.",
            "Le saviez-vous ? En allemand, il existe un mot pour le plaisir ressenti face à l'échec d'autrui : Schadenfreude.",
            "Le saviez-vous ? Les grenouilles peuvent geler complètement en hiver… puis revenir à la vie au printemps.",
            "Le saviez-vous ? Les vaches peuvent monter les escaliers mais pas les descendre.",
            "Le saviez-vous ? Les dauphins dorment avec un seul hémisphère du cerveau à la fois.",
            "Le saviez-vous ? En Écosse, on peut frapper à n'importe quelle porte le Nouvel An pour porter chance.",
            "Le saviez-vous ? En France, il est illégal de nommer un cochon Napoléon.",
            "Le saviez-vous ? Les humains partagent environ 60 % de leur ADN avec les bananes.",
            "Le saviez-vous ? Certains champignons peuvent contrôler le cerveau des insectes.",
            "Le saviez-vous ? Les axolotls peuvent régénérer leur cerveau et leur cœur.",
            "Le saviez-vous ? Les crevettes-pistolets produisent un son plus fort qu'un coup de feu.",
            "Le saviez-vous ? Les requins peuvent vivre plus de 400 ans (requin du Groenland).",
            "Le saviez-vous ? La Tour Eiffel grandit d'environ 15 cm en été.",
            "Le saviez-vous ? Ton nez peut reconnaître plus d'un trillion d'odeurs."
        ]
        
        self.setup_ui()
        self.create_menu()
    
    def create_modern_button(self, parent, text, command, bg_color, width=None):
        """Créer un bouton moderne avec coins arrondis et style amélioré"""
        # Frame pour simuler les coins arrondis avec un effet d'ombre
        button_container = tk.Frame(parent, bg=parent.cget('bg'))
        
        button = tk.Button(
            button_container,
            text=text,
            command=command,
            bg=bg_color,
            fg="white",
            font=("Arial", 11, "bold"),
            cursor="hand2",
            relief=tk.FLAT,
            padx=25,
            pady=12,
            activebackground=self.get_darker_color(bg_color),
            activeforeground="white",
            borderwidth=0,
            highlightthickness=0
        )
        
        if width:
            button.config(width=width)
        
        button.pack()
        
        # Effets hover
        def on_enter(e):
            button.config(bg=self.get_darker_color(bg_color))
        
        def on_leave(e):
            button.config(bg=bg_color)
        
        button.bind("<Enter>", on_enter)
        button.bind("<Leave>", on_leave)
        
        return button_container
    
    def get_darker_color(self, hex_color):
        """Obtenir une version plus foncée d'une couleur"""
        # Supprimer le #
        hex_color = hex_color.lstrip('#')
        # Convertir en RGB
        r, g, b = tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
        # Assombrir de 20%
        r = max(0, int(r * 0.8))
        g = max(0, int(g * 0.8))
        b = max(0, int(b * 0.8))
        # Reconvertir en hex
        return f'#{r:02x}{g:02x}{b:02x}'
        
    def create_menu(self):
        """Création du menu avec l'onglet À propos et Aide"""
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)
        
        # Menu Aide
        help_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Aide", menu=help_menu)
        help_menu.add_command(label="Guide d'utilisation", command=self.show_help)
        
        # Menu À propos
        about_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="À propos", menu=about_menu)
        about_menu.add_command(label="À propos de l'application", command=self.show_about)
        
    def show_about(self):
        """Afficher la fenêtre À propos"""
        messagebox.showinfo(
            "À propos",
            "Ce logiciel a été réalisé par Thibaud DIDIER,\n"
            "pour aider les prochains AED TICE esclavagisés\n"
            "par ces tâches ingrates."
        )
    
    def show_help(self):
        """Afficher le guide d'aide depuis README_TROMBINOSCOPE.md"""
        readme_path = os.path.join(os.path.dirname(__file__), "README_TROMBINOSCOPE.md")
        
        # Créer une fenêtre popup
        popup = tk.Toplevel(self.root)
        popup.title("📚 Guide d'utilisation - Trombinoscope")
        popup.geometry("900x700")
        popup.configure(bg="white")
        
        # Centrer la fenêtre
        popup.transient(self.root)
        
        # Frame principale
        main_frame = tk.Frame(popup, bg="white", padx=20, pady=20)
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Titre
        title_label = tk.Label(
            main_frame,
            text="📚 Guide d'utilisation",
            font=("Arial", 16, "bold"),
            bg="white",
            fg=self.color_blue
        )
        title_label.pack(pady=(0, 15))
        
        # Zone de texte avec défilement pour afficher le README
        text_frame = tk.Frame(main_frame, bg="white")
        text_frame.pack(fill=tk.BOTH, expand=True)
        
        help_text = scrolledtext.ScrolledText(
            text_frame,
            font=("Courier", 9),
            wrap=tk.WORD,
            bg="#f8fafc",
            relief=tk.FLAT,
            padx=10,
            pady=10
        )
        help_text.pack(fill=tk.BOTH, expand=True)
        
        # Charger et afficher le contenu du README
        try:
            if os.path.exists(readme_path):
                with open(readme_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                    help_text.insert(tk.END, content)
            else:
                help_text.insert(tk.END, "⚠️ Fichier README_TROMBINOSCOPE.md introuvable.\n\n")
                help_text.insert(tk.END, "Le guide d'utilisation devrait se trouver dans le dossier de l'application.")
        except Exception as e:
            help_text.insert(tk.END, f"❌ Erreur lors du chargement du guide :\n{str(e)}")
        
        help_text.config(state=tk.DISABLED)
        
        # Bouton Fermer
        close_container = tk.Frame(main_frame, bg="white")
        close_container.pack(pady=(15, 0))
        
        close_btn = tk.Button(
            close_container,
            text="Fermer",
            command=popup.destroy,
            bg=self.color_green,
            fg="white",
            font=("Arial", 11, "bold"),
            cursor="hand2",
            relief=tk.FLAT,
            padx=30,
            pady=10,
            activebackground="#047857",
            borderwidth=0,
            highlightthickness=0
        )
        close_btn.pack()
        
        def close_on_enter(e):
            close_btn.config(bg="#047857")
        def close_on_leave(e):
            close_btn.config(bg=self.color_green)
        close_btn.bind("<Enter>", close_on_enter)
        close_btn.bind("<Leave>", close_on_leave)
        
    def show_easter_egg(self):
        """Afficher un message Easter Egg séquentiel (appelé après victoire du mini-jeu)"""
        # Utiliser l'index actuel au lieu de random
        message = self.easter_messages[self.easter_message_index]
        
        # Incrémenter l'index pour le prochain clic (avec boucle)
        self.easter_message_index = (self.easter_message_index + 1) % len(self.easter_messages)
        
        return message  # Retourner le message pour l'utiliser dans le mini-jeu
    
    def show_whack_a_psyduck_game(self):
        """Afficher le mini-jeu Tape-Taupe avec Psykokwak"""
        # Créer une fenêtre popup pour le jeu
        game_popup = tk.Toplevel(self.root)
        game_popup.title("🎮 Assomme le Psykokwak !")
        game_popup.geometry("700x750")
        game_popup.configure(bg="#1a1a2e")
        game_popup.resizable(False, False)
        
        # Centrer la fenêtre
        game_popup.transient(self.root)
        game_popup.grab_set()
        
        # Variables du jeu stockées dans self pour accès global
        self.game_state = {
            'hits': 0,
            'target_hits': 3,
            'current_hole': None,
            'game_active': True,
            'psyduck_visible': False,
            'game_timer': None,
            'popup': game_popup,
            'hole_labels': [],
            'score_label': None,
            'result_label': None,
            'replay_btn': None,
            'close_btn': None,
            'psyduck_image': None
        }
        
        # Frame principale avec fond dégradé simulé
        main_frame = tk.Frame(game_popup, bg="#1a1a2e", padx=30, pady=20)
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Titre du jeu avec style
        title_frame = tk.Frame(main_frame, bg="#1a1a2e")
        title_frame.pack(pady=(0, 10))
        
        title_label = tk.Label(
            title_frame,
            text="🦆 ASSOMME LE PSYKOKWAK ! 🦆",
            font=("Arial", 20, "bold"),
            bg="#1a1a2e",
            fg="#ffd700"
        )
        title_label.pack()
        
        subtitle_label = tk.Label(
            title_frame,
            text="Clique sur Psykokwak 3 fois pour obtenir un secret !",
            font=("Arial", 11),
            bg="#1a1a2e",
            fg="#a0a0a0"
        )
        subtitle_label.pack(pady=(5, 0))
        
        # Compteur de score
        score_frame = tk.Frame(main_frame, bg="#16213e", padx=20, pady=10)
        score_frame.pack(pady=(10, 20))
        
        self.game_state['score_label'] = tk.Label(
            score_frame,
            text="🎯 Score: 0 / 3",
            font=("Arial", 16, "bold"),
            bg="#16213e",
            fg="#00ff88"
        )
        self.game_state['score_label'].pack()
        
        # Frame du jeu (grille 3x3)
        game_frame = tk.Frame(main_frame, bg="#1a1a2e")
        game_frame.pack(pady=10)
        
        # Charger l'image du psyduck pour le jeu
        try:
            psyduck_game_path = os.path.join(os.path.dirname(__file__), "assets", "psyduck.png")
            psyduck_game_img = Image.open(psyduck_game_path)
            psyduck_game_img = psyduck_game_img.resize((70, 70), Image.Resampling.LANCZOS)
            self.game_state['psyduck_image'] = ImageTk.PhotoImage(psyduck_game_img)
        except Exception as e:
            print(f"Erreur chargement psyduck pour le jeu: {e}")
        
        # Créer les 9 trous (3x3)
        for row in range(3):
            for col in range(3):
                # Container pour chaque trou avec effet d'ombre
                hole_container = tk.Frame(game_frame, bg="#1a1a2e", padx=8, pady=8)
                hole_container.grid(row=row, column=col)
                
                # Le "trou" avec effet 3D
                hole_frame = tk.Frame(
                    hole_container,
                    bg="#0d1117",
                    highlightbackground="#2d3748",
                    highlightthickness=3,
                    width=100,
                    height=100
                )
                hole_frame.pack_propagate(False)
                hole_frame.pack()
                
                # Label pour afficher le psyduck ou rien
                hole_label = tk.Label(
                    hole_frame,
                    bg="#0d1117",
                    width=100,
                    height=100,
                    cursor="crosshair"
                )
                hole_label.pack(expand=True, fill=tk.BOTH)
                
                # Index du trou
                hole_index = row * 3 + col
                self.game_state['hole_labels'].append(hole_label)
                
                # Binding pour le clic sur le trou - utilise une méthode de classe
                hole_label.bind("<Button-1>", lambda e, idx=hole_index: self.on_game_hole_click(idx))
        
        # Frame pour le message de résultat
        result_frame = tk.Frame(main_frame, bg="#1a1a2e")
        result_frame.pack(pady=(20, 10), fill=tk.X)
        
        self.game_state['result_label'] = tk.Label(
            result_frame,
            text="",
            font=("Arial", 11),
            bg="#1a1a2e",
            fg="#ffffff",
            wraplength=550,
            justify=tk.CENTER
        )
        self.game_state['result_label'].pack()
        
        # Frame pour les boutons
        button_frame = tk.Frame(main_frame, bg="#1a1a2e")
        button_frame.pack(pady=(15, 0))
        
        # Bouton rejouer (initialement caché)
        self.game_state['replay_btn'] = tk.Button(
            button_frame,
            text="🔄 Rejouer",
            command=self.restart_whack_game,
            bg="#059669",
            fg="white",
            font=("Arial", 12, "bold"),
            cursor="hand2",
            relief=tk.FLAT,
            padx=25,
            pady=10,
            activebackground="#047857",
            borderwidth=0
        )
        
        # Bouton fermer (initialement caché)
        self.game_state['close_btn'] = tk.Button(
            button_frame,
            text="✖ Fermer",
            command=self.close_whack_game,
            bg="#6b7280",
            fg="white",
            font=("Arial", 12, "bold"),
            cursor="hand2",
            relief=tk.FLAT,
            padx=25,
            pady=10,
            activebackground="#4b5563",
            borderwidth=0
        )
        
        # Effets hover pour les boutons
        self.game_state['replay_btn'].bind("<Enter>", lambda e: self.game_state['replay_btn'].config(bg="#047857"))
        self.game_state['replay_btn'].bind("<Leave>", lambda e: self.game_state['replay_btn'].config(bg="#059669"))
        self.game_state['close_btn'].bind("<Enter>", lambda e: self.game_state['close_btn'].config(bg="#4b5563"))
        self.game_state['close_btn'].bind("<Leave>", lambda e: self.game_state['close_btn'].config(bg="#6b7280"))
        
        # Fermer proprement si la fenêtre est fermée
        game_popup.protocol("WM_DELETE_WINDOW", self.close_whack_game)
        
        # Démarrer le jeu après un court délai
        game_popup.after(800, self.show_psyduck_random)
    
    def on_game_hole_click(self, hole_idx):
        """Gestionnaire de clic sur un trou du jeu"""
        if not self.game_state['game_active']:
            return
        
        if self.game_state['psyduck_visible'] and self.game_state['current_hole'] == hole_idx:
            # TOUCHÉ !
            self.game_state['hits'] += 1
            self.game_state['score_label'].config(text=f"🎯 Score: {self.game_state['hits']} / 3")
            
            # Effet visuel de touche
            self.game_state['hole_labels'][hole_idx].config(bg="#00ff00")
            self.game_state['popup'].after(150, lambda: self.game_state['hole_labels'][hole_idx].config(bg="#0d1117"))
            
            # Cacher le psyduck immédiatement
            self.hide_game_psyduck()
            
            # Vérifier la victoire
            if self.game_state['hits'] >= self.game_state['target_hits']:
                self.game_state['game_active'] = False
                self.game_state['popup'].after(300, self.show_game_victory)
            else:
                # Continuer le jeu après un court délai
                self.game_state['popup'].after(500, self.show_psyduck_random)
    
    def show_psyduck_random(self):
        """Afficher le psyduck dans un trou aléatoire"""
        if not self.game_state['game_active']:
            return
        
        # Cacher l'ancien psyduck si visible
        self.hide_game_psyduck()
        
        # Choisir un nouveau trou aléatoire
        new_hole = random.randint(0, 8)
        self.game_state['current_hole'] = new_hole
        self.game_state['psyduck_visible'] = True
        
        # Afficher le psyduck
        if self.game_state['psyduck_image']:
            self.game_state['hole_labels'][new_hole].config(image=self.game_state['psyduck_image'], bg="#2d3748")
        else:
            self.game_state['hole_labels'][new_hole].config(text="🦆", font=("Arial", 40), bg="#2d3748")
        
        # Programmer la disparition après un délai (400-600ms)
        hide_delay = random.randint(400, 600)
        self.game_state['game_timer'] = self.game_state['popup'].after(hide_delay, self.auto_hide_psyduck)
    
    def auto_hide_psyduck(self):
        """Cacher le psyduck et en afficher un autre - RATÉ = score à 0"""
        if self.game_state['psyduck_visible'] and self.game_state['game_active']:
            # Le psyduck a disparu sans être cliqué = RATÉ
            if self.game_state['hits'] > 0:
                self.game_state['hits'] = 0
                self.game_state['score_label'].config(text="🎯 Score: 0 / 3", fg="#ff4444")
                self.game_state['popup'].after(300, lambda: self.game_state['score_label'].config(fg="#00ff88"))
            self.hide_game_psyduck()
            # Afficher un nouveau psyduck après un court délai
            self.game_state['popup'].after(300, self.show_psyduck_random)
    
    def hide_game_psyduck(self):
        """Cacher le psyduck actuel"""
        if self.game_state['current_hole'] is not None:
            self.game_state['hole_labels'][self.game_state['current_hole']].config(image='', text='', bg="#0d1117")
        self.game_state['psyduck_visible'] = False
        if self.game_state['game_timer']:
            self.game_state['popup'].after_cancel(self.game_state['game_timer'])
            self.game_state['game_timer'] = None
    
    def show_game_victory(self):
        """Afficher l'écran de victoire avec le message Easter Egg"""
        # Obtenir le message séquentiel
        message = self.show_easter_egg()
        
        # Afficher le message de victoire
        self.game_state['result_label'].config(
            text=f"🎉 BRAVO ! Tu as assommé Psykokwak !\n\n💬 \"{message}\"",
            fg="#ffd700",
            font=("Arial", 12, "bold")
        )
        
        # Forcer la mise à jour
        self.game_state['popup'].update_idletasks()
        
        # Afficher les boutons rejouer et fermer
        self.game_state['replay_btn'].pack(side=tk.LEFT, padx=10)
        self.game_state['close_btn'].pack(side=tk.LEFT, padx=10)
        
        # Forcer à nouveau la mise à jour pour s'assurer que les boutons sont visibles
        self.game_state['popup'].update_idletasks()
    
    def restart_whack_game(self):
        """Redémarrer le jeu"""
        self.game_state['hits'] = 0
        self.game_state['current_hole'] = None
        self.game_state['game_active'] = True
        self.game_state['psyduck_visible'] = False
        
        self.game_state['score_label'].config(text="🎯 Score: 0 / 3", fg="#00ff88")
        self.game_state['result_label'].config(text="", font=("Arial", 11))
        
        # Cacher les boutons
        self.game_state['replay_btn'].pack_forget()
        self.game_state['close_btn'].pack_forget()
        
        # Cacher tous les psyducks
        for label in self.game_state['hole_labels']:
            label.config(image='', text='', bg="#0d1117")
        
        # Redémarrer le jeu
        self.game_state['popup'].after(500, self.show_psyduck_random)
    
    def close_whack_game(self):
        """Fermer le jeu"""
        self.game_state['game_active'] = False
        if self.game_state['game_timer']:
            self.game_state['popup'].after_cancel(self.game_state['game_timer'])
        self.game_state['popup'].destroy()
    
    def show_missing_photos_alert(self, missing_count):
        """Afficher une alerte pour les photos manquantes (21ko)"""
        # Créer une fenêtre popup
        popup = tk.Toplevel(self.root)
        popup.title("⚠️ Photos manquantes détectées")
        popup.geometry("600x500")
        popup.configure(bg="white")
        popup.resizable(False, False)
        
        # Centrer la fenêtre
        popup.transient(self.root)
        popup.grab_set()
        
        # Frame principale
        main_frame = tk.Frame(popup, bg="white", padx=25, pady=25)
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Titre
        title_label = tk.Label(
            main_frame,
            text="⚠️ Attention : Photos manquantes détectées",
            font=("Arial", 14, "bold"),
            bg="white",
            fg="#dc2626"
        )
        title_label.pack(pady=(0, 15))
        
        # Image portrait "inconnu"
        try:
            portrait_path = os.path.join(os.path.dirname(__file__), "assets", "portrait.png")
            if os.path.exists(portrait_path):
                portrait_img = Image.open(portrait_path)
                portrait_img = portrait_img.resize((100, 100), Image.Resampling.LANCZOS)
                self.portrait_photo = ImageTk.PhotoImage(portrait_img)
                
                portrait_label = tk.Label(
                    main_frame,
                    image=self.portrait_photo,
                    bg="white"
                )
                portrait_label.pack(pady=10)
        except Exception as e:
            print(f"Erreur chargement portrait: {e}")
        
        # Message principal
        message_text = (
            f"{missing_count} élève{'s' if missing_count > 1 else ''} sans photo {'ont' if missing_count > 1 else 'a'} été détecté{'s' if missing_count > 1 else ''}.\n\n"
            "Ces élèves ont une photo portrait \"inconnu\" pesant précisément 21 ko.\n\n"
            "Pour obtenir un meilleur trombinoscope, il est préférable de récupérer\n"
            "ces photos depuis une extraction Pronote si possible."
        )
        
        msg_label = tk.Label(
            main_frame,
            text=message_text,
            font=("Arial", 11),
            bg="white",
            wraplength=550,
            justify=tk.CENTER
        )
        msg_label.pack(pady=20)
        
        # Info supplémentaire
        info_label = tk.Label(
            main_frame,
            text="Ce message est purement informatif.",
            font=("Arial", 9, "italic"),
            bg="white",
            fg="#6b7280"
        )
        info_label.pack(pady=(10, 20))
        
        # Frame pour les boutons
        buttons_frame = tk.Frame(main_frame, bg="white")
        buttons_frame.pack(pady=5)
        
        # Bouton "Réparer avec une extraction Pronote" - Style moderne
        repair_container = tk.Frame(buttons_frame, bg="white")
        repair_container.pack(side=tk.LEFT, padx=5)
        
        repair_btn = tk.Button(
            repair_container,
            text="🔧 Réparer avec Pronote",
            command=lambda: [popup.destroy(), self.show_pronote_instructions()],
            bg=self.color_light_blue,
            fg="white",
            font=("Arial", 11, "bold"),
            cursor="hand2",
            relief=tk.FLAT,
            padx=25,
            pady=12,
            activebackground="#2563eb",
            borderwidth=0,
            highlightthickness=0
        )
        repair_btn.pack()
        
        # Effets hover pour repair_btn
        def repair_on_enter(e):
            repair_btn.config(bg="#2563eb")
        def repair_on_leave(e):
            repair_btn.config(bg=self.color_light_blue)
        repair_btn.bind("<Enter>", repair_on_enter)
        repair_btn.bind("<Leave>", repair_on_leave)
        
        # Bouton "Ignorer" - Style moderne
        ignore_container = tk.Frame(buttons_frame, bg="white")
        ignore_container.pack(side=tk.LEFT, padx=5)
        
        ignore_btn = tk.Button(
            ignore_container,
            text="Ignorer",
            command=popup.destroy,
            bg=self.color_green,
            fg="white",
            font=("Arial", 11, "bold"),
            cursor="hand2",
            relief=tk.FLAT,
            padx=35,
            pady=12,
            activebackground="#047857",
            borderwidth=0,
            highlightthickness=0
        )
        ignore_btn.pack()
        
        # Effets hover pour ignore_btn
        def ignore_on_enter(e):
            ignore_btn.config(bg="#047857")
        def ignore_on_leave(e):
            ignore_btn.config(bg=self.color_green)
        ignore_btn.bind("<Enter>", ignore_on_enter)
        ignore_btn.bind("<Leave>", ignore_on_leave)
    
    def show_pronote_instructions(self):
        """Afficher les instructions pour exporter les photos depuis Pronote"""
        # Créer une fenêtre popup
        popup = tk.Toplevel(self.root)
        popup.title("📋 Instructions d'export Pronote")
        popup.geometry("700x650")
        popup.configure(bg="white")
        popup.resizable(False, False)
        
        # Centrer la fenêtre
        popup.transient(self.root)
        popup.grab_set()
        
        # Frame principale avec scrollbar
        main_frame = tk.Frame(popup, bg="white")
        main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Titre
        title_label = tk.Label(
            main_frame,
            text="📋 Comment exporter les photos depuis Pronote",
            font=("Arial", 14, "bold"),
            bg="white",
            fg=self.color_blue
        )
        title_label.pack(pady=(0, 20))
        
        # Instructions
        instructions = [
            "1. Ouvrez Pronote.",
            "2. En haut, dans l'onglet \"Import-Export\", cliquez sur \"Exporter les photos des élèves\".",
            "3. Choisissez ou créez un dossier d'emplacement vide.",
            "4. Dans \"Syntaxe utilisée pour le nom des photos exportées\", choisir Nom-Prénom.",
            "   ⚠️ Le tiret est très important !"
        ]
        
        for instruction in instructions:
            instr_label = tk.Label(
                main_frame,
                text=instruction,
                font=("Arial", 10),
                bg="white",
                justify=tk.LEFT,
                anchor="w"
            )
            instr_label.pack(fill=tk.X, pady=3)
        
        # Afficher l'image d'exemple
        try:
            pronote_img_path = os.path.join(os.path.dirname(__file__), "assets", "pronote_export.png")
            if os.path.exists(pronote_img_path):
                pronote_img = Image.open(pronote_img_path)
                # Redimensionner l'image si nécessaire pour qu'elle tienne dans la fenêtre
                max_width = 650
                max_height = 300
                img_width, img_height = pronote_img.size
                
                # Calculer le ratio pour maintenir les proportions
                ratio = min(max_width / img_width, max_height / img_height)
                new_width = int(img_width * ratio)
                new_height = int(img_height * ratio)
                
                pronote_img = pronote_img.resize((new_width, new_height), Image.Resampling.LANCZOS)
                self.pronote_photo = ImageTk.PhotoImage(pronote_img)
                
                img_label = tk.Label(
                    main_frame,
                    image=self.pronote_photo,
                    bg="white",
                    relief=tk.SOLID,
                    borderwidth=1
                )
                img_label.pack(pady=15)
        except Exception as e:
            print(f"Erreur chargement image pronote: {e}")
        
        # Dernière instruction
        final_instr = tk.Label(
            main_frame,
            text="5. Lancez l'export.",
            font=("Arial", 10),
            bg="white",
            justify=tk.LEFT,
            anchor="w"
        )
        final_instr.pack(fill=tk.X, pady=3)
        
        # Séparateur
        separator = tk.Frame(main_frame, height=2, bg="#e5e7eb")
        separator.pack(fill=tk.X, pady=15)
        
        # Message d'information
        info_msg = tk.Label(
            main_frame,
            text="Une fois l'export terminé, cliquez sur \"Continuer\" pour sélectionner\nle dossier contenant les photos exportées.",
            font=("Arial", 9, "italic"),
            bg="white",
            fg="#6b7280",
            justify=tk.CENTER
        )
        info_msg.pack(pady=10)
        
        # Frame pour les boutons
        buttons_frame = tk.Frame(main_frame, bg="white")
        buttons_frame.pack(pady=10)
        
        # Bouton Annuler - Style moderne
        cancel_container = tk.Frame(buttons_frame, bg="white")
        cancel_container.pack(side=tk.LEFT, padx=5)
        
        cancel_btn = tk.Button(
            cancel_container,
            text="❌ Annuler",
            command=popup.destroy,
            bg="#6b7280",
            fg="white",
            font=("Arial", 11, "bold"),
            cursor="hand2",
            relief=tk.FLAT,
            padx=25,
            pady=12,
            activebackground="#4b5563",
            borderwidth=0,
            highlightthickness=0
        )
        cancel_btn.pack()
        
        def cancel_on_enter(e):
            cancel_btn.config(bg="#4b5563")
        def cancel_on_leave(e):
            cancel_btn.config(bg="#6b7280")
        cancel_btn.bind("<Enter>", cancel_on_enter)
        cancel_btn.bind("<Leave>", cancel_on_leave)
        
        # Bouton Continuer - Style moderne
        continue_container = tk.Frame(buttons_frame, bg="white")
        continue_container.pack(side=tk.LEFT, padx=5)
        
        continue_btn = tk.Button(
            continue_container,
            text="✅ Continuer",
            command=lambda: [popup.destroy(), self.repair_with_pronote()],
            bg=self.color_green,
            fg="white",
            font=("Arial", 11, "bold"),
            cursor="hand2",
            relief=tk.FLAT,
            padx=25,
            pady=12,
            activebackground="#047857",
            borderwidth=0,
            highlightthickness=0
        )
        continue_btn.pack()
        
        def continue_on_enter(e):
            continue_btn.config(bg="#047857")
        def continue_on_leave(e):
            continue_btn.config(bg=self.color_green)
        continue_btn.bind("<Enter>", continue_on_enter)
        continue_btn.bind("<Leave>", continue_on_leave)
    
    def repair_with_pronote(self):
        """Réparer les photos manquantes avec les photos Pronote"""
        # Demander le dossier Pronote
        pronote_folder = filedialog.askdirectory(
            title="Sélectionnez le dossier contenant les photos exportées de Pronote"
        )
        
        if not pronote_folder:
            return
        
        classe_jpg_path = self.classe_jpg_path.get()
        
        if not classe_jpg_path or not os.path.exists(classe_jpg_path):
            messagebox.showerror("Erreur", "Le dossier CLASSE_JPG n'est pas valide.")
            return
        
        self.update_status("Réparation des photos en cours...")
        
        # Statistiques
        photos_replaced = 0
        photos_still_missing = 0
        missing_photos_details = []
        
        try:
            # Créer un dictionnaire des photos Pronote (nom fichier -> chemin complet)
            pronote_photos = {}
            for file in os.listdir(pronote_folder):
                if file.lower().endswith(('.jpg', '.jpeg', '.png')):
                    # Extraire le nom sans extension
                    name = os.path.splitext(file)[0]
                    file_path = os.path.join(pronote_folder, file)
                    pronote_photos[name] = file_path
            
            # Parcourir les classes dans CLASSE_JPG
            for class_name in os.listdir(classe_jpg_path):
                class_path = os.path.join(classe_jpg_path, class_name)
                
                if not os.path.isdir(class_path):
                    continue
                
                # Parcourir les photos de la classe
                for file in os.listdir(class_path):
                    if file.lower().endswith(('.jpg', '.jpeg', '.png')):
                        file_path = os.path.join(class_path, file)
                        file_size = os.path.getsize(file_path)
                        
                        # Vérifier si c'est une photo "inconnu" de 21ko
                        if 20500 <= file_size <= 21500:
                            # Extraire le nom (NOM-Prenom)
                            name = os.path.splitext(file)[0]
                            
                            # Chercher la photo correspondante dans le dossier Pronote
                            if name in pronote_photos:
                                pronote_photo_path = pronote_photos[name]
                                
                                # Vérifier que la photo Pronote n'est pas aussi une photo "inconnu"
                                pronote_size = os.path.getsize(pronote_photo_path)
                                if 20500 <= pronote_size <= 21500:
                                    # La photo Pronote est aussi "inconnu"
                                    photos_still_missing += 1
                                    missing_photos_details.append({
                                        'name': name,
                                        'class': class_name,
                                        'reason': 'Photo Pronote aussi "inconnu"'
                                    })
                                else:
                                    # Remplacer la photo
                                    shutil.copy2(pronote_photo_path, file_path)
                                    photos_replaced += 1
                            else:
                                # Photo non trouvée dans le dossier Pronote
                                photos_still_missing += 1
                                missing_photos_details.append({
                                    'name': name,
                                    'class': class_name,
                                    'reason': 'Non trouvé dans dossier Pronote'
                                })
            
            # Afficher le récapitulatif
            self.show_repair_summary(photos_replaced, photos_still_missing, missing_photos_details)
            
            # Re-analyser les classes pour mettre à jour l'aperçu
            if photos_replaced > 0:
                self.analyze_classes()
            
        except Exception as e:
            messagebox.showerror("Erreur", f"Erreur lors de la réparation :\n{str(e)}")
            self.update_status("Erreur lors de la réparation")
            import traceback
            traceback.print_exc()
    
    def show_repair_summary(self, replaced_count, still_missing_count, missing_details):
        """Afficher le récapitulatif de la réparation"""
        # Créer une fenêtre popup
        popup = tk.Toplevel(self.root)
        popup.title("✅ Récapitulatif de la réparation")
        popup.geometry("650x550")
        popup.configure(bg="white")
        popup.resizable(False, False)
        
        # Centrer la fenêtre
        popup.transient(self.root)
        popup.grab_set()
        
        # Frame principale
        main_frame = tk.Frame(popup, bg="white", padx=25, pady=25)
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Titre
        title_label = tk.Label(
            main_frame,
            text="✅ Récapitulatif de la réparation",
            font=("Arial", 14, "bold"),
            bg="white",
            fg=self.color_blue
        )
        title_label.pack(pady=(0, 20))
        
        # Statistiques
        stats_frame = tk.Frame(main_frame, bg="#f0f9ff", relief=tk.FLAT, padx=20, pady=15)
        stats_frame.pack(fill=tk.X, pady=10)
        
        # Photos remplacées
        replaced_label = tk.Label(
            stats_frame,
            text=f"✅ Photos correctement remplacées : {replaced_count}",
            font=("Arial", 11, "bold"),
            bg="#f0f9ff",
            fg=self.color_green
        )
        replaced_label.pack(anchor="w", pady=5)
        
        # Photos toujours manquantes
        missing_label = tk.Label(
            stats_frame,
            text=f"⚠️ Photos toujours manquantes : {still_missing_count}",
            font=("Arial", 11, "bold"),
            bg="#f0f9ff",
            fg="#dc2626" if still_missing_count > 0 else "#6b7280"
        )
        missing_label.pack(anchor="w", pady=5)
        
        # Détails des photos manquantes (si applicable)
        if still_missing_count > 0 and missing_details:
            details_label = tk.Label(
                main_frame,
                text="Détails des photos toujours manquantes :",
                font=("Arial", 10, "bold"),
                bg="white",
                fg=self.color_blue
            )
            details_label.pack(anchor="w", pady=(15, 5))
            
            # Zone de texte avec défilement pour les détails
            details_frame = tk.Frame(main_frame, bg="white")
            details_frame.pack(fill=tk.BOTH, expand=True, pady=5)
            
            details_text = scrolledtext.ScrolledText(
                details_frame,
                font=("Courier", 9),
                height=8,
                wrap=tk.WORD,
                bg="#f8fafc",
                relief=tk.FLAT
            )
            details_text.pack(fill=tk.BOTH, expand=True)
            
            for detail in missing_details[:20]:  # Limiter à 20 pour ne pas surcharger
                details_text.insert(tk.END, f"• {detail['name']} ({detail['class']}) - {detail['reason']}\n")
            
            if len(missing_details) > 20:
                details_text.insert(tk.END, f"\n... et {len(missing_details) - 20} autres\n")
            
            details_text.config(state=tk.DISABLED)
        
        # Message de conclusion
        if replaced_count > 0:
            conclusion_msg = "Les photos ont été remplacées avec succès dans CLASSE_JPG.\nVous pouvez maintenant générer le trombinoscope."
            conclusion_color = self.color_green
        else:
            conclusion_msg = "Aucune photo n'a pu être remplacée.\nVérifiez que le dossier Pronote contient des photos avec la bonne syntaxe (Nom-Prénom)."
            conclusion_color = "#dc2626"
        
        conclusion_label = tk.Label(
            main_frame,
            text=conclusion_msg,
            font=("Arial", 10),
            bg="white",
            fg=conclusion_color,
            justify=tk.CENTER
        )
        conclusion_label.pack(pady=15)
        
        # Frame pour les boutons
        buttons_frame = tk.Frame(main_frame, bg="white")
        buttons_frame.pack(pady=10)
        
        # Bouton Fermer - Style moderne
        close_container = tk.Frame(buttons_frame, bg="white")
        close_container.pack(side=tk.LEFT, padx=5)
        
        cancel_btn = tk.Button(
            close_container,
            text="✖ Fermer",
            command=popup.destroy,
            bg="#6b7280",
            fg="white",
            font=("Arial", 11, "bold"),
            cursor="hand2",
            relief=tk.FLAT,
            padx=25,
            pady=12,
            activebackground="#4b5563",
            borderwidth=0,
            highlightthickness=0
        )
        cancel_btn.pack()
        
        def close_on_enter(e):
            cancel_btn.config(bg="#4b5563")
        def close_on_leave(e):
            cancel_btn.config(bg="#6b7280")
        cancel_btn.bind("<Enter>", close_on_enter)
        cancel_btn.bind("<Leave>", close_on_leave)
        
        # Bouton Générer - Style moderne
        generate_container = tk.Frame(buttons_frame, bg="white")
        generate_container.pack(side=tk.LEFT, padx=5)
        
        generate_btn = tk.Button(
            generate_container,
            text="✨ Générer le trombinoscope",
            command=lambda: [popup.destroy(), self.generate_trombinoscope()],
            bg=self.color_green,
            fg="white",
            font=("Arial", 11, "bold"),
            cursor="hand2",
            relief=tk.FLAT,
            padx=25,
            pady=12,
            activebackground="#047857",
            borderwidth=0,
            highlightthickness=0
        )
        generate_btn.pack()
        
        def generate_on_enter(e):
            generate_btn.config(bg="#047857")
        def generate_on_leave(e):
            generate_btn.config(bg=self.color_green)
        generate_btn.bind("<Enter>", generate_on_enter)
        generate_btn.bind("<Leave>", generate_on_leave)
        
        self.update_status(f"Réparation terminée : {replaced_count} photo(s) remplacée(s)")
        
    def setup_ui(self):
        """Configuration de l'interface utilisateur"""
        
        # Style
        style = ttk.Style()
        style.theme_use('clam')
        
        # Configuration du fond
        self.root.configure(bg=self.color_bg)
        
        # Définir l'icône de l'application avec Psyduck
        try:
            psyduck_icon_path = os.path.join(os.path.dirname(__file__), "assets", "psyduck.png")
            if os.path.exists(psyduck_icon_path):
                icon_img = Image.open(psyduck_icon_path)
                icon_photo = ImageTk.PhotoImage(icon_img)
                self.root.iconphoto(True, icon_photo)
        except Exception as e:
            print(f"Erreur lors du chargement de l'icône: {e}")
        
        # En-tête
        header_frame = tk.Frame(self.root, bg=self.color_blue, height=80)
        header_frame.pack(fill=tk.X, padx=0, pady=0)
        header_frame.pack_propagate(False)
        
        # Conteneur centré pour le titre et le logo
        title_container = tk.Frame(header_frame, bg=self.color_blue)
        title_container.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        
        # Titre
        title_label = tk.Label(
            title_container,
            text="📚 Générateur de Trombinoscope",
            font=("Arial", 24, "bold"),
            bg=self.color_blue,
            fg="white"
        )
        title_label.pack(side=tk.LEFT, padx=(0, 10))
        
        # Logo Psyduck décoratif dans le header
        try:
            psyduck_path = os.path.join(os.path.dirname(__file__), "assets", "psyduck.png")
            psyduck_img = Image.open(psyduck_path)
            psyduck_img = psyduck_img.resize((50, 50), Image.Resampling.LANCZOS)
            self.psyduck_photo = ImageTk.PhotoImage(psyduck_img)
            
            psyduck_label = tk.Label(
                title_container,
                image=self.psyduck_photo,
                bg=self.color_blue
            )
            psyduck_label.pack(side=tk.LEFT)
        except Exception as e:
            print(f"Erreur chargement psyduck: {e}")
        
        # Frame principal
        main_frame = tk.Frame(self.root, bg=self.color_bg)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Section 1: Configuration
        config_frame = tk.LabelFrame(
            main_frame,
            text="📁 Configuration",
            font=("Arial", 13, "bold"),
            bg="white",
            fg=self.color_blue,
            padx=20,
            pady=20,
            relief=tk.FLAT,
            borderwidth=2,
            highlightthickness=1,
            highlightbackground="#e5e7eb"
        )
        config_frame.pack(fill=tk.X, pady=(0, 15))
        
        # Sélection du dossier
        tk.Label(
            config_frame,
            text="Dossier CLASSE_JPG :",
            font=("Arial", 10),
            bg="white"
        ).grid(row=0, column=0, sticky="w", pady=5)
        
        path_frame = tk.Frame(config_frame, bg="white")
        path_frame.grid(row=0, column=1, sticky="ew", padx=10)
        config_frame.columnconfigure(1, weight=1)
        
        tk.Entry(
            path_frame,
            textvariable=self.classe_jpg_path,
            font=("Arial", 10),
            width=50,
            relief=tk.FLAT,
            bg="#f8fafc",
            fg="#1e293b",
            insertbackground="#3b82f6"
        ).pack(side=tk.LEFT, fill=tk.X, expand=True, ipady=6)
        
        # Bouton Parcourir moderne
        browse_container = tk.Frame(path_frame, bg="white")
        browse_container.pack(side=tk.LEFT, padx=(10, 0))
        
        browse_btn = tk.Button(
            browse_container,
            text="📁 Parcourir",
            command=self.select_folder,
            bg=self.color_green,
            fg="white",
            font=("Arial", 10, "bold"),
            cursor="hand2",
            relief=tk.FLAT,
            padx=18,
            pady=8,
            activebackground="#047857",
            borderwidth=0,
            highlightthickness=0
        )
        browse_btn.pack()
        
        def browse_on_enter(e):
            browse_btn.config(bg="#047857")
        def browse_on_leave(e):
            browse_btn.config(bg=self.color_green)
        browse_btn.bind("<Enter>", browse_on_enter)
        browse_btn.bind("<Leave>", browse_on_leave)
        
        # Nom de l'établissement
        tk.Label(
            config_frame,
            text="Nom de l'établissement :",
            font=("Arial", 10),
            bg="white"
        ).grid(row=1, column=0, sticky="w", pady=5)
        
        tk.Entry(
            config_frame,
            textvariable=self.school_name,
            font=("Arial", 10),
            width=50,
            relief=tk.FLAT,
            bg="#f8fafc",
            fg="#1e293b",
            insertbackground="#3b82f6"
        ).grid(row=1, column=1, sticky="w", padx=10, ipady=6)
        
        # Année scolaire
        tk.Label(
            config_frame,
            text="Année scolaire :",
            font=("Arial", 10),
            bg="white"
        ).grid(row=2, column=0, sticky="w", pady=5)
        
        tk.Entry(
            config_frame,
            textvariable=self.school_year,
            font=("Arial", 10),
            width=50,
            relief=tk.FLAT,
            bg="#f8fafc",
            fg="#1e293b",
            insertbackground="#3b82f6"
        ).grid(row=2, column=1, sticky="w", padx=10, ipady=6)
        
        # Format de sortie
        tk.Label(
            config_frame,
            text="Format de sortie :",
            font=("Arial", 10),
            bg="white"
        ).grid(row=3, column=0, sticky="w", pady=5)
        
        format_frame = tk.Frame(config_frame, bg="white")
        format_frame.grid(row=3, column=1, sticky="w", padx=10)
        
        tk.Radiobutton(
            format_frame,
            text="Word (.docx)",
            variable=self.output_format,
            value="word",
            font=("Arial", 10),
            bg="white"
        ).pack(side=tk.LEFT, padx=(0, 20))
        
        tk.Radiobutton(
            format_frame,
            text="PDF (.pdf)",
            variable=self.output_format,
            value="pdf",
            font=("Arial", 10),
            bg="white"
        ).pack(side=tk.LEFT)
        
        # Section 2: Aperçu
        preview_frame = tk.LabelFrame(
            main_frame,
            text="📋 Aperçu des classes",
            font=("Arial", 13, "bold"),
            bg="white",
            fg=self.color_blue,
            padx=20,
            pady=20,
            relief=tk.FLAT,
            borderwidth=2,
            highlightthickness=1,
            highlightbackground="#e5e7eb"
        )
        preview_frame.pack(fill=tk.BOTH, expand=True, pady=(0, 15))
        
        # Zone de texte avec défilement
        self.preview_text = scrolledtext.ScrolledText(
            preview_frame,
            font=("Courier", 9),
            height=10,
            wrap=tk.WORD,
            bg="#f8fafc",
            relief=tk.FLAT
        )
        self.preview_text.pack(fill=tk.BOTH, expand=True)
        
        # Section 3: Actions
        action_frame = tk.Frame(main_frame, bg=self.color_bg)
        action_frame.pack(fill=tk.X)
        
        # Bouton Analyser - Style moderne
        analyze_container = tk.Frame(action_frame, bg=self.color_bg)
        analyze_container.pack(side=tk.LEFT, padx=(0, 10))
        
        analyze_btn = tk.Button(
            analyze_container,
            text="🔍 Analyser les classes",
            command=self.analyze_classes,
            bg=self.color_light_blue,
            fg="white",
            font=("Arial", 12, "bold"),
            cursor="hand2",
            relief=tk.FLAT,
            padx=30,
            pady=15,
            activebackground="#2563eb",
            borderwidth=0,
            highlightthickness=0
        )
        analyze_btn.pack()
        
        def analyze_on_enter(e):
            analyze_btn.config(bg="#2563eb")
        def analyze_on_leave(e):
            analyze_btn.config(bg=self.color_light_blue)
        analyze_btn.bind("<Enter>", analyze_on_enter)
        analyze_btn.bind("<Leave>", analyze_on_leave)
        
        # Bouton Générer - Style moderne
        generate_container = tk.Frame(action_frame, bg=self.color_bg)
        generate_container.pack(side=tk.LEFT)
        
        generate_btn = tk.Button(
            generate_container,
            text="✨ Générer le Trombinoscope",
            command=self.generate_trombinoscope,
            bg=self.color_green,
            fg="white",
            font=("Arial", 12, "bold"),
            cursor="hand2",
            relief=tk.FLAT,
            padx=30,
            pady=15,
            activebackground="#047857",
            borderwidth=0,
            highlightthickness=0
        )
        generate_btn.pack()
        
        def generate_on_enter(e):
            generate_btn.config(bg="#047857")
        def generate_on_leave(e):
            generate_btn.config(bg=self.color_green)
        generate_btn.bind("<Enter>", generate_on_enter)
        generate_btn.bind("<Leave>", generate_on_leave)
        
        # GIF Psyduck à côté du bouton (cliquable pour le mini-jeu Easter Egg)
        psyduck_gif_container = tk.Frame(action_frame, bg=self.color_bg)
        psyduck_gif_container.pack(side=tk.LEFT, padx=(20, 0))
        
        self.psyduck_gif_label = tk.Label(psyduck_gif_container, bg=self.color_bg, cursor="hand2")
        self.psyduck_gif_label.pack()
        
        # Charger le GIF animé
        try:
            self.psyduck_gif_path = os.path.join(os.path.dirname(__file__), "assets", "psyduck_loading.gif")
            if os.path.exists(self.psyduck_gif_path):
                self.psyduck_gif = Image.open(self.psyduck_gif_path)
                self.psyduck_gif_frames = []
                try:
                    while True:
                        frame = self.psyduck_gif.copy()
                        frame = frame.resize((160, 80), Image.Resampling.LANCZOS)
                        self.psyduck_gif_frames.append(ImageTk.PhotoImage(frame))
                        self.psyduck_gif.seek(self.psyduck_gif.tell() + 1)
                except EOFError:
                    pass  # Fin du GIF
                self.psyduck_gif_index = 0
                # Afficher le premier frame du GIF
                if len(self.psyduck_gif_frames) > 0:
                    self.psyduck_gif_label.config(image=self.psyduck_gif_frames[0])
                    # Démarrer l'animation
                    self.animate_psyduck_gif()
                # Rendre le GIF cliquable pour ouvrir le mini-jeu
                self.psyduck_gif_label.bind("<Button-1>", lambda e: self.show_whack_a_psyduck_game())
        except Exception as e:
            print(f"Erreur chargement GIF Psyduck: {e}")
        
        # Barre de progression (initialement cachée)
        self.progress_frame = tk.Frame(main_frame, bg=self.color_bg)
        
        # Container horizontal pour le texte et la barre
        progress_content = tk.Frame(self.progress_frame, bg=self.color_bg)
        progress_content.pack(pady=(10, 5))
        
        self.progress_label = tk.Label(
            progress_content,
            text="",
            font=("Arial", 10, "bold"),
            bg=self.color_bg,
            fg=self.color_blue
        )
        self.progress_label.pack(pady=(0, 8))
        
        # Style moderne pour la barre de progression
        style.configure(
            "Modern.Horizontal.TProgressbar",
            troughcolor='#e5e7eb',
            background='#059669',
            darkcolor='#047857',
            lightcolor='#10b981',
            bordercolor='#d1d5db',
            thickness=20
        )
        
        self.progress_bar = ttk.Progressbar(
            progress_content,
            length=450,
            mode='determinate',
            style="Modern.Horizontal.TProgressbar"
        )
        self.progress_bar.pack()
        
        # Barre de statut
        self.status_label = tk.Label(
            self.root,
            text="Prêt à générer votre trombinoscope",
            font=("Arial", 9),
            bg=self.color_blue,
            fg="white",
            anchor="w",
            padx=10
        )
        self.status_label.pack(fill=tk.X, side=tk.BOTTOM)
    
    def animate_psyduck_gif(self):
        """Animer le GIF Psyduck en continu"""
        if hasattr(self, 'psyduck_gif_frames') and len(self.psyduck_gif_frames) > 0:
            # Vérifier si le label existe toujours et est visible
            if self.psyduck_gif_label.winfo_exists():
                self.psyduck_gif_index = (self.psyduck_gif_index + 1) % len(self.psyduck_gif_frames)
                self.psyduck_gif_label.config(image=self.psyduck_gif_frames[self.psyduck_gif_index])
                # Répéter l'animation toutes les 100ms
                self.root.after(100, self.animate_psyduck_gif)
    
    def select_folder(self):
        """Sélection du dossier CLASSE_JPG"""
        folder = filedialog.askdirectory(title="Sélectionner le dossier CLASSE_JPG")
        if folder:
            self.classe_jpg_path.set(folder)
            self.update_status(f"Dossier sélectionné : {folder}")
            
    def update_status(self, message):
        """Mise à jour de la barre de statut"""
        self.status_label.config(text=message)
        self.root.update_idletasks()
        
    def update_progress(self, current, total, message=""):
        """Mise à jour de la barre de progression avec message aléatoire"""
        if total > 0:
            progress_percent = (current / total) * 100
            self.progress_bar['value'] = progress_percent
            
            # Sélectionner un message aléatoire à chaque mise à jour
            random_msg = random.choice(self.loading_messages)
            
            # Afficher le message de progression avec le message aléatoire
            display_text = f"{message} ({current}/{total})\n💡 {random_msg}"
            self.progress_label.config(text=display_text)
            
            self.root.update_idletasks()
        
    def sort_class_name(self, class_name):
        """Tri intelligent des noms de classes"""
        # Extraction du type et du numéro
        
        # Secondes (2DE)
        if class_name.startswith('2DE'):
            number = int(re.search(r'\d+', class_name).group())
            return (1, number, class_name)
        
        # Premières générales (PG)
        elif class_name.startswith('PG'):
            number = int(re.search(r'\d+', class_name).group())
            return (2, number, class_name)
        
        # Premières STMG (PSTMG)
        elif class_name.startswith('PSTMG'):
            number = int(re.search(r'\d+', class_name).group())
            return (3, number, class_name)
        
        # Terminales générales (TG)
        elif class_name.startswith('TG') and not class_name.startswith('TGF'):
            number = int(re.search(r'\d+', class_name).group())
            return (4, number, class_name)
        
        # Terminales spéciales (TM, TGF, TRHC, etc.)
        elif class_name.startswith('TM') or class_name.startswith('TGF') or class_name.startswith('TRHC'):
            match = re.search(r'\d+', class_name)
            number = int(match.group()) if match else 0
            return (5, number, class_name)
        
        # BTS
        elif class_name.startswith('BTS'):
            # Extraction du type de BTS et du numéro
            bts_match = re.search(r'BTS\s*([A-Z]+)(\d+)', class_name)
            if bts_match:
                bts_type = bts_match.group(1)
                number = int(bts_match.group(2))
                return (6, ord(bts_type[0]), number, class_name)
            return (6, 0, 0, class_name)
        
        # Autres
        else:
            return (99, 0, class_name)
    
    def analyze_classes(self):
        """Analyse les classes dans le dossier sélectionné"""
        folder_path = self.classe_jpg_path.get()
        
        if not folder_path or not os.path.exists(folder_path):
            messagebox.showerror("Erreur", "Veuillez sélectionner un dossier valide.")
            return
        
        self.update_status("Analyse en cours...")
        self.preview_text.delete(1.0, tk.END)
        self.classes_data = {}
        
        try:
            # Parcours des sous-dossiers
            subdirs = [d for d in os.listdir(folder_path) 
                      if os.path.isdir(os.path.join(folder_path, d))]
            
            if not subdirs:
                messagebox.showwarning(
                    "Attention",
                    "Aucun sous-dossier de classe trouvé dans le dossier sélectionné."
                )
                return
            
            # Tri des classes
            subdirs.sort(key=self.sort_class_name)
            
            total_students = 0
            missing_photos_count = 0  # Compteur pour les photos manquantes (21ko)
            
            for class_name in subdirs:
                class_path = os.path.join(folder_path, class_name)
                
                # Recherche des fichiers JPG
                students = []
                for file in os.listdir(class_path):
                    if file.lower().endswith(('.jpg', '.jpeg', '.png')):
                        file_path = os.path.join(class_path, file)
                        # Vérifier la taille du fichier pour détecter les photos "inconnu" d'environ 21ko
                        file_size = os.path.getsize(file_path)
                        # Tolérance de ±500 bytes autour de 21ko pour détecter les photos "inconnu"
                        if 21000 <= file_size <= 22000:  # Entre 20.5ko et 21.5ko
                            missing_photos_count += 1
                        
                        # Extraction du nom (NOM-Prenom)
                        name = os.path.splitext(file)[0]
                        students.append({
                            'name': name,
                            'file_path': file_path
                        })
                
                # Tri alphabétique des élèves
                students.sort(key=lambda x: x['name'])
                
                if students:
                    self.classes_data[class_name] = students
                    total_students += len(students)
                    
                    # Affichage dans la prévisualisation
                    self.preview_text.insert(
                        tk.END,
                        f"📌 {class_name} ({len(students)} élèves)\n",
                        "class_header"
                    )
                    
                    for student in students[:5]:  # Afficher les 5 premiers
                        parts = student['name'].split('-')
                        if len(parts) == 2:
                            prenom = parts[1].capitalize()
                            nom = parts[0].upper()
                            self.preview_text.insert(tk.END, f"   • {prenom} {nom}\n")
                        else:
                            self.preview_text.insert(tk.END, f"   • {student['name']}\n")
                    
                    if len(students) > 5:
                        self.preview_text.insert(tk.END, f"   ... et {len(students) - 5} autres\n")
                    
                    self.preview_text.insert(tk.END, "\n")
            
            # Configuration des tags pour le texte
            self.preview_text.tag_config("class_header", foreground=self.color_blue, font=("Courier", 9, "bold"))
            
            # Résumé
            summary = f"\n{'='*60}\n"
            summary += f"✅ Total : {len(self.classes_data)} classes, {total_students} élèves\n"
            summary += f"{'='*60}\n"
            self.preview_text.insert(tk.END, summary, "summary")
            self.preview_text.tag_config("summary", foreground=self.color_green, font=("Courier", 9, "bold"))
            
            self.update_status(f"Analyse terminée : {len(self.classes_data)} classes trouvées")
            
            # Afficher l'alerte si des photos manquantes ont été détectées
            if missing_photos_count > 0:
                self.show_missing_photos_alert(missing_photos_count)
            
        except Exception as e:
            messagebox.showerror("Erreur", f"Erreur lors de l'analyse :\n{str(e)}")
            self.update_status("Erreur lors de l'analyse")
    
    def generate_trombinoscope(self):
        """Génération du trombinoscope"""
        if not self.classes_data:
            messagebox.showwarning(
                "Attention",
                "Veuillez d'abord analyser les classes (bouton 'Analyser les classes')."
            )
            return
        
        # Cacher le GIF Psyduck lors du clic
        if hasattr(self, 'psyduck_gif_label'):
            self.psyduck_gif_label.pack_forget()
        
        # Demander où enregistrer le fichier
        output_format = self.output_format.get()
        file_extension = ".docx" if output_format == "word" else ".pdf"
        default_name = f"Trombinoscope_{self.school_year.get().replace('-', '_')}{file_extension}"
        
        output_file = filedialog.asksaveasfilename(
            defaultextension=file_extension,
            filetypes=[("Word Document", "*.docx"), ("PDF", "*.pdf")] if output_format == "word" else [("PDF", "*.pdf")],
            initialfile=default_name
        )
        
        if not output_file:
            # Réafficher le GIF si l'utilisateur annule
            if hasattr(self, 'psyduck_gif_label'):
                self.psyduck_gif_label.pack()
            return
        
        # Afficher la barre de progression
        self.progress_frame.pack(fill=tk.X, pady=(10, 0))
        self.progress_bar['value'] = 0
        
        self.update_status("Génération du trombinoscope en cours...")
        
        try:
            # Génération du document Word
            temp_docx = output_file if output_format == "word" else output_file.replace('.pdf', '_temp.docx')
            self.create_word_document(temp_docx)
            
            # Conversion en PDF si nécessaire
            if output_format == "pdf":
                self.update_progress(len(self.classes_data), len(self.classes_data) + 1, "Conversion en PDF")
                self.convert_to_pdf(temp_docx, output_file)
                os.remove(temp_docx)  # Suppression du fichier temporaire
            
            # Cacher la barre de progression
            self.progress_frame.pack_forget()
            
            # Réafficher le GIF après la génération
            if hasattr(self, 'psyduck_gif_label'):
                self.psyduck_gif_label.pack()
            
            self.update_status(f"✅ Trombinoscope généré avec succès : {output_file}")
            messagebox.showinfo(
                "Succès",
                f"Le trombinoscope a été généré avec succès !\n\nFichier : {output_file}"
            )
            
            # Ouvrir le dossier contenant le fichier
            if messagebox.askyesno("Ouvrir", "Voulez-vous ouvrir le dossier contenant le fichier ?"):
                os.startfile(os.path.dirname(output_file))
                
        except Exception as e:
            self.progress_frame.pack_forget()
            # Réafficher le GIF en cas d'erreur
            if hasattr(self, 'psyduck_gif_label'):
                self.psyduck_gif_label.pack()
            messagebox.showerror("Erreur", f"Erreur lors de la génération :\n{str(e)}")
            self.update_status("Erreur lors de la génération")
            import traceback
            traceback.print_exc()
    
    def create_word_document(self, output_file):
        """Création du document Word"""
        # Charger le document template comme base (pour conserver l'image de couverture)
        docx_path = os.path.join(os.path.dirname(__file__), "assets", "001 TROMBI COUV RECTO .docx")
        
        if os.path.exists(docx_path):
            # Utiliser le template comme base du document
            doc = Document(docx_path)
            self.update_progress(0, len(self.classes_data) + 1, "Chargement de la page de couverture")
            
            # Remplacer l'année scolaire dans la couverture
            for paragraph in doc.paragraphs:
                for run in paragraph.runs:
                    # Remplacer différents formats d'année possibles
                    for old_year in ["2024-2025", "2024/2025", "2021-2022", "2020-2030"]:
                        if old_year in run.text:
                            run.text = run.text.replace(old_year, self.school_year.get())
        else:
            # Si le template n'existe pas, créer un document vide et ajouter une couverture par défaut
            doc = Document()
            self.add_cover_page(doc)
        
        # Configuration de la page en paysage avec marges de 1.5cm en haut et bas
        # Appliquer APRÈS le chargement du template pour ne pas écraser la première section
        for section in doc.sections:
            section.page_width = Inches(11.69)  # A4 paysage
            section.page_height = Inches(8.27)
            section.top_margin = Cm(1.5)  # Marges de 1.5cm en haut
            section.bottom_margin = Cm(1.5)  # Marges de 1.5cm en bas
            section.left_margin = Cm(0.7)
            section.right_margin = Cm(0.7)
        
        total_steps = len(self.classes_data) + 1
        current_step = 1
        
        # Pages des classes
        for idx, (class_name, students) in enumerate(self.classes_data.items()):
            self.update_progress(current_step, total_steps, f"Génération de la classe {class_name}")
            # Ne pas ajouter de page_break pour la première classe (idx == 0)
            # pour éviter une page blanche après la couverture
            if idx > 0:
                doc.add_page_break()
            self.add_class_page(doc, class_name, students)
            current_step += 1
        
        # Sauvegarde
        self.update_progress(total_steps, total_steps, "Sauvegarde du document")
        doc.save(output_file)
    
    def add_cover_page(self, doc):
        """Ajout de la page de couverture par défaut"""
        # En-tête
        header = doc.add_paragraph()
        header.alignment = WD_ALIGN_PARAGRAPH.CENTER
        
        run = header.add_run(self.school_name.get())
        run.font.size = Pt(32)
        run.font.bold = True
        run.font.color.rgb = RGBColor(30, 58, 138)  # Bleu foncé
        
        # Année scolaire
        year_para = doc.add_paragraph()
        year_para.alignment = WD_ALIGN_PARAGRAPH.CENTER
        run = year_para.add_run(f"\nAnnée Scolaire {self.school_year.get()}")
        run.font.size = Pt(24)
        run.font.color.rgb = RGBColor(5, 150, 105)  # Vert
        
        # Titre principal
        doc.add_paragraph("\n" * 3)
        title = doc.add_paragraph()
        title.alignment = WD_ALIGN_PARAGRAPH.CENTER
        run = title.add_run("TROMBINOSCOPE")
        run.font.size = Pt(48)
        run.font.bold = True
        run.font.color.rgb = RGBColor(30, 58, 138)
        
        # Informations supplémentaires
        doc.add_paragraph("\n" * 5)
        info = doc.add_paragraph()
        info.alignment = WD_ALIGN_PARAGRAPH.CENTER
        run = info.add_run(f"{len(self.classes_data)} Classes")
        run.font.size = Pt(18)
        
        total_students = sum(len(students) for students in self.classes_data.values())
        info2 = doc.add_paragraph()
        info2.alignment = WD_ALIGN_PARAGRAPH.CENTER
        run = info2.add_run(f"{total_students} Élèves")
        run.font.size = Pt(18)
    
    def add_class_page(self, doc, class_name, students):
        """Ajout d'une page de classe avec disposition 5 rangées × 9 colonnes (optimisé pour 40 élèves, max 45)"""
        
        # En-tête de la page avec le nom de la classe - ESPACEMENT MINIMAL
        class_header = doc.add_paragraph()
        class_header.alignment = WD_ALIGN_PARAGRAPH.CENTER
        class_header.paragraph_format.space_before = Pt(0)
        class_header.paragraph_format.space_after = Pt(2)  # Espacement minimal après le titre
        
        run = class_header.add_run(f"Classe {class_name}")
        run.font.size = Pt(16)  # Titre légèrement réduit pour gagner de l'espace
        run.font.bold = True
        run.font.color.rgb = RGBColor(30, 58, 138)
        
        # Configuration de la grille: 5 rangées × 9 colonnes = 45 élèves max (optimisé pour 40)
        rows = 5
        cols = 9
        
        # Taille des photos optimisée pour 9 colonnes avec photos plus grandes
        photo_width = Cm(1.9)  # Augmenté à 1.9cm pour des photos plus grandes
        
        # Création du tableau avec toutes les lignes
        table = doc.add_table(rows=rows, cols=cols)
        table.alignment = WD_ALIGN_PARAGRAPH.CENTER
        
        # Configuration des marges du tableau pour maximiser l'espace
        for row in table.rows:
            for cell in row.cells:
                # Réduire les marges des cellules au MINIMUM
                tc = cell._element
                tcPr = tc.get_or_add_tcPr()
                tcMar = OxmlElement('w:tcMar')
                for margin_name in ['top', 'left', 'bottom', 'right']:
                    node = OxmlElement(f'w:{margin_name}')
                    node.set(qn('w:w'), '30')  # Marges augmentées à 30 pour 9 colonnes avec photos plus grandes
                    node.set(qn('w:type'), 'dxa')
                    tcMar.append(node)
                tcPr.append(tcMar)
        
        # Remplissage du tableau - FORCER à remplir TOUTES les lignes
        for row_idx in range(rows):
            for col_idx in range(cols):
                idx = row_idx * cols + col_idx
                
                if idx < len(students):
                    student = students[idx]
                    cell = table.rows[row_idx].cells[col_idx]
                    cell.vertical_alignment = WD_ALIGN_PARAGRAPH.CENTER
                    
                    # Ajout de la photo
                    try:
                        paragraph = cell.paragraphs[0]
                        paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER
                        
                        # Réduire l'espacement du paragraphe
                        paragraph.paragraph_format.space_before = Pt(0)
                        paragraph.paragraph_format.space_after = Pt(0)
                        
                        run = paragraph.add_run()
                        run.add_picture(student['file_path'], width=photo_width)
                        
                        # Ajout du nom
                        name_parts = student['name'].split('-')
                        if len(name_parts) == 2:
                            prenom = name_parts[1].capitalize()
                            nom = name_parts[0].upper()
                            display_name = f"{prenom}\n{nom}"
                        else:
                            display_name = student['name']
                        
                        name_para = cell.add_paragraph()
                        name_para.alignment = WD_ALIGN_PARAGRAPH.CENTER
                        name_para.paragraph_format.space_before = Pt(0)
                        name_para.paragraph_format.space_after = Pt(0)
                        
                        run = name_para.add_run(display_name)
                        run.font.size = Pt(7)  # Augmenté à 7pt pour meilleure lisibilité avec photos plus grandes
                        run.font.bold = True
                        
                    except Exception as e:
                        # En cas d'erreur, afficher juste le nom
                        paragraph = cell.paragraphs[0]
                        paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER
                        run = paragraph.add_run(f"[Photo manquante]\n{student['name']}")
                        run.font.size = Pt(7)
        
        # Si la classe a plus de 45 élèves, afficher un avertissement
        if len(students) > rows * cols:
            doc.add_paragraph()
            warning = doc.add_paragraph()
            warning.alignment = WD_ALIGN_PARAGRAPH.CENTER
            run = warning.add_run(f"⚠ {len(students) - (rows * cols)} élèves supplémentaires non affichés (limite: {rows * cols} élèves/page)")
            run.font.size = Pt(9)
            run.font.color.rgb = RGBColor(220, 38, 38)  # Rouge
    
    def convert_to_pdf(self, docx_file, pdf_file):
        """Conversion du document Word en PDF"""
        try:
            from docx2pdf import convert
            convert(docx_file, pdf_file)
        except ImportError:
            messagebox.showwarning(
                "Attention",
                "La conversion en PDF nécessite l'installation de 'docx2pdf'.\n"
                "Le fichier Word a été généré à la place."
            )
            # Renommer le fichier .docx en gardant le nom demandé
            new_name = pdf_file.replace('.pdf', '.docx')
            shutil.move(docx_file, new_name)
        except Exception as e:
            messagebox.showerror(
                "Erreur de conversion",
                f"Impossible de convertir en PDF.\n{str(e)}\n\n"
                "Le fichier Word a été conservé."
            )


def main():
    """Point d'entrée de l'application"""
    root = tk.Tk()
    app = TrombinoscopeApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
