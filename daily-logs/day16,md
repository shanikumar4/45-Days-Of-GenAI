# Day 16 — Mini Project 3: AI Study Buddy (CLI Chatbot with OpenAI SDK, Streaming & Conversation Memory)

> **#45DaysOfGenAI** • [LinkedIn](https://www.linkedin.com/in/shani-kumar-041177329/) • [GitHub](https://github.com/shanikumar4)

---

# What I Learned Today

Today, I started building **Mini Project 3: AI Study Buddy**, a command-line chatbot that helps students learn any topic using a Large Language Model (LLM). Instead of only learning new concepts, I focused on applying them by building a real-world AI application.

The chatbot supports **streaming responses**, **conversation memory**, and a custom **system prompt** to create a helpful study assistant. While building the project, I also learned how professional AI applications are structured using modular Python files, making the code easier to maintain and extend.

One important lesson was understanding that a chatbot is much more than just sending prompts to an API. Features like conversation history, prompt engineering, error handling, and user experience are equally important when building production-ready AI applications.

---

## Mini Project 3 — AI Study Buddy

The goal of this project is to build an AI-powered CLI chatbot that acts as a personal study companion.

### Key Features

* Interactive command-line chatbot
* Streaming AI responses
* Conversation memory
* Custom Study Buddy personality
* Modular project architecture
* Error handling
* Command-based interface

---

## Project Architecture

Instead of writing everything in a single Python file, I organized the project into multiple modules.

### Folder Structure

```text
Mini-Project-3-AI-Study-Buddy/
│
├── app.py
├── chatbot.py
├── config.py
├── history.py
├── prompts.py
├── requirements.txt
├── .env
└── .gitignore
```

### Why Modular Design?

* Easier to maintain
* Better code readability
* Reusable components
* Follows professional software engineering practices

---

## OpenAI Python SDK

I used the **OpenAI Python SDK** (configured with OpenRouter for free models) to communicate with an LLM.

### Key Points

* Simple API integration
* Supports streaming responses
* Compatible with OpenRouter
* Easy conversation management

---

## System Prompt

The chatbot uses a custom **System Prompt** to define its behavior.

### Key Points

* Acts as an AI Study Buddy
* Gives beginner-friendly explanations
* Uses Markdown formatting
* Explains programming concepts step by step
* Handles small spelling mistakes intelligently
* Avoids exposing internal reasoning

---

## Conversation Memory

A chatbot feels intelligent only when it remembers previous messages.

### Key Points

* Stores user and assistant messages
* Sends conversation history with every API call
* Maintains context across multiple questions
* Creates a natural chat experience

---

## Streaming Responses

Instead of waiting for the complete answer, responses are streamed token by token.

### Benefits

* Faster perceived response time
* Better user experience
* Similar interaction to ChatGPT
* Real-time output in the terminal

---

## Error Handling

I added error handling to make the chatbot more reliable.

### Handles

* Invalid API key
* Connection issues
* Rate limit errors
* Model availability errors
* Unexpected exceptions

---

## CLI Commands

To improve usability, I added command support.

### Available Commands

* `/help`
* `/history`
* `/clear`
* `/exit`

These commands allow users to manage conversations without making unnecessary API requests.

---

## Memory Optimization

Sending the complete conversation every time increases token usage.

### Optimization

* Keep the system prompt
* Store only the most recent messages
* Reduce token consumption
* Improve performance

---

## Response Timing

The chatbot measures how long each AI response takes.

### Why It Matters

* Helps compare model performance
* Useful for debugging
* Gives insight into application latency

---

## What I Learned During Development

This project taught me that building AI applications involves much more than calling an API.

Some of the most valuable lessons were:

* Designing clean project architecture
* Writing effective system prompts
* Managing conversation history
* Handling API errors gracefully
* Optimizing token usage
* Improving user experience through streaming
* Building scalable and maintainable code

I also encountered real-world issues while integrating the API, including quota limitations and model availability. Debugging these problems helped me understand how AI APIs work in practice and how to troubleshoot integration issues.

---

## What's Next?

The current chatbot works well, but there are many exciting features I plan to add to make it a more powerful AI Study Buddy.

### Upcoming Features

* Save conversations to a JSON file
* Load previous chat sessions
* Add `/quiz <topic>` command
* Generate flashcards from any topic
* Summarize long conversations
* Add syntax-highlighted code output
* Build a beautiful terminal UI using the `rich` library
* Display token usage and model information
* Add colored output and loading animations
* Support Retrieval-Augmented Generation (RAG) with PDFs and notes
* Create a Streamlit web interface
* Add voice input and text-to-speech support
* Package the project for easy installation

---

## Today's Takeaway

Today's project showed me that building AI applications is not just about generating answers—it is about creating a complete user experience. Features like conversation memory, streaming responses, prompt engineering, modular architecture, and robust error handling make a simple chatbot feel like a real AI assistant.

This project also gave me hands-on experience with software engineering practices used in production AI systems, making it one of the most practical milestones in my **#45DaysOfGenAI** journey.

---

## Reference

* https://platform.openai.com/docs
* https://github.com/openai/openai-python
* https://openrouter.ai/docs
