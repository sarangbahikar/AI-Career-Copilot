def get_strengths(text, skills):

    strengths = []

    if len(skills) >= 8:
        strengths.append("Strong Technical Skill Set")

    if "project" in text.lower():
        strengths.append("Project Experience Present")

    if "internship" in text.lower():
        strengths.append("Internship Experience Present")

    if "machine learning" in text.lower():
        strengths.append("Machine Learning Knowledge")

    if "deep learning" in text.lower():
        strengths.append("Deep Learning Skills")

    return strengths