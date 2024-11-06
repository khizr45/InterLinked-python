from sentence_transformers import SentenceTransformer, util

# Load the model


# Sample job JSON object
job_js = {
        "job_id": 103,
        "person_posted": 15,
        "title": "Frontend Developer",
        "location": "Hybrid",
        "job_type": "Part Time",
        "job_domain": "Web Development",
        "createdAt": "2024-10-21T16:49:31.000Z",
        "updatedAt": "2024-10-21T16:49:31.000Z",
        "jobDetails": [
            {
                "detail_id": 1,
                "job_id": 103,
                "field_name": "job_requirements",
                "value": "Proficient in JavaScript, React, and CSS frameworks"
            },
            {
                "detail_id": 2,
                "job_id": 103,
                "field_name": "job_description",
                "value": "Build responsive UI components and maintain web applications"
            }
        ]
    }
# Sample candidate JSON object
candidate_js = {
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

def cvRanking(job_json , candidate_json):
    model = SentenceTransformer('all-MiniLM-L6-v2')
    # Extract relevant job fields
    job_title = job_json["title"]
    job_domain = job_json["job_domain"]
    job_requirements = " ".join([detail["value"] for detail in job_json["jobDetails"] if detail["field_name"] == "job_requirements"])
    job_description = " ".join([detail["value"] for detail in job_json["jobDetails"] if detail["field_name"] == "job_description"])

    # Define weights for each component based on the table
    weights = {
        "title": 0.20,
        "requirement": 0.40,
        "description": 0.35,
        "domain": 0.05
    }

    # Function to calculate similarity between two fields
    def calculate_similarity_score(text1, text2):
        if text1 and text2:
            embedding1 = model.encode(text1)
            embedding2 = model.encode(text2)
            return util.cos_sim(embedding1, embedding2).item()
        return 0.0

    # Calculate similarity for each component
    title_similarity = calculate_similarity_score(job_title, candidate_json.get("objective", "") + " " + " ".join([exp["title"] for exp in candidate_json["experience"]]))
    requirement_similarity = calculate_similarity_score(job_requirements, ", ".join(candidate_json["skills"] + candidate_json.get("technical_skills", [])))
    description_similarity = calculate_similarity_score(job_description, candidate_json.get("objective", "") + " " + " ".join([exp["description"] for exp in candidate_json["experience"]]) + " " + " ".join([project["description"] for project in candidate_json["projects"]]))
    domain_similarity = calculate_similarity_score(job_domain, ", ".join([edu["degree"] for edu in candidate_json["education"]]) + " " + " ".join([exp["title"] for exp in candidate_json["experience"]]))

    # Calculate the final score
    overall_similarity = (
        weights["title"] * title_similarity +
        weights["requirement"] * requirement_similarity +
        weights["description"] * description_similarity +
        weights["domain"] * domain_similarity
    )

    # Print individual scores and overall score
    print(f"Title Similarity: {title_similarity:.4f}")
    print(f"Requirement Similarity: {requirement_similarity:.4f}")
    print(f"Description Similarity: {description_similarity:.4f}")
    print(f"Domain Similarity: {domain_similarity:.4f}")
    print(f"Overall Similarity Score: {overall_similarity:.4f}")

    return overall_similarity,title_similarity,requirement_similarity,description_similarity,domain_similarity
