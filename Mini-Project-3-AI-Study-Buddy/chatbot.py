from config import client, MODEL
from history import get_messages

from openai import (
    AuthenticationError,
    RateLimitError,
    APIConnectionError,
    NotFoundError,
)

import time
from rich.console import Console
from rich.markdown import Markdown
from rich.live import Live

console = Console()

def chat():

    try:

        start = time.time()

        stream = client.chat.completions.create(
            model=MODEL,
            messages=get_messages(),
            temperature=0.3,
            max_tokens=800,
            stream=True,
        )

        answer = ""

        print("\n🤖 AI:\n")
        
        with Live(Markdown(""), console=console, refresh_per_second=12, transient=False) as live:
            for chunk in stream:
                token = chunk.choices[0].delta.content
                if token:
                    answer += token
                    live.update(Markdown(answer))

        end = time.time()

        print()
        print("\n-----------------------------")
        print(f"⏱ Response Time : {end-start:.2f} sec")
        print("-----------------------------\n")

        return answer

    except AuthenticationError:
        print("\n❌ Invalid OpenRouter API Key.")
        return ""

    except RateLimitError:
        print("\n❌ Free model quota exceeded.")
        return ""

    except APIConnectionError:
        print("\n❌ Internet connection error.")
        return ""

    except NotFoundError:
        print("\n❌ Model not available.")
        return ""

    except Exception as e:
        print(f"\n❌ {e}")
        return ""