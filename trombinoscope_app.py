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
            "Marc Andral est un CONNARD :-) . Pardon, un GROS CONNARD !"
        ]
        
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
        
    def create_menu(self):
        """Création du menu avec l'onglet À propos"""
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)
        
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
        
    def show_easter_egg(self):
        """Afficher un message Easter Egg aléatoire"""
        message = random.choice(self.easter_messages)
        
        # Créer une fenêtre popup
        popup = tk.Toplevel(self.root)
        popup.title("🦆 Psyduck vous parle...")
        popup.geometry("450x200")
        popup.configure(bg="white")
        popup.resizable(False, False)
        
        # Centrer la fenêtre
        popup.transient(self.root)
        popup.grab_set()
        
        # Frame principale
        frame = tk.Frame(popup, bg="white", padx=20, pady=20)
        frame.pack(fill=tk.BOTH, expand=True)
        
        # Message
        msg_label = tk.Label(
            frame,
            text=message,
            font=("Arial", 11),
            bg="white",
            wraplength=400,
            justify=tk.LEFT
        )
        msg_label.pack(pady=20)
        
        # Bouton fermer
        close_btn = tk.Button(
            frame,
            text="Fermer",
            command=popup.destroy,
            bg=self.color_blue,
            fg="white",
            font=("Arial", 10, "bold"),
            cursor="hand2",
            relief=tk.FLAT,
            padx=20,
            pady=5
        )
        close_btn.pack()
        
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
        
        # Logo Psyduck cliquable (Easter Egg)
        try:
            psyduck_path = os.path.join(os.path.dirname(__file__), "assets", "psyduck.png")
            psyduck_img = Image.open(psyduck_path)
            psyduck_img = psyduck_img.resize((50, 50), Image.Resampling.LANCZOS)
            self.psyduck_photo = ImageTk.PhotoImage(psyduck_img)
            
            psyduck_label = tk.Label(
                title_container,
                image=self.psyduck_photo,
                bg=self.color_blue,
                cursor="hand2"
            )
            psyduck_label.pack(side=tk.LEFT)
            psyduck_label.bind("<Button-1>", lambda e: self.show_easter_egg())
        except Exception as e:
            print(f"Erreur chargement psyduck: {e}")
        
        # Frame principal
        main_frame = tk.Frame(self.root, bg=self.color_bg)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Section 1: Configuration
        config_frame = tk.LabelFrame(
            main_frame,
            text="📁 Configuration",
            font=("Arial", 12, "bold"),
            bg="white",
            fg=self.color_blue,
            padx=15,
            pady=15
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
            width=50
        ).pack(side=tk.LEFT, fill=tk.X, expand=True)
        
        tk.Button(
            path_frame,
            text="Parcourir",
            command=self.select_folder,
            bg=self.color_green,
            fg="white",
            font=("Arial", 9, "bold"),
            cursor="hand2",
            relief=tk.FLAT,
            padx=15
        ).pack(side=tk.LEFT, padx=(10, 0))
        
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
            width=50
        ).grid(row=1, column=1, sticky="w", padx=10)
        
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
            width=50
        ).grid(row=2, column=1, sticky="w", padx=10)
        
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
            font=("Arial", 12, "bold"),
            bg="white",
            fg=self.color_blue,
            padx=15,
            pady=15
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
        
        # Bouton Analyser
        tk.Button(
            action_frame,
            text="🔍 Analyser les classes",
            command=self.analyze_classes,
            bg=self.color_light_blue,
            fg="white",
            font=("Arial", 11, "bold"),
            cursor="hand2",
            relief=tk.FLAT,
            padx=20,
            pady=10
        ).pack(side=tk.LEFT, padx=(0, 10))
        
        # Bouton Générer
        tk.Button(
            action_frame,
            text="✨ Générer le Trombinoscope",
            command=self.generate_trombinoscope,
            bg=self.color_green,
            fg="white",
            font=("Arial", 11, "bold"),
            cursor="hand2",
            relief=tk.FLAT,
            padx=20,
            pady=10
        ).pack(side=tk.LEFT)
        
        # Barre de progression (initialement cachée)
        self.progress_frame = tk.Frame(main_frame, bg=self.color_bg)
        self.progress_label = tk.Label(
            self.progress_frame,
            text="",
            font=("Arial", 9),
            bg=self.color_bg
        )
        self.progress_label.pack(pady=(10, 5))
        
        self.progress_bar = ttk.Progressbar(
            self.progress_frame,
            length=400,
            mode='determinate'
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
            
            for class_name in subdirs:
                class_path = os.path.join(folder_path, class_name)
                
                # Recherche des fichiers JPG
                students = []
                for file in os.listdir(class_path):
                    if file.lower().endswith(('.jpg', '.jpeg', '.png')):
                        # Extraction du nom (NOM-Prenom)
                        name = os.path.splitext(file)[0]
                        students.append({
                            'name': name,
                            'file_path': os.path.join(class_path, file)
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
            messagebox.showerror("Erreur", f"Erreur lors de la génération :\n{str(e)}")
            self.update_status("Erreur lors de la génération")
            import traceback
            traceback.print_exc()
    
    def create_word_document(self, output_file):
        """Création du document Word"""
        doc = Document()
        
        # Configuration de la page en paysage avec marges TRÈS réduites
        for section in doc.sections:
            section.page_width = Inches(11.69)  # A4 paysage
            section.page_height = Inches(8.27)
            section.top_margin = Cm(0.5)  # Marges minimales
            section.bottom_margin = Cm(0.5)
            section.left_margin = Cm(0.7)
            section.right_margin = Cm(0.7)
        
        total_steps = len(self.classes_data) + 1
        current_step = 0
        
        # Page de couverture depuis le fichier ODT
        self.update_progress(current_step, total_steps, "Ajout de la page de couverture")
        self.add_cover_page_from_odt(doc)
        current_step += 1
        
        # Pages des classes
        for idx, (class_name, students) in enumerate(self.classes_data.items()):
            self.update_progress(current_step, total_steps, f"Génération de la classe {class_name}")
            doc.add_page_break()
            self.add_class_page(doc, class_name, students)
            current_step += 1
        
        # Sauvegarde
        self.update_progress(total_steps, total_steps, "Sauvegarde du document")
        doc.save(output_file)
    
    def add_cover_page_from_odt(self, doc):
        """Ajout de la page de couverture depuis le fichier DOCX"""
        try:
            # Chemin vers le fichier DOCX (avec espaces dans le nom)
            docx_path = os.path.join(os.path.dirname(__file__), "assets", "001 TROMBI COUV RECTO .docx")
            
            if os.path.exists(docx_path):
                # Charger le document de couverture existant
                cover_doc = Document(docx_path)
                
                # Copier tous les éléments du document de couverture
                for element in cover_doc.element.body:
                    doc.element.body.append(element)
                
                # Remplacer l'année scolaire si elle apparaît dans le texte
                # Parcourir tous les paragraphes et remplacer "2024-2025" par l'année actuelle
                for paragraph in doc.paragraphs:
                    for run in paragraph.runs:
                        if "2024-2025" in run.text:
                            run.text = run.text.replace("2024-2025", self.school_year.get())
                        # Aussi vérifier d'autres formats possibles
                        if "2024/2025" in run.text:
                            run.text = run.text.replace("2024/2025", self.school_year.get())
                
            else:
                # Si le fichier DOCX n'existe pas, utiliser la page de couverture par défaut
                print(f"Fichier de couverture non trouvé : {docx_path}")
                self.add_cover_page(doc)
                
        except Exception as e:
            print(f"Erreur lors de l'ajout de la couverture DOCX: {e}")
            import traceback
            traceback.print_exc()
            # Fallback vers la page de couverture par défaut
            self.add_cover_page(doc)
    
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
        """Ajout d'une page de classe avec disposition 5 rangées × 10 colonnes"""
        
        # En-tête de la page avec le nom de la classe - ESPACEMENT MINIMAL
        class_header = doc.add_paragraph()
        class_header.alignment = WD_ALIGN_PARAGRAPH.CENTER
        class_header.paragraph_format.space_before = Pt(0)
        class_header.paragraph_format.space_after = Pt(2)  # Espacement minimal après le titre
        
        run = class_header.add_run(f"Classe {class_name}")
        run.font.size = Pt(16)  # Titre légèrement réduit pour gagner de l'espace
        run.font.bold = True
        run.font.color.rgb = RGBColor(30, 58, 138)
        
        # Configuration de la grille: 5 rangées × 10 colonnes = 50 élèves max
        rows = 5
        cols = 10
        
        # Taille des photos optimisée pour 10 colonnes
        photo_width = Cm(1.6)  # Réduit à 1.6cm pour permettre 10 colonnes
        
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
                    node.set(qn('w:w'), '20')  # Marges minimales réduites à 20 pour 10 colonnes
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
                        run.font.size = Pt(6)  # Réduit à 6pt
                        run.font.bold = True
                        
                    except Exception as e:
                        # En cas d'erreur, afficher juste le nom
                        paragraph = cell.paragraphs[0]
                        paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER
                        run = paragraph.add_run(f"[Photo manquante]\n{student['name']}")
                        run.font.size = Pt(6)
        
        # Si la classe a plus de 50 élèves, afficher un avertissement
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
