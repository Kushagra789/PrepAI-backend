def match_resume_with_job(resume_skills, job_description):

    job_skills_list = [
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
        "Git",
        "GitHub",
        "Redis",
        "Socket.IO"
    ]


    required_skills = []

    for skill in job_skills_list:
        if skill.lower() in job_description.lower():
            required_skills.append(skill)


    matched_skills = []

    for skill in resume_skills:
        if skill in required_skills:
            matched_skills.append(skill)


    missing_skills = []

    for skill in required_skills:
        if skill not in resume_skills:
            missing_skills.append(skill)


    if len(required_skills) > 0:
        match_percentage = int(
            (len(matched_skills) / len(required_skills)) * 100
        )
    else:
        match_percentage = 0


    return {
        "match_percentage": match_percentage,
        "matched_skills": matched_skills,
        "missing_skills": missing_skills
    }