from chatbot import chat
from history import (
    add_user_message,
    add_assistant_message,
    clear_history,
    show_history,
    save_history,
    load_history
)
import shlex

print("=" * 50)
print("📚 AI Study Buddy")
print("=" * 50)

print("Model      : OpenRouter Auto")
print("Streaming  : Enabled (with Syntax Highlighting)")
print("Memory     : Enabled (Persistent)")
print()

print("Type /help for commands.\n")

while True:

    user = input("👤 You: ").strip()

    if not user:
        continue

    # Split command and arguments safely
    parts = user.split(maxsplit=1)
    command = parts[0].lower()
    args = parts[1] if len(parts) > 1 else ""

    if command in ["exit", "quit", "/exit"]:
        print("\n👋 Goodbye!")
        break

    elif command == "/help":

        print("""
Available Commands:

/help                 Show commands
/history              Show conversation
/clear                Clear memory
/save [filename]      Save current chat session (default: session.json)
/load [filename]      Load a chat session (default: session.json)
/quiz <topic>         Generate practice questions
/flashcards <topic>   Create quick revision flashcards
/summary              Summarize the current conversation
/exit                 Exit chatbot
""")
        continue

    elif command == "/history":
        show_history()
        continue

    elif command == "/clear":
        clear_history()
        print("✅ Conversation cleared.\n")
        continue

    elif command == "/save":
        filename = args.strip() or "session.json"
        if save_history(filename):
            print(f"✅ Session saved to {filename}.\n")
        continue

    elif command == "/load":
        filename = args.strip() or "session.json"
        if load_history(filename):
            print(f"✅ Session loaded from {filename}.\n")
        continue
        
    elif command == "/quiz":
        if not args:
            print("❌ Please provide a topic for the quiz. (e.g. /quiz Python loops)\n")
            continue
        user_prompt = f"Generate 3 practice questions about {args}."
        print(f"Generating quiz for: {args}...")
        add_user_message(user_prompt)
        answer = chat()
        if answer:
            add_assistant_message(answer)
        continue

    elif command == "/flashcards":
        if not args:
            print("❌ Please provide a topic for flashcards. (e.g. /flashcards Machine Learning)\n")
            continue
        user_prompt = f"Create 5 quick revision flashcards with concepts and definitions about {args}."
        print(f"Generating flashcards for: {args}...")
        add_user_message(user_prompt)
        answer = chat()
        if answer:
            add_assistant_message(answer)
        continue

    elif command == "/summary":
        user_prompt = "Please provide a concise summary of our conversation so far."
        print("Generating summary...")
        add_user_message(user_prompt)
        answer = chat()
        if answer:
            add_assistant_message(answer)
        continue

    add_user_message(user)

    answer = chat()

    if answer:
        add_assistant_message(answer)