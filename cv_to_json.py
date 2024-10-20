import google.generativeai as genai
import pdfplumber
from flask import Flask, jsonify, request
from flask_cors import CORS
import json

app = Flask(__name__)

CORS(app)

def extract_text_from_pdf(file):
    with pdfplumber.open(file) as pdf:
        text = ""
        for page in pdf.pages:
            text += page.extract_text()
    return text

@app.route('/api/cv-to-json', methods=['POST'])
def cv_to_json():
    if 'file' not in request.files:
        return jsonify({'message': 'File not found'}), 400

    file = request.files['file']

    if file and file.filename.endswith('.pdf'):
        extracted_text = extract_text_from_pdf(file)
        print("============================TEXT OF CV ====================================")
        print(extracted_text)

        model = "name: string; email: string; phone: string; objective?: string; education: { degree: string; institution: string; year?: string; cgpa?: string; }[]; experience: { company: string;title: string; description: string; duration: string; }[]; github?: string; projects?: { name: string; description: string; technologies: string; }[]; skills: string[]; technical_skills?: string[];"
        
        # Google PaLM model API configuration
        api_key = 'AIzaSyCf77ZpJx1d8fmexr2an5SQ-qAKSL3GZDk'
        genai.configure(api_key=api_key)
        
        model = genai.GenerativeModel(model_name="gemini-1.5-flash")
        
        # Use `generate_content`
        prompt = (
           "Convert this CV to JSON using the following fields: name, email, phone, objective, education (degree, institution, year, cgpa), "
            "experience (company, title, description, duration), github, projects (name, description, technologies), skills [], technical_skills []. "
            "If any field is not mentioned in the CV, leave it empty. "
    "       Only return the JSON object with no additional text. The CV text is: ." + extracted_text
        )
        
        response = model.generate_content(prompt)

        print(response.text)

        response_json = json.loads(response.text)
        
        return jsonify(response_json), 200

    return jsonify({'message': 'Invalid file type, please upload a PDF'}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8000,debug=True)
