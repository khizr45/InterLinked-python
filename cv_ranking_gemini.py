import google.generativeai as genai
import os
from dotenv import load_dotenv
import json


weights = {
        "title": 0.20,
        "requirement": 0.40,
        "description": 0.35,
        "domain": 0.05
    }
def cv_ranking_gemini(job_json,candidate_json):
    load_dotenv()
    api_key = os.getenv('API_KEY')
    genai.configure(api_key=api_key)

    model = genai.GenerativeModel(model_name="gemini-1.5-flash")

    # Use `generate_content`
    prompt = (
        f"I am matching job title with objective, experience position on candidate cv and naming it as title_scale."
        f"secondly, I am matching job_requirements with skills and technical skills on candidate cv and naming it as skills_scale."
        f"thirdly, I am matching job description with object, experience description and project description on candidates cv and naming it as exprience_scale."
        f"fourthly, I am matching domain with education_degree, experience position and naming it as domain_scale"
        f"Now tell me how should I break down scaling total of 1 between these 4 catgories for provided job description."
        f"Just return the json not any other thing, containg the key and value of scaling of all categories."
        f"job description: {job_json}"
        f"candiate cv: {candidate_json}"
        f"do the ranking based on semantic matching."
        f"weight of each type of ranking: {weights}"
        f"also add overall similarity in the json object according to weights of each type of ranking."
    )

    response = model.generate_content(prompt)

    start_index = response.text.find('{')
    end_index = response.text.rfind('}') + 1

    response_json = json.loads(response.text[start_index:end_index])

    return response_json["overall_similarity"] , response_json["title_scale"] , response_json["skills_scale"], response_json["experience_scale"], response_json["domain_scale"]