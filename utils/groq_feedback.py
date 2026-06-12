import os

from groq import Groq
from dotenv import load_dotenv

load_dotenv()
print("GROQ KEY =", os.getenv("GROQ_API_KEY"))
client = Groq(
    api_key=os.getenv(
        "GROQ_API_KEY"
    )
)


def generate_feedback(text):

    prompt = f"""
You are an expert ATS recruiter.

Analyze this resume and provide:

1. Strengths
2. Weaknesses
3. Recommendations

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