import streamlit as st
from PyPDF2 import PdfReader
from docx import Document as DocxDocument
import os
import re
from transformers import pipeline
from collections import defaultdict
from deep_translator import GoogleTranslator
from gtts import gTTS
from doctr.io import DocumentFile
from doctr.models import ocr_predictor

@st.cache_resource
def load_summarizer():
    return pipeline("summarization", model="facebook/bart-large-cnn")

@st.cache_resource
def load_ocr_model():
    return ocr_predictor(pretrained=True)

summarizer = load_summarizer()
ocr_model = load_ocr_model()

def extract_text(file):
    ext = os.path.splitext(file.name)[-1].lower()
    if ext in [".jpg", ".jpeg", ".png", ".pdf"]:
        doc = DocumentFile.from_pdf(file) if ext == ".pdf" else DocumentFile.from_images(file)
        result = ocr_model(doc)
        return result.export()["value"]
    elif ext == ".docx":
        doc = DocxDocument(file)
        return "\n".join([p.text for p in doc.paragraphs])
    elif ext == ".txt":
        return file.read().decode("utf-8")
    else:
        return ""

def extract_metadata(text):
    title = text.strip().split("\n")[0][:80]
    date_match = re.search(r'\d{1,2} \w+ \d{4}', text)
    date = date_match.group() if date_match else "Date inconnue"
    return title, date

def classify_article(text):
    keywords = {
        "Politique": ["président", "gouvernement", "élection"],
        "Économie": ["croissance", "pib", "bourse", "marché", "inflation"],
        "Société": ["éducation", "santé", "social", "famille", "logement"],
        "Culture": ["musique", "cinéma", "livre", "art", "festival"],
        "Sport": ["football", "match", "jo", "ligue", "compétition"]
    }
    for theme, mots in keywords.items():
        if any(mot in text.lower() for mot in mots):
            return theme
    return "Autres"

def summarize_text(text):
    try:
        return summarizer(text[:1024], max_length=100, min_length=30, do_sample=False)[0]['summary_text']
    except:
        return "Résumé non disponible."

def translate_to_wolof(text):
    try:
        return GoogleTranslator(source='fr', target='sn').translate(text)
    except:
        return "[Traduction indisponible]"

def generate_voiceover_script(articles_by_theme, translate=False):
    script = ""
    for theme, articles in articles_by_theme.items():
        script += f"\n🗂️ {theme}\n"
        for art in articles:
            phrase = f"Le {art['date']}, un média local a rapporté : {art['resume']}\n"
            if translate:
                phrase = translate_to_wolof(phrase)
            script += phrase
    return script.strip()

def generate_audio_fr(text, filename="voix_off_fr.mp3"):
    tts = gTTS(text=text, lang="fr")
    tts.save(filename)
    return filename

from docx import Document as DocxDocumentExport
def generate_docx_by_theme(articles_by_theme):
    doc = DocxDocumentExport()
    doc.add_heading("Revue de Presse Thématique", 0)
    for theme, articles in articles_by_theme.items():
        doc.add_heading(f"Thème : {theme}", level=1)
        for art in articles:
            doc.add_heading(art['titre'], level=2)
            doc.add_paragraph(f"Date : {art['date']}")
            doc.add_paragraph("Résumé :")
            doc.add_paragraph(art['resume'])
            doc.add_paragraph("---")
    path = "revue_presse.docx"
    doc.save(path)
    return path

# Interface Streamlit
st.title("📰 Générateur de Revue de Presse Thématique (DocTR OCR)")
st.markdown("Charge tes fichiers presse ci-dessous (.pdf, .docx, .txt, .png, .jpg)")

uploaded_files = st.file_uploader("Fichiers :", accept_multiple_files=True, type=["pdf", "docx", "txt", "png", "jpg", "jpeg"])

if uploaded_files:
    articles_by_theme = defaultdict(list)
    with st.spinner("Analyse des fichiers en cours..."):
        for file in uploaded_files:
            text = extract_text(file)
            titre, date = extract_metadata(text)
            theme = classify_article(text)
            resume = summarize_text(text)
            article = {"titre": titre, "date": date, "theme": theme, "resume": resume}
            articles_by_theme[theme].append(article)

    if articles_by_theme:
        docx_path = generate_docx_by_theme(articles_by_theme)
        st.success("✅ Revue de presse générée.")
        with open(docx_path, "rb") as f:
            st.download_button("📥 Télécharger Word", f, file_name="revue_presse.docx")

        st.subheader("🎙️ Script Voix-Off (Français)")
        fr_script = generate_voiceover_script(articles_by_theme)
        st.text_area("Script FR", fr_script, height=300)

        st.subheader("🌍 Script Voix-Off (Wolof)")
        wo_script = generate_voiceover_script(articles_by_theme, translate=True)
        st.text_area("Script WO", wo_script, height=300)

        st.download_button("📤 Télécharger Script FR", fr_script, file_name="script_voixoff_fr.txt")
        st.download_button("📤 Télécharger Script WO", wo_script, file_name="script_voixoff_wolof.txt")

        if st.button("🔉 Générer voix-off FR (MP3)"):
            audio_path = generate_audio_fr(fr_script)
            with open(audio_path, "rb") as audio_file:
                st.audio(audio_file.read(), format="audio/mp3")
                st.download_button("📥 Télécharger MP3", audio_file, file_name="voix_off_fr.mp3")
