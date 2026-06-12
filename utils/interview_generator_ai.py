from utils.groq_feedback import client


def generate_interview_questions_ai(text):

    prompt = f"""
You are a Senior Technical Interviewer.

Analyze this resume and generate:

1. 5 Technical Questions
2. 5 Project Questions
3. 5 HR Questions

Return ONLY in this format:

TECHNICAL:
- Question
- Question

PROJECT:
- Question
- Question

HR:
- Question
- Question

Resume:

{text[:6000]}
"""

    response = client.chat.completions.create(

        model="llama-3.3-70b-versatile",

        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]

    )

    return response.choices[0].message.content