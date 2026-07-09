import os
import time
from dotenv import load_dotenv
from openai import OpenAI
from colorama import Fore, Style, init
from config import SYSTEM_PROMPT

init(autoreset=True)

load_dotenv()

client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)

print("=" * 60)
print(Fore.CYAN + "Visionerds AI Chatbot")
print(Fore.CYAN + "Created by: Muhammad Tayyab Malik")
print(Fore.GREEN + "Model : Llama 3.3 70B")
print(Fore.GREEN + "Provider : Groq")
print(Fore.GREEN + "Status : Online ✅")
print("=" * 60)

print("\nAvailable Commands")
print("--------------------------")
print("clear - Clear terminal")
print("exit  - Quit chatbot\n")

while True:

    user_input = input(Fore.YELLOW + "You: ").strip()

    # Empty message
    if not user_input:
        print(Fore.RED + "⚠ Please enter a message.\n")
        continue

    # Exit
    if user_input.lower() == "exit":
        print(Fore.GREEN + "\nGoodbye! 👋")
        break

   

    # Clear screen
    if user_input.lower() == "clear":
        os.system("cls" if os.name == "nt" else "clear")
        continue

    # Greeting (No API call)
    greetings = ["hi", "hello", "hey"]

    if user_input.lower() in greetings:
        print(
            Fore.CYAN +
            "\nAI: Hello! I am your AI Prompt Engineering Mentor."
            "\nAsk me anything about AI, Python, Machine Learning, Git, Prompt Engineering or Programming.\n"
        )
        continue

    try:

        start = time.time()

        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            temperature=0.3,
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

        end = time.time()

        print(Fore.CYAN + "\nAI:")
        print(response.choices[0].message.content)

        print(
            Fore.GREEN +
            f"\n⏱ Response Time : {end-start:.2f} seconds\n"
        )

    except Exception as e:

        print(Fore.RED + "\n❌ Unable to contact the AI.")
        print(Fore.RED + "Please check your internet connection or API key.")

        print(Fore.YELLOW + f"\n[DEBUG] {e}\n")