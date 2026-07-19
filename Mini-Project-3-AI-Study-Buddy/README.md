# 📚 AI Study Buddy

A command-line based AI assistant tailored for students, powered by OpenRouter and OpenAI models. It features real-time streaming, rich markdown syntax highlighting, and persistent memory to keep track of your study sessions.

## ✨ Features

- **Real-time Streaming:** See the AI's responses dynamically with syntax-highlighted code blocks (thanks to `rich`).
- **Persistent History:** Chat history is automatically saved to `history.json` and survives application restarts.
- **Session Management:** Save or load specific chat sessions to file.
- **Interactive Commands:**
  - `/quiz <topic>` - Generates 3 practice questions about a specific topic.
  - `/flashcards <topic>` - Creates 5 quick revision flashcards with definitions.
  - `/summary` - Summarizes the current conversation so far.
  - `/history` - View the entire chat history.
  - `/clear` - Wipes the current conversation from memory.

## 🚀 Installation & Setup

1. **Clone or Download the Repository**
2. **Create a Virtual Environment (Optional but recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```
3. **Install Dependencies:**
   ```bash
   pip install -r requirment.txt
   ```
4. **Configure API Keys:**
   Create a `.env` file in the root directory and add your OpenRouter API key:
   ```env
   OPENROUTER_API_KEY=your_openrouter_api_key_here
   ```

## 🎮 Usage

Run the main application script:

```bash
python app.py
```

Inside the chat, you can type `/help` to see all available commands.

## 🛠️ Built With
- [Python](https://www.python.org/)
- [OpenAI Python SDK](https://github.com/openai/openai-python) (Used for OpenRouter)
- [Rich](https://rich.readthedocs.io/en/stable/) (For syntax-highlighted markdown streaming)
- [python-dotenv](https://pypi.org/project/python-dotenv/)
