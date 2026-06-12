target_skills = [
    "python",
    "sql",
    "machine learning",
    "deep learning",
    "aws",
    "docker",
    "git",
    "streamlit"
]

def find_missing_skills(skills):

    missing = []

    for skill in target_skills:

        if skill not in skills:
            missing.append(skill)

    return missing