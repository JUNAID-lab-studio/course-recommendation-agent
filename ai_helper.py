import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

def generate_learning_path(student):
    prompt = f"""
    Student Details:
    Name: {student['name']}
    Education: {student['education']}
    Skills: {', '.join(student['skills'])}
    Career Goal: {student['goal']}

    Recommend:
    1. 5 suitable courses
    2. Reason for each course
    3. A step-by-step learning roadmap.
    """

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content
