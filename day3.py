import os
import re
import time
from dotenv import load_dotenv
from openai import OpenAI
from colorama import Fore, init
from config import SYSTEM_PROMPT

# -----------------------------
# Initialization
# -----------------------------

init(autoreset=True)
load_dotenv()

client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)

# Greetings handled locally
GREETINGS = {
    "hi", "hello", "hey", "assalamualaikum", "salam"
}

# Casual conversation handled locally
CASUAL_INPUTS = {
    "ok", "okay", "fine", "good",
    "im ok", "i am ok", "i'm ok",
    "thanks", "thank you",
    "bye",
    "good morning",
    "good afternoon",
    "good evening",
    "how are you",
    "whats up",
    "what's up",
    "sup"
}


# -----------------------------
# UI Functions
# -----------------------------

def show_banner():
    print(Fore.CYAN + "=" * 65)
    print(Fore.CYAN + "              Visionerds AI Chatbot")
    print(Fore.CYAN + "                  Version 1.1")
    print(Fore.WHITE + "       Developed by: Muhammad Tayyab Malik")
    print(Fore.GREEN + "-" * 65)
    print(Fore.GREEN + " Model    : Llama 3.3 70B")
    print(Fore.GREEN + " Provider : Groq")
    print(Fore.GREEN + " Status   :  Online")
    print(Fore.CYAN + "=" * 65)

    print(Fore.YELLOW + "\nAvailable Commands")
    print(Fore.YELLOW + "-" * 25)
    print(" clear  → Clear terminal")
    print(" about  → Chatbot information")
    print(" exit   → Quit chatbot")

    print(
        Fore.CYAN +
        "\n💡 Ask anything about AI, Python, Machine Learning,\n"
        "   Prompt Engineering, Git or Programming.\n"
    )


def show_about():
    print(Fore.CYAN)
    print("=" * 45)
    print("Visionerds AI Chatbot")
    print("Version   : 1.1")
    print("Developer : Muhammad Tayyab Malik")
    print("Model     : Llama 3.3 70B")
    print("Provider  : Groq")
    print("=" * 45)
    print()


# -----------------------------
# Validation
# -----------------------------

def is_valid_query(text):

    text = text.strip().lower()

    if not text:
        return False

    if len(text) < 4:
        return False

    if text.isdigit():
        return False

    if re.fullmatch(r'[^a-zA-Z0-9]+', text):
        return False

    if re.fullmatch(r'(.)\1{3,}', text):
        return False

    return True


# -----------------------------
# AI Function
# -----------------------------

def get_ai_response(user_input):

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

    print(Fore.CYAN)
    print("─" * 65)
    print(" AI Response")
    print("─" * 65)

    print(response.choices[0].message.content)

    print("─" * 65)

    print(Fore.GREEN + f"\n Response Time: {end-start:.2f} sec\n")


# -----------------------------
# Main
# -----------------------------

def main():

    show_banner()

    while True:

        user_input = input(Fore.YELLOW + "You: ").strip()

        if user_input.lower() == "exit":
            print(Fore.GREEN)
            print("\nThank you for using Visionerds AI Chatbot.")
            print("Happy Learning!")
            print("Goodbye! 👋")
            break

        if user_input.lower() == "clear":
            os.system("cls" if os.name == "nt" else "clear")
            show_banner()
            continue

        if user_input.lower() == "about":
            show_about()
            continue

        if not user_input:
            print(Fore.RED)
            print(" Input cannot be empty.")
            print("Please ask a question related to AI or Programming.\n")
            continue

        if not is_valid_query(user_input):
            print(Fore.RED)
            print(" Please enter a meaningful AI or programming-related question.\n")
            continue

        if user_input.lower() in GREETINGS:
            print(Fore.CYAN)
            print("Hello!")
            print("I am your AI Prompt Engineering Mentor.")
            print("How can I help you today?\n")
            continue

        if user_input.lower() in CASUAL_INPUTS:
            print(Fore.CYAN)
            print("I am an AI Prompt Engineering Mentor.")
            print("Please ask a question related to AI, Python,")
            print("Machine Learning, Prompt Engineering, Git or Programming.\n")
            continue

        try:
            get_ai_response(user_input)

        except Exception as e:

            print(Fore.RED)
            print("=" * 50)
            print("❌ ERROR")
            print("=" * 50)
            print("Unable to contact the AI.")
            print("Check your internet connection or API key.")
            print("=" * 50)

            print(Fore.YELLOW + f"\n[DEBUG]: {e}\n")


if __name__ == "__main__":
    main()