# Générateur de Revue de Presse Thématique avec Synthèse Vocale

## Description

Cette application Streamlit permet de :
- Importer des fichiers presse (.pdf, .docx, .txt, images)
- Extraire, classifier et résumer les articles automatiquement
- Générer une revue de presse Word organisée par thème
- Produire un script voix-off en français et sa traduction automatique en wolof
- Générer un fichier audio MP3 de la voix-off française (via gTTS)

## Installation

1. Cloner le dépôt :
```bash
git clone https://github.com/papaadama91/revuede-presse-app.git
cd revuede-presse-app
```

2. Installer les dépendances :
```bash
pip install -r requirements.txt
```

3. Installer Tesseract OCR :
- Windows : https://github.com/tesseract-ocr/tesseract
- macOS : `brew install tesseract`
- Linux : `sudo apt install tesseract-ocr`

## Usage
```bash
streamlit run app.py
```

## Déploiement en ligne
Connecte ton dépôt à [Streamlit Cloud](https://streamlit.io/cloud) pour publier ton app.

## Licence
MIT
