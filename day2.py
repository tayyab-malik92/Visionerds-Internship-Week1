import os
from dotenv import load_dotenv
from openai import OpenAI

# Load variables from the .env file
load_dotenv()

# Create the client
client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)

# Send a message to the model
user_input = input("Enter your sentence: ")

response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    temperature=0,
    messages=[
        {
            "role": "system",
            "content": """
You are an AI Engineering mentor.

Rules:
- Explain step by step.
- Never skip beginner concepts.
- Use simple English.
- Give one real-world example.
- End with one practice exercise.
"""
        },
        {
            "role": "user",
            "content": user_input
        }
    ]
)

print(response.choices[0].message.content)