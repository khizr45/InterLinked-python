import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

job_json = {
        "job_id": 8,
        "person_posted": 5,
        "title": "Software Developer",
        "location": "Hybrid",
        "job_type": "Full Time",
        "job_domain": "Software Engineering",
        "createdAt": "2024-11-02T12:01:05.000Z",
        "updatedAt": "2024-11-02T12:01:05.000Z",
        "jobDetails": [
            {
                "detail_id": 15,
                "job_id": 8,
                "field_name": "job_requirements",
                "value": "<p>Education, Experience, Licenses &amp; Certifications:</p><p>Experience Required:</p><p> • 1 year of information systems experience as a Software Developer Education </p><p>• An Associate's Degree in Computer Science, Computer Information Services, Computer Engineering, Mathematics, or Engineering is required </p><p>• A Bachelor's Degree in Computer Science, Computer Information Services, Computer Engineering, Mathematics, or Engineering is preferred.</p><p> Experience Preferred:</p><p> • 3 years of information systems experience as a Software Developer</p><p> Licenses &amp; Certifications :</p><p>• None required</p><p><br></p><p>Skills/Requirements:</p><p> • Working knowledge of information technology fundamentals and programming languages.</p><p> • Ability to gain detailed knowledge of in-house programming languages, program design and development procedures, turnover procedures, and housekeeping standards. </p><p>• Ability to perform analysis of straightforward system functionality with support of more senior Software Engineers. • Ability to gain detailed knowledge of general system architecture and functionality, as well as detailed knowledge of specific sub-systems. </p><p>• Working knowledge of commonly used concepts, practices, and procedures as it relates to software development. </p><p>• Ability to effectively manage time while working on multiple assignments with guidance as to relative priorities of assignments.</p>",
                "createdAt": "2024-11-02T12:01:05.000Z",
                "updatedAt": "2024-11-02T12:01:05.000Z"

                
            },
            {
                "detail_id": 16,
                "job_id": 8,
                "field_name": "job_description",
                "value": "<p>Job Summary:</p><p> Provides programming support for new and existing information systems based on user specifications with guidance from other staff members. Consults with and provides users with assistance in determining program enhancements and required maintenance.&nbsp;&nbsp;</p><p><br></p><p>Job Duties:</p><p> • Performs program maintenance, modifications, and enhancements to new/existing systems through programming, testing, documenting, and training users. </p><p>• Confers with user personnel and department representatives in resolving questions of program/system intent, output requirements, input data acquisition, and inclusion of internal checks and controls. </p><p>• Responsible for learning Company systems and how they are automated. </p><p>• Provides on-call programming support.</p><p> • Communicates and works as needed with any internal/external customers with a more senior developer/engineer or manager present. </p><p>• All Southeastern Freight Lines associates must embrace and support the five values that define the Company’s culture and be personally committed to the Quality Improvement Process. </p><p>• Performs other duties as assigned by management.</p>",
                "createdAt": "2024-11-02T12:01:05.000Z",
                "updatedAt": "2024-11-02T12:01:05.000Z"
            }
        ]
    }

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
)

response = model.generate_content(prompt)

print(response.text)