# 📰 SEN Revue de Presse – Générateur IA avec OCR, Résumé, Script Vocal

**SEN Revue de Presse** est une application Streamlit intelligente qui :

- 📥 Accepte fichiers presse (PDF, Word, texte, images)
- 🧠 Résume automatiquement le contenu avec IA (BART)
- 🗂 Classe les articles par **thèmes** (Politique, Économie, etc.)
- 🌍 Génère un **script voix-off** (français + traduction wolof)
- 🔊 Produit un **MP3 vocal** avec `gTTS`
- 📄 Génère un fichier Word (.docx) thématique
- 🎬 Propose un **script prêt pour vidéo YouTube**

---

## 🚀 Démo en ligne (Streamlit Cloud)

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://sen-revue-presse.streamlit.app)

---

## 🖥️ Installation locale

```bash
git clone https://github.com/papaadama91/sen-revue-presse.git
cd sen-revue-presse

# (Optionnel)
python -m venv venv
source venv/bin/activate

pip install -r requirements.txt
streamlit run app.py
