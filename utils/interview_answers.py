from utils.groq_feedback import client


def generate_answer(question):

    prompt = f"""
You are a senior AI interviewer.

Provide a concise interview answer
for the following question.

Question:
{question}

Keep the answer:
- Professional
- Interview ready
- Around 100-150 words
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