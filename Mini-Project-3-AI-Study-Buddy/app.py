from chatbot import chat

from history import (
    add_user_message,
    add_assistant_message,
    clear_history,
    show_history,
)

print("=" * 50)
print("📚 AI Study Buddy")
print("=" * 50)

print("Model      : OpenRouter Auto")
print("Streaming  : Enabled")
print("Memory     : Enabled")
print()

print("Type /help for commands.\n")

while True:

    user = input("👤 You: ").strip()

    if not user:
        continue

    command = user.lower()

    if command in ["exit", "quit", "/exit"]:
        print("\n👋 Goodbye!")
        break

    elif command == "/help":

        print("""
Available Commands

/help       Show commands

/history    Show conversation

/clear      Clear memory

/exit       Exit chatbot
""")
        continue

    elif command == "/history":
        show_history()
        continue

    elif command == "/clear":
        clear_history()
        print("✅ Conversation cleared.\n")
        continue

    add_user_message(user)

    answer = chat()

    if answer:
        add_assistant_message(answer)