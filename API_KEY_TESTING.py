import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv('API_KEY')
genai.configure(api_key=api_key)

model = genai.GenerativeModel(model_name="gemini-1.5-flash")

# Use `generate_content`
prompt = (
    f"Convert this CV to JSON and keep the following fields: education, "
    f"experience, skills, projects, programming languages. The CV text is:"
)

response = model.generate_content(prompt)

print(response.text)