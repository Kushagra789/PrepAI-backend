def calculate_ats_score(
    text,
    skills,
    education,
    projects
):

    ats_score = 0

    details = {}


    # Keyword score
    if len(skills) >= 5:
        keyword_score = 30
    else:
        keyword_score = len(skills) * 5


    ats_score += keyword_score

    details["keyword_match"] = keyword_score



    # Education score
    if len(education) > 0:
        education_score = 20
    else:
        education_score = 0


    ats_score += education_score

    details["education_score"] = education_score



    # Project score
    if len(projects) >= 2:
        project_score = 25
    else:
        project_score = 10


    ats_score += project_score

    details["project_score"] = project_score



    # Experience score
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
        experience_score = 25
    else:
        experience_score = 10


    ats_score += experience_score

    details["experience_score"] = experience_score



    return {
        "ATS_score": ats_score,
        "details": details
    }