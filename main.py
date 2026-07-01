from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from services.resume_analyzer import (
    extract_skills,
    extract_education,
    extract_projects,
    calculate_resume_score,
    extract_name,
    extract_contact_info
)

from services.ai_feedback import generate_resume_feedback
from services.ats_checker import calculate_ats_score

app = FastAPI()

# ==============================
# CORS
# ==============================
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "https://prep-ai-frontend-nine.vercel.app",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class ResumeText(BaseModel):
    text: str


@app.get("/")
def home():
    return {"message": "PrepAI Backend is running 🚀"}


@app.post("/upload-resume/")
async def upload_resume(data: ResumeText):

    extracted_text = data.text

    candidate_name = extract_name(extracted_text)
    contact_info = extract_contact_info(extracted_text)
    skills = extract_skills(extracted_text)
    education = extract_education(extracted_text)
    projects = extract_projects(extracted_text)

    score = calculate_resume_score(
        extracted_text,
        skills,
        education,
        projects
    )

    ai_feedback = generate_resume_feedback(
        skills,
        education,
        projects,
        score["resume_score"]
    )

    ats_score = calculate_ats_score(
        extracted_text,
        skills,
        education,
        projects
    )

    return {
        "message": "Resume analyzed successfully",
        "candidate_name": candidate_name,
        "contact_info": contact_info,
        "filename": "Uploaded Resume",
        "skills": skills,
        "education": education,
        "projects": projects,
        "score": score,
        "ai_feedback": ai_feedback,
        "ats_score": ats_score
    }