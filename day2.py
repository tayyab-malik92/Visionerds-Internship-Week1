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
You are a data extraction assistant.

Rules:
- Return ONLY valid JSON.
- No explanation.
- Extract the person's name, city, and intent if available.
"""
        },
        {
            "role": "user",
            "content": user_input
        }
    ]
)

print(response.choices[0].message.content)