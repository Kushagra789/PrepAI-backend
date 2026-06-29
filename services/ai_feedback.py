def generate_resume_feedback(
    skills,
    education,
    projects,
    score
):

    feedback = []


    # Skills feedback
    if len(skills) < 5:
        feedback.append(
            "Add more technical skills relevant to your target job."
        )
    else:
        feedback.append(
            "Your technical skills section is good."
        )


    # Project feedback
    if len(projects) < 3:
        feedback.append(
            "Add more projects to demonstrate practical experience."
        )
    else:
        feedback.append(
            "Your projects section shows practical development experience."
        )


    # Education feedback
    if len(education) == 0:
        feedback.append(
            "Add your educational background clearly."
        )


    # Score feedback
    if score < 70:
        feedback.append(
            "Improve your resume by adding stronger projects and experience."
        )
    else:
        feedback.append(
            "Your resume structure is strong."
        )


    return feedback