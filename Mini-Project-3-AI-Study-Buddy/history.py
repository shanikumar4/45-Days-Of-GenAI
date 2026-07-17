from prompts import SYSTEM_PROMPT

MAX_HISTORY = 10

messages = [
    {
        "role": "system",
        "content": SYSTEM_PROMPT
    }
]


def add_user_message(text):
    messages.append(
        {
            "role": "user",
            "content": text
        }
    )
    trim_history()


def add_assistant_message(text):
    messages.append(
        {
            "role": "assistant",
            "content": text
        }
    )
    trim_history()


def trim_history():
    """
    Keep:
    System Prompt
    +
    Last MAX_HISTORY messages
    """

    if len(messages) > MAX_HISTORY + 1:
        del messages[1:-MAX_HISTORY]


def get_messages():
    return messages


def clear_history():
    global messages

    messages = [
        {
            "role": "system",
            "content": SYSTEM_PROMPT
        }
    ]


def show_history():
    print("\n========== HISTORY ==========\n")

    for msg in messages[1:]:
        print(f"{msg['role'].upper()}:")
        print(msg["content"])
        print()

    print("=============================\n")