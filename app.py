from flask import Flask, render_template, request, redirect, url_for, send_file
from gtts import gTTS
import os
import PyPDF2

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'pdf' not in request.files:
            return 'No file part'
        
        file = request.files['pdf']
        if file.filename == '':
            return 'No selected file'
        
        if file and file.filename.endswith('.pdf'):
            # Save the uploaded file to the server
            pdf_path = os.path.join('uploads', file.filename)
            file.save(pdf_path)
            
            # Extract text from the PDF
            with open(pdf_path, 'rb') as pdf_file:
                pdfreader = PyPDF2.PdfReader(pdf_file)
                text = ""
                for page in pdfreader.pages:
                    text += page.extract_text().strip().replace('\n', ' ')
            
            # Convert the extracted text to speech
            tts = gTTS(text=text, lang='en', slow=False)
            mp3_path = pdf_path.replace('.pdf', '.mp3')
            tts.save(mp3_path)
            
            return redirect(url_for('download', filename=os.path.basename(mp3_path)))
    
    return render_template('index.html')

@app.route('/download/<filename>')
def download(filename):
    return send_file(os.path.join('uploads', filename), as_attachment=True)

if __name__ == '__main__':
    os.makedirs('uploads', exist_ok=True)
    app.run(debug=True)