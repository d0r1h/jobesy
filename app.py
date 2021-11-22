from flask import Flask, flash, request, redirect, render_template
from werkzeug.utils import secure_filename
import os
import urllib.request
UPLOAD_FOLDER =  "/home/d0r1h/Desktop/Jobsy/job"

app = Flask(__name__)
app.secret_key = "123"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'doc', 'docx'])

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/')
def upload_form():
    return render_template("job.html")


@app.route('/', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        resume_text = request.form['resume_text']
        if 'file' not in request.files:
            flash('No file exist')
            return redirect(request.url)

        file = request.files['file']
        
        if file.filename == '':
            flash('No file selected for uploading')
            return redirect(request.url)

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)

            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            flash('File successfully uploaded')
            return redirect('/')
        else:
            flash('Allowed file types are txt, pdf, doc, docx')
            return redirect(request.url)


if __name__ == "__main__":
    app.run(debug=True)
