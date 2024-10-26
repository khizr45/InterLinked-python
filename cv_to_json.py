import google.generativeai as genai
import pdfplumber
from flask import Flask, jsonify, request
from flask_cors import CORS
import json
import os
from dotenv import load_dotenv

def extract_text_from_pdf(file):
    with pdfplumber.open(file) as pdf:
        text = ""
        for page in pdf.pages:
            text += page.extract_text()
    return text


def cv_to_json(file):
        load_dotenv()
        extracted_text = extract_text_from_pdf(file)
        
        # Google PaLM model API configuration
        api_key = os.getenv('API_KEY')
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

        response_json = json.loads(response.text)
        
        return response_json

