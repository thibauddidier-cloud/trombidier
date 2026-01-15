# 🎯 INSTALLATION EN 3 ÉTAPES

## Pour les utilisateurs qui ne sont PAS familiers avec Python

---

## 📥 ÉTAPE 1 : Télécharger et décompresser

1. **Téléchargez** le fichier `Trombinoscope_Generator_v1.0.zip`
2. **Faites un clic droit** sur le fichier → **Extraire tout...**
3. **Choisissez** un emplacement (par exemple : `C:\Trombinoscope`)

---

## 🐍 ÉTAPE 2 : Installer Python (une seule fois)

### Si Python n'est PAS encore installé :

1. Allez sur **https://www.python.org/downloads/**
2. Cliquez sur **"Download Python 3.x.x"**
3. **Lancez l'installateur**
4. ⚠️ **IMPORTANT** : Cochez **"Add Python to PATH"** en bas de la fenêtre
5. Cliquez sur **"Install Now"**
6. Attendez la fin de l'installation
7. Fermez la fenêtre

### Pour vérifier si Python est installé :

1. Appuyez sur **Windows + R**
2. Tapez **cmd** et appuyez sur Entrée
3. Dans la fenêtre noire, tapez : `python --version`
4. Si vous voyez "Python 3.x.x", c'est bon ! ✅

---

## ⚡ ÉTAPE 3 : Créer l'exécutable

### Méthode Automatique (Recommandé) :

1. Ouvrez le dossier décompressé
2. **Double-cliquez** sur `build_exe.bat`
3. Une fenêtre noire s'ouvre et installe tout automatiquement
4. Attendez la fin (environ 2-3 minutes)
5. L'exécutable est créé dans le dossier `dist/`
6. **Double-cliquez** sur `dist/Trombinoscope_Generator.exe`
7. C'est prêt ! 🎉

### Méthode Alternative (Si la première ne marche pas) :

1. Appuyez sur **Windows + R**
2. Tapez **cmd** et appuyez sur Entrée
3. Dans la fenêtre noire, tapez ces commandes une par une :

```
cd C:\Trombinoscope
```
*(Remplacez par le chemin de votre dossier)*

```
pip install -r requirements_trombinoscope.txt
```
*Attendez que tout s'installe*

```
python trombinoscope_app.py
```
*L'application se lance !*

---

## 🎮 UTILISER L'APPLICATION

### Première utilisation :

1. **Lancez** l'application (double-clic sur l'exécutable)
2. Cliquez sur **"Parcourir"**
3. **Sélectionnez** votre dossier `CLASSE_JPG`
4. Vérifiez le **nom de l'établissement** et **l'année**
5. Cliquez sur **"🔍 Analyser les classes"**
6. Vérifiez l'aperçu
7. Choisissez **Word** ou **PDF**
8. Cliquez sur **"✨ Générer le Trombinoscope"**
9. Choisissez où **enregistrer** le fichier
10. Attendez quelques secondes
11. **Terminé !** 🎉

---

## 📁 PRÉPARER VOS DONNÉES

### Structure des dossiers :

```
📁 CLASSE_JPG/
   📁 2DE01/
      🖼️ DUPONT-Marie.jpg
      🖼️ MARTIN-Pierre.jpg
      🖼️ BERNARD-Sophie.jpg
   📁 2DE02/
      🖼️ ...
   📁 PG01/
      🖼️ ...
```

### ⚠️ IMPORTANT - Nommer les fichiers :

✅ **BON** : `DUPONT-Marie.jpg`  
✅ **BON** : `MARTIN-Pierre.jpg`  
✅ **BON** : `BERNARD-Sophie.jpg`  

❌ **MAUVAIS** : `Marie Dupont.jpg`  
❌ **MAUVAIS** : `DUPONT Marie.jpg`  
❌ **MAUVAIS** : `dupont-marie.jpg`  

**Format exact** : `NOM-Prenom.jpg` (avec le tiret)

---

## 🆘 PROBLÈMES FRÉQUENTS

### "Python n'est pas reconnu comme une commande..."

**Solution** :
1. Désinstallez Python
2. Réinstallez en cochant **"Add Python to PATH"**
3. Redémarrez votre ordinateur

---

### "Module PIL/docx not found"

**Solution** :
1. Ouvrez CMD (Windows + R → cmd)
2. Tapez : `pip install -r requirements_trombinoscope.txt`
3. Attendez la fin de l'installation

---

### "Les photos ne s'affichent pas"

**Solution** :
- Vérifiez que les fichiers sont en `.jpg`, `.jpeg` ou `.png`
- Vérifiez le format des noms : `NOM-Prenom.extension`
- Pas d'espaces dans les noms de dossiers

---

### "La conversion PDF ne marche pas"

**Solution** :
- Choisissez **Word (.docx)** à la place
- Ouvrez le fichier avec Microsoft Word
- Fichier → Enregistrer sous → PDF

---

### "L'application ne se lance pas"

**Solution 1** :
- Clic droit sur `build_exe.bat`
- **Exécuter en tant qu'administrateur**

**Solution 2** :
- Utilisez Python directement :
- Ouvrez CMD
- Tapez : `python trombinoscope_app.py`

---

## 💡 ASTUCES

### Pour aller plus vite :

1. **Créez un raccourci** de l'exécutable sur votre bureau
2. **Préparez vos dossiers** de photos à l'avance
3. **Testez** avec 2-3 classes d'abord

### Pour de meilleurs résultats :

- 📸 Utilisez des **photos de bonne qualité**
- 📏 Gardez des **dimensions similaires** pour toutes les photos
- 🗂️ **Organisez bien** vos dossiers de classes
- ✏️ **Vérifiez les noms** avant de générer

---

## ✅ CHECKLIST AVANT DE GÉNÉRER

Avant de cliquer sur "Générer", vérifiez :

- [ ] Toutes les photos sont dans les bons dossiers
- [ ] Les noms de fichiers sont au format `NOM-Prenom.jpg`
- [ ] Le nom de l'établissement est correct
- [ ] L'année scolaire est correcte
- [ ] Vous avez choisi le bon format (Word ou PDF)
- [ ] L'analyse a bien trouvé toutes vos classes

---

## 🎓 EXEMPLE COMPLET

### Situation :
Vous avez 3 classes à photographier :
- 2DE01 (28 élèves)
- 2DE02 (32 élèves)
- PG01 (25 élèves)

### Étapes :

1. **Créez** un dossier `CLASSE_JPG`
2. **Créez** 3 sous-dossiers : `2DE01`, `2DE02`, `PG01`
3. **Mettez** les photos dans chaque dossier
4. **Renommez** chaque photo : `NOM-Prenom.jpg`
5. **Lancez** l'application
6. **Sélectionnez** le dossier `CLASSE_JPG`
7. **Cliquez** sur "Analyser les classes"
8. **Vérifiez** que les 3 classes apparaissent (85 élèves au total)
9. **Choisissez** Word
10. **Cliquez** sur "Générer le Trombinoscope"
11. **Enregistrez** : `Trombinoscope_2024-2025.docx`
12. **Attendez** 10-20 secondes
13. **Ouvrez** le document et vérifiez
14. **Terminé !** 🎉

---

## 🎯 RÉSUMÉ ULTRA-RAPIDE

```
1. Télécharger + Décompresser
   ↓
2. Installer Python (cocher "Add to PATH")
   ↓
3. Double-clic sur build_exe.bat
   ↓
4. Utiliser dist/Trombinoscope_Generator.exe
   ↓
5. Profiter ! 🎉
```

---

## 📞 BESOIN D'AIDE ?

Si rien ne fonctionne :

1. Lisez **README_TROMBINOSCOPE.md** (plus détaillé)
2. Vérifiez que **Python 3.8+** est installé
3. Essayez la **méthode alternative** ci-dessus
4. Redémarrez votre ordinateur et réessayez

---

**Bonne création de trombinoscopes ! 📚✨**

*Version simplifiée pour utilisateurs débutants*
