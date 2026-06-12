def calculate_ats_score(text, skills):

    score = 0

    text = text.lower()

    # Skills
    score += min(len(skills) * 3, 30)

    # Education
    education_keywords = [
        "bachelor",
        "master",
        "degree",
        "university",
        "college"
    ]

    if any(word in text for word in education_keywords):
        score += 20

    # Projects
    if "project" in text:
        score += 20

    # Certifications
    if "certification" in text or "certificate" in text:
        score += 15

    # Experience
    if "experience" in text or "internship" in text:
        score += 15

    return min(score, 100)