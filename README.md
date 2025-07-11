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

📂 Formats supportés
Type de fichier	Extensions
Texte brut	.txt
Word	.docx
PDF	.pdf
Image presse	.jpg, .png

OCR basé sur easyocr — fonctionne sur Streamlit Cloud.

🎙 Script & Voix-off
✅ Script généré automatiquement par thème

🇫🇷 Français + 🌍 traduction wolof

🔊 MP3 généré automatiquement avec gTTS

🎬 Génération vidéo YouTube
Le script peut être utilisé dans :

CapCut / Canva (copier/coller script + audio)

Shotcut / OpenShot avec images de presse

Une future version inclura génération automatique de vidéos .mp4

✨ Exemples d'usages
Présenter l'actualité à la radio locale

Résumer les journaux du jour pour YouTube/TikTok

Préparer un bulletin de veille en entreprise

🔧 À venir
✅ Upload images pour vidéo

🎞 Génération automatique de vidéo .mp4

🗣 Voix masculine via edge-tts ou API ElevenLabs

🌍 Traduction Wolof améliorée

🧠 Technologies
Python, Streamlit

EasyOCR, HuggingFace Transformers (BART)

gTTS, Deep Translator

Word export (python-docx)

📜 Licence
MIT – utilisation libre à but personnel, éducatif ou professionnel.

👨‍💻 Auteur
@papaadama91

yaml
Copier
Modifier
