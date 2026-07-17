from config import client, MODEL
from history import get_messages

from openai import (
    AuthenticationError,
    RateLimitError,
    APIConnectionError,
    NotFoundError,
)

import time


def chat():

    try:

        start = time.time()

        stream = client.chat.completions.create(
            model=MODEL,
            messages=get_messages(),
            temperature=0.3,
            max_tokens=300,
            stream=True,
        )

        answer = ""

        print("\n🤖 AI:\n")

        for chunk in stream:

            token = chunk.choices[0].delta.content

            if token:
                print(token, end="", flush=True)
                answer += token

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