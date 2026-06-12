def generate_interview_questions(skills):

    questions = []

    if "python" in skills:

        questions.extend([
            "What are Python decorators?",
            "Difference between list and tuple?",
            "Explain generators in Python."
        ])

    if "sql" in skills:

        questions.extend([
            "What is a JOIN?",
            "Difference between WHERE and HAVING?",
            "Explain indexing in SQL."
        ])

    if "machine learning" in skills:

        questions.extend([
            "What is overfitting?",
            "What is bias-variance tradeoff?",
            "Difference between bagging and boosting?"
        ])

    if "deep learning" in skills:

        questions.extend([
            "What is backpropagation?",
            "Difference between CNN and RNN?",
            "Why use dropout?"
        ])

    if "nlp" in skills:

        questions.extend([
            "What is tokenization?",
            "What are embeddings?",
            "What is attention mechanism?"
        ])

    return list(set(questions))