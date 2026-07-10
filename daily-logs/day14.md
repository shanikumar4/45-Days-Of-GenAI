# Day 14 — OpenAI Python SDK: Chat Completions, Streaming, Function Calling & Structured JSON Output

> **#45DaysOfGenAI** • [LinkedIn](https://www.linkedin.com/in/shani-kumar-041177329/) • [GitHub](https://github.com/shanikumar4)

---

# What I Learned Today

Today, I learned how to use the **OpenAI Python SDK** to build AI-powered applications. I explored how **Chat Completions** work, how **streaming responses** improve user experience, how **function calling (tool use)** enables LLMs to interact with external APIs and Python functions, and how **structured JSON output** helps generate consistent, machine-readable responses for real-world applications.

---

## OpenAI Python SDK

The OpenAI Python SDK is the official Python library used to interact with OpenAI models through an API.

### Key Points

* Official library for accessing OpenAI models
* Easy to integrate into Python applications
* Supports chat, streaming, tool calling, and structured outputs
* Simplifies communication with AI models

---

## Chat Completions

Chat Completions allow us to send a conversation (messages) to an LLM and receive an AI-generated response.

### Key Points

* Uses a list of messages as input
* Supports system, user, and assistant roles
* Maintains conversational context
* Used for chatbots and AI assistants

---

## Message Roles

Each conversation consists of different message roles that help define the interaction.

### Key Points

* **System** – Sets the assistant's behavior and instructions
* **User** – Contains the user's query or request
* **Assistant** – Represents previous AI responses
* Helps maintain context throughout the conversation

---

## Streaming Responses

Streaming allows the model to generate responses token by token instead of waiting for the complete output.

### Key Points

* Displays responses in real time
* Improves user experience
* Reduces perceived waiting time
* Useful for chatbots and long responses

---

## Function Calling (Tool Use)

Function calling enables the model to decide when it should call external functions, APIs, or databases to complete a task.

### Key Points

* Connects LLMs with external tools
* Supports API calls and database queries
* Improves accuracy using real-world data
* Forms the foundation of AI agents

---

## Tool Definitions

Before an LLM can use a function, developers define available tools and their expected parameters.

### Key Points

* Functions are described using JSON schema
* Specifies function name and description
* Defines required input parameters
* Helps the model choose the correct tool

---

## Structured JSON Output

Structured output asks the model to return information in formats like JSON instead of plain text.

### Key Points

* Produces machine-readable responses
* Easy to parse in applications
* Improves consistency
* Useful for automation and APIs

---

## Why Structured Output Matters

Applications often need structured data instead of natural language.

### Key Points

* Reduces parsing errors
* Makes backend integration easier
* Provides predictable responses
* Ideal for extracting information

---

## Chat Completion Workflow

A typical OpenAI application follows a simple workflow from user input to AI response.

### Key Points

* User sends a prompt
* Model processes the request
* Optional tool/function is called if needed
* Final response is generated

---

## Today's Takeaway

Today's learning helped me understand how the **OpenAI Python SDK** enables developers to build intelligent AI applications. Chat Completions make conversations possible, streaming creates a smoother user experience, function calling allows models to interact with external tools, and structured JSON output makes AI responses reliable and easy to integrate into real-world software. These features are essential for building modern AI assistants, automation systems, and AI-powered applications.

---

## Reference

- https://platform.openai.com/docs
- https://github.com/openai/openai-python