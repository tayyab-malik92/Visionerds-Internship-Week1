# Day 3 - Chatbot Development Findings

## Interactive Chat Loop
- Used `while True` to create a continuous conversation.
- Added an `exit` command to terminate the chatbot gracefully.

## Dynamic User Input
- Replaced hardcoded prompts with `input()`.
- Enabled the chatbot to answer any user query.

## System Prompt
- Moved the chatbot's behavior into `config.py`.
- Made the chatbot easier to maintain and customize.

## Project Structure
- Separated configuration from application logic.
- Improved code readability and organization.

## Git Workflow
- Created a feature branch (`day3-chatbot`).
- Learned how Pull Requests are used in collaborative development.

## Key Learning
- A chatbot becomes interactive by continuously accepting user input and sending it to the LLM while maintaining a clean project structure.