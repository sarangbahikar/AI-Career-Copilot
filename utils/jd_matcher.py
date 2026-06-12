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

        if skill in job_description:

            required_skills.append(
                skill
            )

    # ---------------------------------
    # Match with Resume Skills
    # ---------------------------------

    for skill in required_skills:

        if skill in resume_skills_lower:

            matched_skills.append(
                skill
            )

        else:

            missing_skills.append(
                skill
            )

    # ---------------------------------
    # Calculate Match Score
    # ---------------------------------

    if len(required_skills) > 0:

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

    suggestions = []

    for skill in missing_skills:

        suggestions.append(
            f"Consider learning {skill.title()}"
        )

    return {

        "score": score,

        "required": required_skills,

        "matched": matched_skills,

        "missing": missing_skills,

        "suggestions": suggestions
    }