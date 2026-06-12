def recommend_roles(skills):

    skills = [skill.lower() for skill in skills]

    roles = []

    # AI / ML

    if (
        "machine learning" in skills or
        "deep learning" in skills or
        "tensorflow" in skills or
        "pytorch" in skills
    ):
        roles.append(
            "Machine Learning Engineer"
        )

    # Data Science

    if (
        "python" in skills and
        "pandas" in skills and
        "numpy" in skills
    ):
        roles.append(
            "Data Scientist"
        )

    # NLP

    if (
        "nlp" in skills or
        "langchain" in skills
    ):
        roles.append(
            "NLP Engineer"
        )

    # GenAI

    if (
        "langchain" in skills and
        "aws" in skills
    ):
        roles.append(
            "GenAI Engineer"
        )

    # Data Analyst

    if (
        "sql" in skills and
        "pandas" in skills
    ):
        roles.append(
            "Data Analyst"
        )

    # AI Engineer

    if (
        "python" in skills and
        "machine learning" in skills
    ):
        roles.append(
            "AI Engineer"
        )

    return list(set(roles))