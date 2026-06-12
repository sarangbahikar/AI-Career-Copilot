def get_weaknesses(text):

    weaknesses = []

    text = text.lower()

    if "certification" not in text and "certificate" not in text:
        weaknesses.append(
            "No Certifications Found"
        )

    if "project" not in text:
        weaknesses.append(
            "No Projects Found"
        )

    if "internship" not in text and "experience" not in text:
        weaknesses.append(
            "No Experience Found"
        )

    if "portfolio" not in text:
        weaknesses.append(
            "Portfolio Website Missing"
        )

    return weaknesses