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

candidate_json = {
    "education": [
        {
            "cgpa": "2.8",
            "degree": "Bachelors in Computer Science",
            "institution": "FAST NUCES",
            "year": "2025"
        }
    ],
    "email": "nasiruddinabubakar@gmail.com",
    "experience": [
        {
            "company": "Trization LLC",
            "description": "I was managing the landing website for the company.",
            "duration": "june 2023 - december 2023",
            "title": "Junior frontend developer"
        }
    ],
    "github": "https://github.com/nasiruddinabubakar",
    "name": "NASIRUDDIN ABUBAKAR",
    "objective": "A full stack developer, ready to make people's lives easier",
    "phone": "+923212120428",
    "projects": [
        {
            "description": "Developed SnapGram, an Instagram clone, using React for the frontend and integrated it with the powerful Appwrite backend on the cloud. SnapGram features functionalities such as uploading photos, following other users, and liking posts. Leveraging Appwrite's cloud services, the application ensures efficient data storage and retrieval.",
            "name": "Social Media App",
            "technologies": [
                "React",
                "Appwrite"
            ]
        },
        {
            "description": "Developed a comprehensive cargo shipping management system using React for the frontend and Node.js with Express for the backend. The system enables companies to efficiently manage their shipping operations, including adding and viewing ships, tracking orders, and analyzing shipping summaries. I implemented user authentication for secure access and integrated APIs for real-time data updates. The project showcases my proficiency in full-stack development, utilizing modern technologies to create a robust and user-friendly solution. It also demonstrates my skills in handling data, designing intuitive user interfaces, and ensuring the security and integrity of sensitive information. This project reflects my commitment to delivering high-quality software solutions that meet business needs and user expectations.",
            "name": "ShippinInit",
            "technologies": [
                "React",
                "Node.js",
                "Express"
            ]
        },
        {
            "description": "A blog sharing application crafted in C. The application allows users to share and engage with blog posts in a streamlined manner. With a focus on implementing robust data structures, such as linked lists and arrays, the application efficiently manages and retrieves blog content.",
            "name": "E-Baithak",
            "technologies": [
                "C"
            ]
        },
        {
            "description": "Developed a complete School Management System on C using Object Oriented Concepts. The software allows students to view their marks and attendance, the teacher can mark attendance and upload results, the administrator can view and add new classes.",
            "name": "School Management System",
            "technologies": [
                "C"
            ]
        }
    ],
    "skills": [
        "Html",
        "CSS",
        "JavaScript",
        "Typescript",
        "ReactJS",
        "NodeJs",
        "MySQL",
        "ShadCN"
    ],
    "technical_skills": []
}
weights = {
        "title": 0.20,
        "requirement": 0.40,
        "description": 0.35,
        "domain": 0.05
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
    f"candiate cv: {candidate_json}"
    f"do the ranking based on semantic matching."
    f"weight of each type of ranking: {weights}"
    f"also add overall similarity in the json object according to weights of each type of ranking."
)

response = model.generate_content(prompt)

print(response.text)