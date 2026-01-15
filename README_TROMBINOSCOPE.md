# 📚 Générateur de Trombinoscope - Guide d'Installation et d'Utilisation

## 🎯 Description

Application desktop pour générer automatiquement des trombinoscopes au format Word ou PDF à partir de photos d'élèves organisées par classe.

## 📋 Fonctionnalités

✅ Interface graphique intuitive avec couleurs institutionnelles (bleu/vert)  
✅ Sélection facile du dossier contenant les photos  
✅ Tri automatique des classes (2DE, PG, PSTMG, TG, TM, BTS, etc.)  
✅ Génération dynamique : jusqu'à 36 élèves par page  
✅ Format de page paysage  
✅ Export Word (.docx) et PDF (.pdf)  
✅ Prévisualisation des classes avant génération  
✅ Page de couverture personnalisable  

---

## 🚀 Installation

### Prérequis

- **Python 3.8 ou supérieur**
- **Windows 10/11** (pour la conversion PDF et la création d'exécutable)

### Étape 1 : Installer Python

1. Téléchargez Python depuis [python.org](https://www.python.org/downloads/)
2. **Important** : Cochez "Add Python to PATH" lors de l'installation

### Étape 2 : Installer les dépendances

Ouvrez un terminal (CMD ou PowerShell) dans le dossier contenant les fichiers et exécutez :

```bash
pip install -r requirements_trombinoscope.txt
```

---

## 🎮 Utilisation

### Option 1 : Lancer l'application Python

```bash
python trombinoscope_app.py
```

### Option 2 : Créer un exécutable (.exe)

#### Installation de PyInstaller

```bash
pip install pyinstaller
```

#### Création de l'exécutable

```bash
pyinstaller --onefile --windowed --name="Trombinoscope" --icon=icon.ico trombinoscope_app.py
```

L'exécutable sera créé dans le dossier `dist/`

**Note** : Pour inclure une icône personnalisée, placez un fichier `icon.ico` dans le même dossier avant la conversion.

#### Création avec tous les assets

Pour inclure le fichier de couverture :

```bash
pyinstaller --onefile --windowed --name="Trombinoscope" --add-data="assets;assets" trombinoscope_app.py
```

---

## 📖 Mode d'emploi

### 1️⃣ Structure des dossiers

Organisez vos photos comme suit :

```
CLASSE_JPG/
├── 2DE01/
│   ├── ALFRANCA-Eva.jpg
│   ├── ANDRADE-Tiana.jpg
│   └── ... (autres élèves)
├── 2DE02/
│   └── ... (photos des élèves)
├── PG01/
├── PSTMG1/
├── TG01/
└── BTS CJN1/
```

**Format des noms de fichiers** : `NOM-Prenom.jpg` (exemple : `DUPONT-Marie.jpg`)

### 2️⃣ Lancer l'application

1. Ouvrez l'application
2. Cliquez sur **"Parcourir"** pour sélectionner le dossier `CLASSE_JPG`
3. Vérifiez/modifiez le nom de l'établissement et l'année scolaire
4. Cliquez sur **"🔍 Analyser les classes"**

### 3️⃣ Prévisualisation

L'application affiche :
- Liste de toutes les classes trouvées
- Nombre d'élèves par classe
- Aperçu des premiers noms

### 4️⃣ Génération

1. Choisissez le format : **Word (.docx)** ou **PDF (.pdf)**
2. Cliquez sur **"✨ Générer le Trombinoscope"**
3. Choisissez l'emplacement et le nom du fichier
4. Attendez la fin de la génération

---

## 🎨 Personnalisation

### Modifier les couleurs

Dans le fichier `trombinoscope_app.py`, modifiez les variables :

```python
self.color_blue = "#1e3a8a"      # Bleu foncé
self.color_green = "#059669"      # Vert
self.color_light_blue = "#3b82f6" # Bleu clair
self.color_bg = "#f0f9ff"         # Fond
```

### Modifier la mise en page

Pour changer le nombre de photos par page, modifiez la section `add_class_page` :

```python
if num_students <= 28:
    rows = 4  # Nombre de lignes
    cols = 7  # Nombre de colonnes
```

---

## 🔧 Résolution de problèmes

### La conversion PDF ne fonctionne pas

**Solution** : Installez Microsoft Word ou utilisez l'export Word uniquement.

Alternative sans Word :

```bash
pip uninstall docx2pdf
pip install pypandoc
```

### Photos ne s'affichent pas

**Vérifications** :
- Format des fichiers : `.jpg`, `.jpeg` ou `.png`
- Noms de fichiers : `NOM-Prenom.extension`
- Pas d'espaces ou caractères spéciaux dans les noms de dossiers

### L'application ne se lance pas

```bash
# Vérifier l'installation de Python
python --version

# Réinstaller les dépendances
pip install --upgrade -r requirements_trombinoscope.txt
```

---

## 📝 Ordre de tri des classes

L'application trie automatiquement les classes dans l'ordre suivant :

1. **Secondes** : 2DE01, 2DE02, ..., 2DE15
2. **Premières générales** : PG01, PG02, ..., PG15
3. **Premières STMG** : PSTMG1, PSTMG2, ..., PSTMG5
4. **Terminales générales** : TG01, TG02, ..., TG10
5. **Terminales spéciales** : TM1, TM2, TGF, TRHC
6. **BTS** : BTS CJN1, BTS CJN2, BTS MCO1, BTS MCO2, ...

---

## 🆘 Support

Pour toute question ou problème :
- Vérifiez que tous les fichiers sont au bon format
- Consultez les messages d'erreur dans l'application
- Assurez-vous que Python et les dépendances sont correctement installés

---

## 📄 Licence

Application développée pour le Lycée Toulouse Lautrec  
Version 1.0 - 2025

---

## 🎯 Checklist avant génération

- [ ] Dossier CLASSE_JPG correctement organisé
- [ ] Photos nommées au format NOM-Prenom.jpg
- [ ] Python et dépendances installés
- [ ] Nom de l'établissement et année scolaire vérifiés
- [ ] Format de sortie sélectionné (Word ou PDF)
- [ ] Analyse effectuée avec succès

**Bonne génération de trombinoscope ! 📸**
