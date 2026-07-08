
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
        "content": "You are an expert English text correction assistant. Follow the examples exactly."
    },

    {
        "role": "user",
        "content": "Input: i luv pyhton"
    },
    {
        "role": "assistant",
        "content": "Output: I love Python."
    },

    {
        "role": "user",
        "content": "Input: hello    wrld"
    },
    {
        "role": "assistant",
        "content": "Output: Hello world."
    },

    {
        "role": "user",
        "content": "Input: im lerning ai"
    },
    {
        "role": "assistant",
        "content": "Output: I'm learning AI."
    },

   {
    "role": "user",
    "content": user_input
}
]
)
# Print the AI's response
print(response.choices[0].message.content)
