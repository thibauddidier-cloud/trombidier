# 📚 APPLICATION TROMBINOSCOPE - INDEX DES FICHIERS

Bienvenue ! Ce package contient tout ce dont vous avez besoin pour générer vos trombinoscopes.

---

## 🚀 DÉMARRAGE RAPIDE

### Vous êtes débutant ?
👉 Lisez **INSTALLATION_FACILE.md**

### Vous connaissez Python ?
👉 Lisez **GUIDE_RAPIDE.md**

### Vous voulez tous les détails ?
👉 Lisez **README_TROMBINOSCOPE.md**

---

## 📁 LISTE DES FICHIERS

### 🎯 Pour démarrer rapidement

| Fichier | Description | Quand l'utiliser |
|---------|-------------|------------------|
| **INSTALLATION_FACILE.md** | Guide pour débutants | Vous n'avez jamais utilisé Python |
| **GUIDE_RAPIDE.md** | Guide de démarrage rapide | Vous voulez démarrer en 5 min |
| **launcher.py** | Lance l'app automatiquement | Double-clic pour lancer |

### 📖 Documentation

| Fichier | Description |
|---------|-------------|
| **README_TROMBINOSCOPE.md** | Documentation complète |
| **RÉCAPITULATIF.md** | Vue d'ensemble du projet |
| **README.txt** | Version texte simple |

### 💻 Fichiers de l'application

| Fichier | Description |
|---------|-------------|
| **trombinoscope_app.py** | Application principale (GUI) |
| **test_trombinoscope.py** | Version ligne de commande |
| **launcher.py** | Lanceur automatique |

### 🔧 Scripts de build

| Fichier | Système | Description |
|---------|---------|-------------|
| **build_exe.bat** | Windows | Crée l'exécutable .exe |
| **build_exe.sh** | Linux/Mac | Crée l'exécutable |

### ⚙️ Fichiers de configuration

| Fichier | Description |
|---------|-------------|
| **requirements_trombinoscope.txt** | Dépendances Python |
| **trombinoscope.spec** | Configuration PyInstaller |

### 📄 Assets et exemples

| Dossier/Fichier | Description |
|-----------------|-------------|
| **assets/** | Page de couverture |
| **sample_data/** | Exemples de photos |

---

## 🎯 QUEL FICHIER LIRE EN PREMIER ?

### Scénario 1 : Je ne connais pas Python
```
1. INSTALLATION_FACILE.md
2. Installer Python
3. Double-clic sur build_exe.bat
4. Utiliser l'exécutable
```

### Scénario 2 : Je connais un peu Python
```
1. GUIDE_RAPIDE.md
2. pip install -r requirements_trombinoscope.txt
3. python launcher.py
```

### Scénario 3 : Je veux tout comprendre
```
1. RÉCAPITULATIF.md (vue d'ensemble)
2. README_TROMBINOSCOPE.md (détails)
3. Personnaliser trombinoscope_app.py
```

### Scénario 4 : Je veux juste tester
```
1. pip install -r requirements_trombinoscope.txt
2. python test_trombinoscope.py
3. Ouvrir Trombinoscope_Test.docx
```

---

## 🔥 ACTIONS RAPIDES

### Installer les dépendances
```bash
pip install -r requirements_trombinoscope.txt
```

### Lancer l'application (avec interface)
```bash
python launcher.py
```
ou
```bash
python trombinoscope_app.py
```

### Tester (sans interface)
```bash
python test_trombinoscope.py
```

### Créer l'exécutable Windows
```bash
build_exe.bat
```

### Créer l'exécutable Linux/Mac
```bash
chmod +x build_exe.sh
./build_exe.sh
```

---

## 📊 ARBORESCENCE DU PACKAGE

```
distribution_trombinoscope/
│
├── 📄 INDEX.md (ce fichier)
├── 📄 README.txt
├── 📄 INSTALLATION_FACILE.md ⭐ (pour débutants)
├── 📄 GUIDE_RAPIDE.md ⭐ (démarrage rapide)
├── 📄 README_TROMBINOSCOPE.md (doc complète)
├── 📄 RÉCAPITULATIF.md (vue d'ensemble)
│
├── 🐍 trombinoscope_app.py (app principale)
├── 🐍 test_trombinoscope.py (test CLI)
├── 🐍 launcher.py ⭐ (lanceur auto)
│
├── 🔧 build_exe.bat (Windows)
├── 🔧 build_exe.sh (Linux/Mac)
├── ⚙️ requirements_trombinoscope.txt
├── ⚙️ trombinoscope.spec
│
├── 📁 assets/
│   └── 001_TROMBI_COUV_RECTO.odt
│
└── 📁 sample_data/
    └── CLASSE_JPG/
        └── 2DE01/
            ├── ALFRANCA-Eva.jpg
            └── ANDRADE-Tiana.jpg
```

---

## ✅ CHECKLIST DE DÉMARRAGE

Avant de commencer, vérifiez :

- [ ] Python 3.8+ installé (avec "Add to PATH")
- [ ] Package décompressé dans un dossier
- [ ] Lu au moins un fichier de documentation
- [ ] Photos organisées au format NOM-Prenom.jpg
- [ ] Dossiers de classes prêts (2DE01, PG01, etc.)

---

## 🎓 EXEMPLES D'UTILISATION

### Exemple 1 : Test rapide avec les données fournies
```bash
python test_trombinoscope.py
```
→ Génère un fichier Word avec les 2 photos d'exemple

### Exemple 2 : Interface graphique
```bash
python launcher.py
```
→ Lance l'application avec GUI

### Exemple 3 : Créer un exécutable
```bash
build_exe.bat
```
→ Crée `dist/Trombinoscope_Generator.exe`

---

## 💡 CONSEILS

### Pour les débutants
1. Commencez par **INSTALLATION_FACILE.md**
2. Suivez les étapes pas à pas
3. Testez avec quelques photos d'abord
4. Puis testez avec toutes vos classes

### Pour les utilisateurs expérimentés
1. Installez les dépendances
2. Personnalisez `trombinoscope_app.py` si nécessaire
3. Créez l'exécutable
4. Distribuez-le à vos collègues

### Pour les développeurs
1. Lisez le code dans `trombinoscope_app.py`
2. Modifiez les couleurs, la mise en page, etc.
3. Testez avec `test_trombinoscope.py`
4. Recréez l'exécutable

---

## 🆘 BESOIN D'AIDE ?

### Problème d'installation
→ Consultez **INSTALLATION_FACILE.md** section "Problèmes fréquents"

### Problème de génération
→ Consultez **README_TROMBINOSCOPE.md** section "Résolution de problèmes"

### Question sur les fonctionnalités
→ Consultez **RÉCAPITULATIF.md** section "Fonctionnalités"

### Erreur technique
→ Vérifiez que Python 3.8+ est installé avec "Add to PATH"

---

## 📞 QUESTIONS FRÉQUENTES

**Q : Quel fichier dois-je lire en premier ?**
R : Si vous débutez → INSTALLATION_FACILE.md, sinon → GUIDE_RAPIDE.md

**Q : Comment créer l'exécutable .exe ?**
R : Double-cliquez sur build_exe.bat

**Q : Mes photos ne s'affichent pas**
R : Vérifiez le format des noms : NOM-Prenom.jpg

**Q : La conversion PDF ne marche pas**
R : Utilisez Word (.docx) puis convertissez avec Microsoft Word

**Q : Puis-je personnaliser les couleurs ?**
R : Oui, modifiez trombinoscope_app.py lignes 30-33

---

## 🎯 RÉSUMÉ

### 3 façons d'utiliser l'application :

1. **Exécutable** (recommandé pour distribution)
   - Lancez `build_exe.bat`
   - Utilisez `dist/Trombinoscope_Generator.exe`

2. **Avec launcher** (recommandé pour usage personnel)
   - Double-clic sur `launcher.py`
   - Installe automatiquement les dépendances

3. **Direct** (pour développeurs)
   - `pip install -r requirements_trombinoscope.txt`
   - `python trombinoscope_app.py`

---

## ✨ PRÊT À COMMENCER ?

1. **Lisez** le fichier adapté à votre niveau
2. **Suivez** les instructions
3. **Testez** avec les données d'exemple
4. **Générez** votre premier trombinoscope !

**Bonne création ! 📚🎓✨**

---

*Version 1.0 - Janvier 2025*  
*Développé pour le Lycée Toulouse Lautrec*
