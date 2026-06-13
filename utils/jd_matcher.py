import re


def calculate_jd_match(
    resume_skills,
    job_description
):

    job_description = job_description.lower()

    resume_skills_lower = [
        skill.lower().strip()
        for skill in resume_skills
    ]

    common_skills = [

        # Programming

        "python",
        "sql",
        "c",
        "java",

        # Data Science

        "numpy",
        "pandas",
        "matplotlib",
        "seaborn",

        # Machine Learning

        "machine learning",
        "deep learning",
        "tensorflow",
        "keras",
        "pytorch",
        "scikit-learn",
        "xgboost",

        # NLP

        "nlp",
        "nltk",
        "hugging face",

        # GenAI

        "langchain",
        "rag",
        "faiss",
        "vector database",
        "openai api",

        # Backend

        "fastapi",
        "flask",

        # Databases

        "mongodb",
        "mysql",
        "postgresql",
        "redis",

        # Cloud

        "aws",
        "docker",
        "kubernetes",

        # Computer Vision

        "opencv",

        # App Development

        "streamlit"
    ]

    required_skills = []
    matched_skills = []
    missing_skills = []

    # ---------------------------------
    # Extract required skills from JD
    # ---------------------------------

    for skill in common_skills:

        if len(skill.split()) == 1:

            words = re.findall(
                r"\b\w+\b",
                job_description
            )

            if skill.lower() in words:

                required_skills.append(
                    skill
                )

        else:

            if skill.lower() in job_description:

                required_skills.append(
                    skill
                )

    # ---------------------------------
    # Match with Resume Skills
    # ---------------------------------

    for skill in required_skills:

        if skill.lower() in resume_skills_lower:

            matched_skills.append(
                skill
            )

        else:

            missing_skills.append(
                skill
            )

    # ---------------------------------
    # Match Score
    # ---------------------------------

    if required_skills:

        score = int(
            (
                len(matched_skills)
                /
                len(required_skills)
            ) * 100
        )

    else:

        score = 0

    # ---------------------------------
    # Suggestions
    # ---------------------------------

    suggestions = [

        f"Consider learning {skill.title()}"
        for skill in missing_skills
    ]

    return {

        "score": score,

        "required": required_skills,

        "matched": matched_skills,

        "missing": missing_skills,

        "suggestions": suggestions
    }