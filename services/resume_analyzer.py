import re


def extract_skills(text):
    skills_list = [
        "Python",
        "Java",
        "C++",
        "JavaScript",
        "React",
        "FastAPI",
        "Django",
        "AWS",
        "Docker",
        "Kubernetes",
        "Machine Learning",
        "SQL",
        "GitHub",
        "Git",
        "Redis",
        "Socket.IO"
    ]

    found_skills = []

    for skill in skills_list:
        if skill.lower() in text.lower():
            found_skills.append(skill)

    return found_skills


def extract_education(text):
    education_keywords = [
        "B.Tech",
        "B.E",
        "Bachelor",
        "Master",
        "M.Tech",
        "MCA",
        "Computer Science",
        "Engineering",
        "University",
        "College"
    ]

    found_education = []

    for keyword in education_keywords:
        if keyword.lower() in text.lower():
            found_education.append(keyword)

    return found_education


def extract_projects(text):
    ignored_words = [
        "projects",
        "project",
        "system design",
        "backend",
        "web technologies"
    ]

    found_projects = []

    lines = text.split("\n")

    for line in lines:
        clean_line = line.strip()

        if len(clean_line) < 3:
            continue

        if clean_line.lower() in ignored_words:
            continue

        if (
            "app" in clean_line.lower()
            or "application" in clean_line.lower()
            or "chat" in clean_line.lower()
            or "tracker" in clean_line.lower()
            or "smart" in clean_line.lower()
        ):
            found_projects.append(clean_line)

    return found_projects


def calculate_resume_score(text, skills, education, projects):
    score = 0
    feedback = []

    if len(skills) >= 3:
        score += 25
    else:
        feedback.append("Add more technical skills")

    if len(education) > 0:
        score += 25
    else:
        feedback.append("Add education details")

    if len(projects) >= 2:
        score += 25
    else:
        feedback.append("Add more projects")

    experience_keywords = [
        "experience",
        "internship",
        "work",
        "job"
    ]

    has_experience = False

    for keyword in experience_keywords:
        if keyword.lower() in text.lower():
            has_experience = True
            break

    if has_experience:
        score += 25
    else:
        feedback.append("Add internships or work experience")

    return {
        "resume_score": score,
        "feedback": feedback
    }


def extract_name(text):
    lines = text.split("\n")

    ignored_words = [
        "student",
        "resume",
        "curriculum vitae",
        "education",
        "skills",
        "projects",
        "experience"
    ]

    for line in lines:
        clean_line = line.strip()

        if len(clean_line) == 0:
            continue

        if clean_line.lower() in ignored_words:
            continue

        words = clean_line.split()

        if 1 < len(words) <= 4:
            return clean_line

    return "Name not detected"


def extract_contact_info(text):
    contact_info = {
        "email": None,
        "phone": None,
        "linkedin": None,
        "github": None
    }

    # Email extraction
    email_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

    email_match = re.search(email_pattern, text)

    if email_match:
        contact_info["email"] = email_match.group()


    # Phone extraction
    phone_pattern = r"\b\d{10}\b"

    phone_match = re.search(phone_pattern, text)

    if phone_match:
        contact_info["phone"] = phone_match.group()


    # LinkedIn detection
    if "linkedin" in text.lower():
        contact_info["linkedin"] = "LinkedIn profile detected"


    # GitHub detection
    if "github" in text.lower():
        contact_info["github"] = "GitHub profile detected"


    return contact_info