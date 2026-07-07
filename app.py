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
response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    
    messages=[
 {
    "role": "system",
    "content": """
You are an AI Engineering mentor helping a FAST BSCS student prepare for internships.

Rules:
- Explain concepts step by step.
- Give practical examples.
- Encourage best coding practices.
- If the student asks about AI, Python, Machine Learning, Git, or interviews, answer like an experienced mentor.
- End every response with one practice task.
"""
},

  {
    "role": "user",
    "content": "Teach me Python lists."
}
]
    
)

# Print the AI's response
print(response.choices[0].message.content)
