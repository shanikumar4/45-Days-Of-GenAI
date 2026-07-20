# Day 17 — LangChain Fundamentals: Chains, Prompts & Memory

> **#45DaysOfGenAI** • [LinkedIn](https://www.linkedin.com/in/shani-kumar-041177329/) • [GitHub](https://github.com/shanikumar4)

---

# What I Learned Today

Today, I started learning **LangChain**, one of the most popular frameworks for building AI applications powered by Large Language Models (LLMs). Instead of making a single API call, LangChain helps organize prompts, memory, chains, and outputs into reusable workflows.

I explored the core components that make AI applications more modular, scalable, and easier to maintain. This helped me understand how modern chatbots and AI assistants are built beyond simple prompt-response interactions.

---

## What is LangChain?

LangChain is an open-source framework for developing LLM-powered applications.

### Key Features

* Prompt management
* Chain multiple LLM calls
* Conversation memory
* Output parsing
* Tool integration
* Modular architecture

---

## LangChain Architecture

A typical LangChain workflow looks like this:

```text
User
   │
   ▼
Prompt Template
   │
   ▼
Chain
   │
Memory + LLM
   │
   ▼
Output Parser
   │
   ▼
Final Response
```

---

## PromptTemplate & ChatPromptTemplate

I learned how LangChain makes prompts reusable using **PromptTemplate** and **ChatPromptTemplate**.

### Key Points

* Create reusable prompts
* Insert dynamic variables
* Support System, Human, and Assistant messages
* Keep prompts organized and maintainable

---

## Chains

Chains connect multiple LLM operations into a workflow.

### LLMChain

The simplest chain that combines a prompt with an LLM to generate a response.

### SequentialChain

Runs multiple chains one after another, where the output of one becomes the input of the next.

### RouterChain

Routes user requests to different chains based on the type of query, such as math, coding, or writing.

---

## Output Parsers

Output Parsers convert raw LLM responses into structured formats like:

* JSON
* Python dictionaries
* Lists

This makes AI responses easier to process in applications.

---

## Memory

Memory allows the chatbot to remember previous conversations and maintain context.

### ConversationBufferMemory

* Stores the complete conversation
* Best for short chats
* Higher token usage

### ConversationSummaryMemory

* Stores a summarized conversation
* Uses fewer tokens
* Better for long conversations

---

## What I Learned

Today's learning helped me understand the building blocks of LangChain and how they work together to create intelligent AI applications.

Some important concepts I explored:

* Prompt Templates
* Chat Prompt Templates
* LLMChain
* SequentialChain
* RouterChain
* Output Parsers
* Conversation Memory

---

## What's Next?

Next, I'll explore more advanced LangChain topics:

* Document Loaders
* Text Splitters
* Embeddings
* Vector Databases
* Retrieval-Augmented Generation (RAG)
* LangChain Agents

---

## Today's Takeaway

LangChain provides a structured way to build AI applications by combining prompts, chains, memory, and output parsers. Understanding these fundamentals gives me a strong foundation for building more advanced projects like RAG-based chatbots and AI assistants.

---

## References

* https://python.langchain.com/
* https://docs.langchain.com/
* https://github.com/langchain-ai/langchain

This version is around **30–35% shorter** than the previous one while keeping the same clean format and consistent style with your earlier **#45DaysOfGenAI** notes.
