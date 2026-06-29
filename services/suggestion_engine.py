def generate_suggestions(missing_skills):

    suggestions = []


    skill_suggestions = {

        "Python":
        "Learn Python and add Python-based projects to your resume.",

        "AWS":
        "Learn AWS fundamentals and add cloud deployment experience.",

        "Docker":
        "Add containerization projects using Docker.",

        "Kubernetes":
        "Learn Kubernetes for container orchestration.",

        "Machine Learning":
        "Add machine learning projects using Python libraries.",

        "React":
        "Build frontend projects using React.",

        "SQL":
        "Improve database skills and add SQL-based projects.",

        "FastAPI":
        "Build backend APIs using FastAPI."
    }


    for skill in missing_skills:

        if skill in skill_suggestions:
            suggestions.append(
                skill_suggestions[skill]
            )

        else:
            suggestions.append(
                f"Consider learning {skill} and adding related projects."
            )


    if len(suggestions) == 0:
        suggestions.append(
            "Your resume matches the job requirements well."
        )


    return suggestions