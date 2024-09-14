import google.generativeai as genai
import PyPDF2
from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)

CORS(app)

def extract_text_from_pdf(reader):
    text = ""
    for page in range(len(reader.pages)):
        text += reader.pages[page].extract_text() or ''  # Safeguard in case no text is extracted
    return text

@app.route('/api/cv-to-json', methods=['POST'])
def cv_to_json():
    if 'file' not in request.files:
        return jsonify({'message': 'File not found'}), 400

    file = request.files['file']

    if file and file.filename.endswith('.pdf'):
        reader = PyPDF2.PdfReader(file)
        extracted_text = extract_text_from_pdf(reader)
        
        # Google PaLM model API configuration
        api_key = 'AIzaSyCf77ZpJx1d8fmexr2an5SQ-qAKSL3GZDk'
        genai.configure(api_key=api_key)
        
        model = genai.GenerativeModel(model_name="gemini-1.5-flash")
        
        # Use `generate_content`
        prompt = (
            f"Convert this CV to JSON and keep the following fields: education, "
            f"experience, skills, projects, technical_skills and keep other details at top of json as well but always keep these fields. The CV text is: {extracted_text}"
        )
        
        response = model.generate_content(prompt)

        print(response.text)
        
        return jsonify(response.text), 200

    return jsonify({'message': 'Invalid file type, please upload a PDF'}), 400

if __name__ == '__main__':
    app.run(debug=True)
