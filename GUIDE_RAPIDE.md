# 🚀 GUIDE DE DÉMARRAGE RAPIDE

## Pour utiliser l'application immédiatement sur Windows

### Option 1 : Exécution directe (recommandé pour les tests)

1. **Téléchargez tous les fichiers** dans un dossier sur votre ordinateur
2. **Double-cliquez sur** `build_exe.bat` pour créer l'exécutable
3. **L'exécutable sera dans** le dossier `dist/`
4. **Double-cliquez sur** `Trombinoscope_Generator.exe`

### Option 2 : Exécution avec Python

1. **Ouvrez un terminal** (CMD) dans le dossier
2. Exécutez :
   ```
   pip install -r requirements_trombinoscope.txt
   python trombinoscope_app.py
   ```

---

## 📋 Fichiers fournis

| Fichier | Description |
|---------|-------------|
| `trombinoscope_app.py` | Application principale avec interface graphique |
| `test_trombinoscope.py` | Script de test en ligne de commande |
| `requirements_trombinoscope.txt` | Dépendances Python nécessaires |
| `build_exe.bat` | Script pour créer l'exécutable Windows |
| `README_TROMBINOSCOPE.md` | Documentation complète |
| `assets/` | Dossier contenant la page de couverture |
| `sample_data/` | Exemples de données pour tester |

---

## 🎯 Utilisation rapide

### 1. Préparez vos données

Organisez vos photos dans des dossiers :

```
CLASSE_JPG/
├── 2DE01/
│   ├── DUPONT-Marie.jpg
│   ├── MARTIN-Pierre.jpg
│   └── ...
├── 2DE02/
├── PG01/
└── BTS MCO1/
```

**Important** : Les noms de fichiers doivent être au format `NOM-Prenom.jpg`

### 2. Lancez l'application

- Double-cliquez sur l'exécutable `.exe`
- OU exécutez `python trombinoscope_app.py`

### 3. Configurez

1. Cliquez sur "Parcourir" et sélectionnez votre dossier `CLASSE_JPG`
2. Vérifiez le nom de l'établissement et l'année
3. Cliquez sur "🔍 Analyser les classes"

### 4. Générez

1. Choisissez le format (Word ou PDF)
2. Cliquez sur "✨ Générer le Trombinoscope"
3. Choisissez où sauvegarder le fichier
4. C'est terminé ! 🎉

---

## ⚡ Commandes rapides

### Tester l'application (sans interface graphique)

```bash
python test_trombinoscope.py
```

### Créer l'exécutable

```bash
build_exe.bat
```

ou manuellement :

```bash
pip install pyinstaller
pyinstaller --onefile --windowed --name="Trombinoscope" trombinoscope_app.py
```

### Installer les dépendances

```bash
pip install -r requirements_trombinoscope.txt
```

---

## 🎨 Caractéristiques

✅ **Interface intuitive** avec couleurs institutionnelles  
✅ **Tri automatique** des classes par niveau  
✅ **Grille adaptative** : jusqu'à 36 élèves par page  
✅ **Export multiple** : Word et PDF  
✅ **Prévisualisation** avant génération  
✅ **Page de couverture** personnalisée  

---

## 📞 En cas de problème

### "Python n'est pas reconnu"
➡️ Installez Python depuis [python.org](https://www.python.org/downloads/)  
➡️ Cochez "Add Python to PATH" lors de l'installation

### "Module PIL/docx not found"
➡️ Exécutez : `pip install -r requirements_trombinoscope.txt`

### La conversion PDF ne fonctionne pas
➡️ Utilisez le format Word (.docx)  
➡️ Vous pouvez ensuite convertir en PDF avec Word

---

## 🎓 Exemples de résultats

L'application génère un document avec :

1. **Page de couverture** avec le nom de l'établissement et l'année
2. **Une page par classe** contenant :
   - En-tête : Établissement • Année • Nom de la classe
   - Photos des élèves en grille
   - Prénom et NOM sous chaque photo

---

## 💡 Astuces

- 📸 **Qualité des photos** : Utilisez des JPG de bonne qualité (mais pas trop lourds)
- 📝 **Nommage** : Respectez le format `NOM-Prenom.jpg` exactement
- 🗂️ **Organisation** : Un dossier par classe, tous dans `CLASSE_JPG`
- ⚡ **Performance** : L'analyse est rapide même avec 50+ classes

---

## ✨ Mise à jour

Pour mettre à jour l'application :
1. Remplacez `trombinoscope_app.py` par la nouvelle version
2. Recréez l'exécutable avec `build_exe.bat`

---

**Bonne utilisation ! 📚✨**
