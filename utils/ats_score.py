def calculate_ats_score(text, skills):

    text = text.lower()

    breakdown = {
        "skills": 0,
        "education": 0,
        "projects": 0,
        "experience": 0,
        "certifications": 0
    }

    # Skills (30)

    breakdown["skills"] = min(
        len(skills) * 3,
        30
    )

    # Education (20)

    education_keywords = [
        "bachelor",
        "master",
        "degree",
        "university",
        "college"
    ]

    if any(
        word in text
        for word in education_keywords
    ):
        breakdown["education"] = 20

    # Projects (20)

    if "project" in text:
        breakdown["projects"] = 20

    # Experience (15)

    if (
        "experience" in text or
        "internship" in text
    ):
        breakdown["experience"] = 15

    # Certifications (15)

    if (
        "certification" in text or
        "certificate" in text
    ):
        breakdown["certifications"] = 15

    total = sum(
        breakdown.values()
    )

    breakdown["total"] = min(
        total,
        100
    )

    return breakdown