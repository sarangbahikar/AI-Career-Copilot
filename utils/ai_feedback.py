import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

for m in genai.list_models():
    print(m.name)
model = genai.GenerativeModel(
    "gemini-2.0-flash"
)


def generate_feedback(resume_text):

    prompt = f"""
    You are an expert ATS reviewer,
    recruiter and career coach.

    Analyze the following resume.

    Provide:

    1. Resume Strengths
    2. Areas for Improvement
    3. ATS Optimization Suggestions
    4. Best Suitable Job Roles
    5. Overall Resume Rating out of 10

    Resume:

    {resume_text}
    """

    response = model.generate_content(
        prompt
    )

    return response.text