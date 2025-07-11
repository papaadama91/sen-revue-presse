# Générateur de Revue de Presse Thématique avec Synthèse Vocale

# 📰 SEN Revue de Presse – Générateur intelligent avec script vocal

**SEN Revue de Presse** est une application Streamlit qui :
- 📥 Accepte fichiers presse (PDF, Word, texte, images)
- 🧠 Résume automatiquement les contenus avec IA
- 🗂 Classe les articles par **thèmes** (Politique, Économie, Société…)
- 🎙 Génère un **script voix-off** (français + wolof)
- 🔊 Produit un fichier **audio MP3**
- 📄 Génère un fichier Word structuré

---

## 🚀 Démo (Streamlit Cloud)

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://sen-revue-presse.streamlit.app)

---

## 📦 Installation locale

### 1. Cloner le dépôt

```bash
git clone https://github.com/papaadama91/sen-revue-presse.git
cd sen-revue-presse
2. Créer un environnement virtuel (optionnel mais recommandé)
bash
Copier
Modifier
python -m venv venv
source venv/bin/activate      # Linux/macOS
venv\Scripts\activate.bat     # Windows
3. Installer les dépendances
bash
Copier
Modifier
pip install -r requirements.txt
Pas besoin d’installer Tesseract : l’OCR est intégré avec DocTR.

4. Lancer l'application
bash
Copier
Modifier
streamlit run app.py
📁 Formats supportés
Type de fichier	Extensions
Texte brut	.txt
Word	.docx
PDF	.pdf
Images presse	.jpg, .png

🌍 Traduction & Script Wolof
Traduction automatique (fr ➝ wolof) avec deep-translator

Script généré lisible + téléchargeable

Synthèse vocale disponible en français (gTTS)

🔒 Licence
Projet open-source sous licence MIT. Utilisation libre à des fins personnelles, éducatives ou professionnelles.

🙏 Contributeur principal
👤 @papaadama91
