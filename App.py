from flask import Flask, render_template, request
import os
from resume_ranker import rank_resumes

app = Flask(__name__)
UPLOAD_FOLDER = 'resumes'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        jd_file = request.files['jd_file']
        resumes = request.files.getlist('resume_files')

        jd_path = os.path.join(app.config['UPLOAD_FOLDER'], 'job_description.txt')
        jd_file.save(jd_path)

        for resume in resumes:
            resume.save(os.path.join(app.config['UPLOAD_FOLDER'], resume.filename))

        ranked = rank_resumes(jd_path, app.config['UPLOAD_FOLDER'])
        return render_template('index.html', results=ranked)

    return render_template('index.html', results=None)

if __name__ == '__main__':
    app.run(debug=True)


