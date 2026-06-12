skills_db = [
    "python",
    "sql",
    "machine learning",
    "deep learning",
    "nlp",
    "tensorflow",
    "pytorch",
    "streamlit",
    "docker",
    "aws",
    "git",
    "pandas",
    "numpy"
]

def extract_skills(text):
    text = text.lower()

    found_skills = []

    for skill in skills_db:
        if skill in text:
            found_skills.append(skill)

    return list(set(found_skills))