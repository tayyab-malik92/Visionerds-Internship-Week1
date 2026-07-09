# Day 3 - Interactive AI Chatbot Findings

## Interactive Chat Loop
- Built a continuous chatbot using `while True`.
- Added an `exit` command to close the chatbot gracefully.

## Dynamic User Input
- Replaced hardcoded prompts with `input()`.
- Enabled users to ask any AI or programming-related question.

## Strong AI Mentor Persona
- Defined the chatbot's behavior using a dedicated `SYSTEM_PROMPT`.
- Configured the chatbot to act strictly as an AI Prompt Engineering Mentor.
- Restricted the chatbot from engaging in unrelated casual conversations.

## Configuration Management
- Moved the system prompt to `config.py`.
- Improved project organization by separating configuration from application logic.

## User Experience Enhancements
- Added empty input validation with a friendly warning message.
- Added a startup banner displaying chatbot information.
- Added built-in commands:
  - `clear` – Clears the terminal.
  - `exit` – Exits the chatbot.
- Added greeting detection (`hi`, `hello`, `hey`) without making an API call.
- Displayed AI response time for every query.

## Error Handling
- Used `try` and `except` to prevent the chatbot from crashing.
- Displayed user-friendly error messages.
- Logged technical errors for debugging purposes.

## Project Structure
- Organized the project into separate files:
  - `day3.py`
  - `config.py`
  - `.env`
  - `.gitignore`
  - `requirements.txt`

## Git Workflow
- Created a dedicated feature branch (`day3-chatbot`).
- Learned feature branch development and Pull Request workflow.

## Key Learnings
- A chatbot becomes more professional by combining:
  - A strong system prompt
  - Input validation
  - Proper error handling
  - Clear project structure
  - Better user experience
  - Git version control

## Future Improvements
- Add conversation memory to maintain chat history.
- Support multiple AI models.
- Develop a web-based interface using Streamlit or Flask.
- Implement chat history export functionality.