import json
import os
from prompts import SYSTEM_PROMPT

MAX_HISTORY = 10
HISTORY_FILE = "history.json"

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
    save_history(HISTORY_FILE)


def add_assistant_message(text):
    messages.append(
        {
            "role": "assistant",
            "content": text
        }
    )
    trim_history()
    save_history(HISTORY_FILE)


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
    save_history(HISTORY_FILE)


def show_history():
    print("\n========== HISTORY ==========\n")
    for msg in messages[1:]:
        print(f"{msg['role'].upper()}:")
        print(msg["content"])
        print()
    print("=============================\n")


def save_history(filename="session.json"):
    try:
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(messages, f, indent=4)
        return True
    except Exception as e:
        print(f"\n❌ Failed to save history to {filename}: {e}")
        return False


def load_history(filename="session.json"):
    global messages
    if os.path.exists(filename):
        try:
            with open(filename, "r", encoding="utf-8") as f:
                loaded = json.load(f)
                if isinstance(loaded, list) and len(loaded) > 0:
                    messages = loaded
            return True
        except Exception as e:
            print(f"\n❌ Failed to load history from {filename}: {e}")
            return False
    return False

# Auto-load on start
load_history(HISTORY_FILE)