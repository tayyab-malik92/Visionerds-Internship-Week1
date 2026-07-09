import os
import re
import time
from dotenv import load_dotenv
from openai import OpenAI
from colorama import Fore, init
from config import SYSTEM_PROMPT

# Initialize Colorama
init(autoreset=True)

# Load environment variables
load_dotenv()

# Create Groq client
client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)

# ------------------------------
# Chatbot Banner
# ------------------------------

print("=" * 60)
print(Fore.CYAN + "🤖 Visionerds AI Chatbot")
print(Fore.CYAN + "Created by: Muhammad Tayyab Malik")
print(Fore.GREEN + "Model    : Llama 3.3 70B")
print(Fore.GREEN + "Provider : Groq")
print(Fore.GREEN + "Status   : Online ✅")
print("=" * 60)

print("\nAvailable Commands")
print("--------------------------")
print("clear - Clear terminal")
print("exit  - Quit chatbot\n")

# ------------------------------
# Helper Functions
# ------------------------------

def is_valid_query(text):
    """
    Validate obvious invalid inputs before calling the API.
    """
    text = text.strip().lower()

    # Empty
    if not text:
        return False

    # Very short input
    if len(text) < 4:
        return False

    # Only numbers
    if text.isdigit():
        return False

    # Only symbols
    if re.fullmatch(r'[^a-zA-Z0-9]+', text):
        return False

    # Same character repeated (aaaaaa, $$$$$)
    if re.fullmatch(r'(.)\1{3,}', text):
        return False

    return True


# Greetings handled locally (No API call)
greetings = {
    "hi",
    "hello",
    "hey",
    "assalamualaikum",
    "salam"
}

# Casual messages handled locally (No API call)
casual_inputs = {
    "ok",
    "okay",
    "fine",
    "good",
    "im ok",
    "i am ok",
    "i'm ok",
    "thanks",
    "thank you",
    "bye",
    "good morning",
    "good afternoon",
    "good evening",
    "how are you",
    "whats up",
    "what's up",
    "sup"
}

# ------------------------------
# Chat Loop
# ------------------------------

while True:

    user_input = input(Fore.YELLOW + "You: ").strip()

    # Exit
    if user_input.lower() == "exit":
        print(Fore.GREEN + "\nGoodbye! 👋")
        break

    # Clear Screen
    if user_input.lower() == "clear":
        os.system("cls" if os.name == "nt" else "clear")
        continue

    # Empty input
    if not user_input:
        print(Fore.RED + "\n⚠ Please enter a message.\n")
        continue

    # Invalid input
    if not is_valid_query(user_input):
        print(Fore.RED + "\nAI:")
        print("⚠ Please enter a meaningful AI or programming-related question.\n")
        continue

    # Greeting
    if user_input.lower() in greetings:
        print(Fore.CYAN + "\nAI:")
        print("Hello! I am your AI Prompt Engineering Mentor.")
        print("Ask me anything related to AI, Python, Machine Learning, Prompt Engineering, Git, or Programming.\n")
        continue

    # Casual conversation
    if user_input.lower() in casual_inputs:
        print(Fore.CYAN + "\nAI:")
        print("I am an AI Prompt Engineering Mentor.")
        print("Please ask a question related to AI, Python, Machine Learning, Prompt Engineering, Git, or Programming.\n")
        continue

    # --------------------------
    # API Call
    # --------------------------

    try:

        start = time.time()

        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            temperature=0.2,
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
            f"\n⏱ Response Time: {end - start:.2f} seconds\n"
        )

    except Exception as e:

        print(Fore.RED + "\n❌ Unable to contact the AI.")
        print(Fore.RED + "Please check your internet connection or API key.")

        # Developer log
        print(Fore.YELLOW + f"\n[DEBUG]: {e}\n")