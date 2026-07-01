import re


# ==========================
# SKILLS EXTRACTION
# ==========================
def extract_skills(text):
    skills_list = [
        "Python",
        "Java",
        "C",
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
        "Socket.IO",
        "HTML",
        "CSS",
        "Node.js",
        "MongoDB"
    ]

    found_skills = []

    lower_text = text.lower()

    for skill in skills_list:
        if skill.lower() in lower_text:
            found_skills.append(skill)

    return sorted(list(set(found_skills)))


# ==========================
# EDUCATION EXTRACTION
# ==========================
def extract_education(text):

    keywords = [
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

    found = []

    lower_text = text.lower()

    for keyword in keywords:
        if keyword.lower() in lower_text:
            found.append(keyword)

    return sorted(list(set(found)))


# ==========================
# PROJECT EXTRACTION
# ==========================
def extract_projects(text):

    patterns = [
        r"([A-Z][A-Za-z ]+ App)",
        r"([A-Z][A-Za-z ]+ Application)",
        r"([A-Z][A-Za-z ]+ Tracker)",
        r"([A-Z][A-Za-z ]+ Chat)",
    ]

    projects = []

    for pattern in patterns:
        matches = re.findall(pattern, text)

        for match in matches:
            match = match.strip()

            if len(match) > 3:
                projects.append(match)

    return sorted(list(set(projects)))


# ==========================
# RESUME SCORE
# ==========================
def calculate_resume_score(text, skills, education, projects):

    score = 0

    feedback = []

    if len(skills) >= 5:
        score += 25
    else:
        feedback.append("Add more technical skills.")

    if education:
        score += 20
    else:
        feedback.append("Education section is missing.")

    if len(projects) >= 2:
        score += 20
    else:
        feedback.append("Add at least two projects.")

    if re.search(r"(experience|internship|work)", text, re.IGNORECASE):
        score += 20
    else:
        feedback.append("Add internship or work experience.")

    if re.search(r"(github|linkedin)", text, re.IGNORECASE):
        score += 15
    else:
        feedback.append("Add GitHub and LinkedIn links.")

    return {
        "resume_score": score,
        "feedback": feedback
    }


# ==========================
# NAME EXTRACTION
# ==========================
def extract_name(text):

    text = (
        text.replace("©", " ")
        .replace("«", " ")
        .replace("»", " ")
        .replace("Cy", " ")
        .replace("ae", " ")
    )

    text = re.sub(r"\s+", " ", text)

    stop_words = {
        "Student",
        "Developer",
        "Engineer",
        "Intern",
        "Education",
        "Projects",
        "Experience",
        "Technical",
        "Skills",
        "Languages",
        "Backend",
        "Frontend",
        "University",
        "College"
    }

    words = text.split()

    for i in range(len(words)):

        candidate = []

        for j in range(i, min(i + 3, len(words))):

            word = words[j]

            if word in stop_words:
                break

            if re.fullmatch(r"[A-Z][a-z]+", word):
                candidate.append(word)
            else:
                break

        if len(candidate) >= 2:
            return " ".join(candidate)

    return "Name not detected"


# ==========================
# CONTACT EXTRACTION
# ==========================
def extract_contact_info(text):

    contact_info = {
        "email": None,
        "phone": None,
        "linkedin": None,
        "github": None
    }

    email = re.search(
        r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}",
        text
    )

    if email:
        contact_info["email"] = email.group()

    phone = re.search(
        r"(?:\+91[- ]?)?[6-9]\d{9}",
        text
    )

    if phone:
        contact_info["phone"] = phone.group()

    linkedin = re.search(
        r"(https?://)?(www\.)?linkedin\.com/[^\s]+",
        text,
        re.IGNORECASE
    )

    if linkedin:
        contact_info["linkedin"] = linkedin.group()
    elif "linkedin" in text.lower():
        contact_info["linkedin"] = "Detected"

    github = re.search(
        r"(https?://)?(www\.)?github\.com/[^\s]+",
        text,
        re.IGNORECASE
    )

    if github:
        contact_info["github"] = github.group()
    elif "github" in text.lower():
        contact_info["github"] = "Detected"

    return contact_info