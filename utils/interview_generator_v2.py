def generate_interview_questions(skills, text):

    text = text.lower()

    technical = []
    project = []
    hr = []

    # -------------------
    # Technical Questions
    # -------------------

    if "machine learning" in skills:

        technical.extend([
            "Explain bias-variance tradeoff.",
            "What is overfitting and underfitting?",
            "Difference between bagging and boosting?"
        ])

    if "deep learning" in skills:

        technical.extend([
            "Explain backpropagation.",
            "Why use dropout layers?",
            "Difference between CNN and RNN?"
        ])

    if "nlp" in skills:

        technical.extend([
            "What are word embeddings?",
            "Explain tokenization.",
            "What is attention mechanism?"
        ])

    if "langchain" in skills:

        technical.extend([
            "What are chains in LangChain?",
            "How does LangChain memory work?"
        ])

    if "faiss" in skills:

        technical.extend([
            "Why use FAISS in RAG systems?",
            "What are vector embeddings?"
        ])

    # -------------------
    # Project Questions
    # -------------------

    if "pneumonia" in text:

        project.extend([
            "Explain your Pneumonia Detection project.",
            "Why did you choose DenseNet121?",
            "How did you handle class imbalance?"
        ])

    if "chatbot" in text:

        project.extend([
            "Explain your chatbot architecture.",
            "How did retrieval improve responses?",
            "What challenges did you face?"
        ])

    if "rag" in text:

        project.extend([
            "Explain the complete RAG pipeline.",
            "Why did you choose FAISS?",
            "How would you evaluate a RAG system?"
        ])

    # -------------------
    # HR Questions
    # -------------------

    hr.extend([
        "Tell me about yourself.",
        "Why should we hire you?",
        "Describe a challenging project.",
        "Where do you see yourself in 5 years?",
        "What are your strengths and weaknesses?"
    ])

    return {
        "technical": technical,
        "project": project,
        "hr": hr
    }