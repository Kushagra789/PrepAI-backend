from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware

import os
import shutil

from utils.pdf_utils import extract_text_from_pdf

from services.resume_analyzer import (
    extract_skills,
    extract_education,
    extract_projects,
    calculate_resume_score,
    extract_name,
    extract_contact_info
)

from services.job_matcher import match_resume_with_job
from services.suggestion_engine import generate_suggestions
from services.ai_feedback import generate_resume_feedback
from services.ats_checker import calculate_ats_score


app = FastAPI()

# ==============================
# 🚀 FINAL CORS FIX (PRODUCTION SAFE)
# ==============================
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://prep-ai-frontend-nine.vercel.app"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)


@app.get("/")
def home():
    return {"message": "PrepAI is running 🚀"}


@app.post("/upload-resume/")
async def upload_resume(file: UploadFile = File(...)):

    file_path = os.path.join(UPLOAD_DIR, file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    extracted_text = extract_text_from_pdf(file_path)

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
        "filename": file.filename,
        "skills": skills,
        "education": education,
        "projects": projects,
        "score": score,
        "ai_feedback": ai_feedback,
        "ats_score": ats_score
    }