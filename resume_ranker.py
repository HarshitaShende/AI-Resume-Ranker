import os
import PyPDF2
import spacy
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

nlp = spacy.load('en_core_web_sm')

def extract_text_from_pdf(pdf_path):
    with open(pdf_path, 'rb') as f:
        reader = PyPDF2.PdfReader(f)
        text = ''
        for page in reader.pages:
            text += page.extract_text()
    return text

def clean_text(text):
    doc = nlp(text.lower())
    tokens = [token.lemma_ for token in doc if not token.is_stop and token.is_alpha]
    return " ".join(tokens)

def rank_resumes(jd_path, resume_folder):
    jd_text = extract_text_from_pdf(jd_path) if jd_path.endswith('.pdf') else open(jd_path).read()
    jd_cleaned = clean_text(jd_text)

    scores = []
    for filename in os.listdir(resume_folder):
        if filename.endswith('.pdf'):
            path = os.path.join(resume_folder, filename)
            resume_text = extract_text_from_pdf(path)
            resume_cleaned = clean_text(resume_text)

            vectorizer = TfidfVectorizer()
            vectors = vectorizer.fit_transform([jd_cleaned, resume_cleaned])
            score = cosine_similarity(vectors[0:1], vectors[1:2])[0][0]
            scores.append((filename, score))

    ranked = sorted(scores, key=lambda x: x[1], reverse=True)
    return ranked
