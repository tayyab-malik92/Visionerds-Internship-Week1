import os
from dotenv import load_dotenv
from openai import OpenAI
from config import SYSTEM_PROMPT

# Load variables from the .env file
load_dotenv()

# Create the client
client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)

print("🤖 AI Chatbot Started made by TAYYAB!")
print("Type 'exit' to quit.\n")

while True:
    user_input = input("You: ")

    if not user_input.strip():
        continue

    if user_input.lower() == "exit":
        print("Goodbye! 👋")
        break

    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            temperature=0.7,
            messages=[
                {
                    "role": "system",
                    "content": SYSTEM_PROMPT
                },
                {
                    "role": "user",
                    "content": user_input
                }
            ]
        )

        print("\nAI:", response.choices[0].message.content)

    except Exception as e:
        print("\n❌ Unable to contact the AI.")
        print("Please check your internet connection or API key and try again.")

        # Developer log (for debugging)
        print(f"[DEBUG]: {e}")