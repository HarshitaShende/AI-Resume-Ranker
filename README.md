# 🤖 AI Resume Ranker
An NLP-powered web app that ranks resumes based on a job description using TF-IDF and cosine similarity.

![Screenshot_19-6-2025_162149_127 0 0 1](https://github.com/user-attachments/assets/a0cb7325-cb3d-4887-aa35-73ea906d2f98)

![Screenshot_19-6-2025_162242_127 0 0 1](https://github.com/user-attachments/assets/584e9e83-c01e-4a37-8d1d-11d90c2ce260)


![Screenshot 2025-06-19 162342](https://github.com/user-attachments/assets/59d3f354-6b9c-4499-95d6-a958707149df)

![Screenshot 2025-06-19 162417](https://github.com/user-attachments/assets/7e26aafe-bbd5-46a8-b22c-86d6284d0011)


## 🛠 Tech Stack
- Python 3
- Flask
- SpaCy (for text preprocessing)
- Scikit-learn (TF-IDF, cosine similarity)
- PyPDF2 (PDF parsing)
- HTML/CSS frontend

## 📦 Features
- Upload Job Description (PDF/TXT)
- Upload multiple Resumes (PDF)
- View match % for each resume
- Responsive UI with gradient design
- Automatically clears previous uploads

## 🚀 Run Locally

```bash
git clone https://github.com/HarshitaShende/ai-resume-ranker.git
cd ai-resume-ranker
pip install -r requirements.txt
python -m spacy download en_core_web_sm
python app.py
