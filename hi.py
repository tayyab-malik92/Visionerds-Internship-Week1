import os
import json
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables
load_dotenv()

# Create Groq Client
client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)

# User Input
user_input = input("Enter your sentence: ")

response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    temperature=0,
    messages=[
        {
            "role": "system",
            "content": """
You are an Information Extraction AI.

Extract information from the user's sentence.

Return ONLY valid JSON.

JSON Format:

{
    "name":"",
    "city":"",
    "interest":""
}

Rules:
- Do not explain anything.
- Do not write markdown.
- Return JSON only.
- If any field is missing, write null.
"""
        },
        {
            "role": "user",
            "content": user_input
        }
    ]
)

# Get JSON string from AI
json_text = response.choices[0].message.content

print("\nRaw JSON:\n")
print(json_text)

# Convert JSON string to Python Dictionary
data = json.loads(json_text)

print("\nExtracted Information\n")

print("Name     :", data["name"])
print("City     :", data["city"])
print("Interest :", data["interest"])

# Save JSON
with open("person.json", "w", encoding="utf-8") as file:
    json.dump(data, file, indent=4)

print("\nJSON saved to person.json")