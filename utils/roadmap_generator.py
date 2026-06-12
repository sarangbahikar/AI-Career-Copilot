def generate_roadmap(roles):

    roadmap = []

    if "AI Engineer" in roles:

        roadmap = [

            "Month 1: Advanced Python and SQL",

            "Month 2: Statistics and Machine Learning",

            "Month 3: Deep Learning with TensorFlow/PyTorch",

            "Month 4: NLP, LangChain and RAG",

            "Month 5: Docker, FastAPI and AWS",

            "Month 6: Build and Deploy an AI Project"
        ]

    elif "Machine Learning Engineer" in roles:

        roadmap = [

            "Month 1: Python, NumPy and Pandas",

            "Month 2: Machine Learning Algorithms",

            "Month 3: Model Evaluation and Feature Engineering",

            "Month 4: Deep Learning",

            "Month 5: MLOps and Deployment",

            "Month 6: Production ML Project"
        ]

    elif "Data Scientist" in roles:

        roadmap = [

            "Month 1: Python and SQL",

            "Month 2: Statistics and Probability",

            "Month 3: Data Analysis with Pandas",

            "Month 4: Machine Learning",

            "Month 5: Data Visualization",

            "Month 6: End-to-End Data Science Project"
        ]

    else:

        roadmap = [

            "Month 1: Python Fundamentals",

            "Month 2: SQL",

            "Month 3: Data Analysis",

            "Month 4: Machine Learning",

            "Month 5: Projects",

            "Month 6: Deployment"
        ]

    return roadmap