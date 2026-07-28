# Day 18 — LangChain Advanced: Tools, Agents, Messages, Structured Output, Memory & Middleware

> **#45DaysOfGenAI** • [LinkedIn](https://www.linkedin.com/in/shani-kumar-041177329/) • [GitHub](https://github.com/shanikumar4)

---

# What I Learned Today

Today, I dived deeper into **LangChain** by exploring its advanced components — Tools, Agents, Messages, Structured Output, Memory (with LangGraph), and Middleware. These are the building blocks that transform a simple LLM call into a fully autonomous AI agent capable of reasoning, using external tools, and maintaining context across conversations.

---

## Tools in LangChain

Tools are functions that an LLM can call to perform real-world tasks like fetching weather, searching the web, or running calculations.

### Key Points

* A tool has a **name**, a **description**, and **argument definitions**
* Defined using the `@tool` decorator from `langchain.tools`
* Bound to a model using `model.bind_tools([tool])`
* The model decides **when** and **how** to call a tool
* Tool outputs are fed back to the model for a final response

### Tool Execution Flow

```text
User Query
    │
    ▼
Model + Bound Tools
    │
    ▼
Tool Call (if needed)
    │
    ▼
Tool Execution
    │
    ▼
Result → Model
    │
    ▼
Final Response
```

---

## Agents

Agents are autonomous systems that use an LLM as a reasoning engine to decide which tools to call, in what order, based on the user's request.

### Key Points

* Created using `create_agent(model, tools=[...])`
* The agent autonomously decides tool usage
* Supports **streaming** responses with `agent.stream()`
* Works with a single tool or **multiple tools** simultaneously
* Can use real-world tools like **TavilySearch** for web search

### Example: Agent with Multiple Tools

* **TavilySearch** — fetches real-time web results
* **Calculator tool** — evaluates math expressions
* The agent decides which tool to call based on the query

---

## Messages

Messages are the fundamental units of communication between the user and the model in LangChain.

### Message Types

* **SystemMessage** — Tells the model how to behave and sets the context
* **HumanMessage** — Represents the user's input
* **AIMessage** — Represents the model's response (includes content, tool calls, metadata)
* **ToolMessage** — Represents the output returned from a tool call

### Key Points

* Every message has a **Role**, **Content**, and optional **Metadata**
* Use **text prompts** (strings) for simple, single-turn requests
* Use **message lists** for multi-turn conversations with context
* System messages guide the model's persona and behavior
* Message metadata includes optional fields like `name` and `id` for tracing

---

## Structured Output

Structured Output forces the LLM to return responses in a fixed, predictable format instead of free-form text — making it easy to parse in applications.

### Ways to Define Structured Output

#### 1. Pydantic BaseModel
* Define fields with `Field(description=...)` for validation
* Supports **nested structures** (e.g., a Movie with a list of Actors)
* Use `model.with_structured_output(Schema)` to bind the schema
* Supports `include_raw=True` to get both raw and parsed output

#### 2. TypedDict
* Simpler alternative using Python's built-in `typing`
* No runtime validation, but less boilerplate
* Use `Annotated` fields to provide descriptions

#### 3. DataClasses
* Uses Python's `@dataclass` decorator
* Clean and readable class definition

### Key Points

* Structured output makes AI responses **machine-readable**
* Ideal for extracting entities, filling forms, or generating JSON responses
* Nested models enable **complex, hierarchical data extraction**

---

## Agent with Memory

Memory allows agents to remember previous conversations across multiple turns using **LangGraph's checkpoint system**.

### Key Points

* Uses `InMemorySaver` as a checkpointer for in-session memory
* Each conversation is tracked by a unique **thread_id** in the config
* Different `thread_id` values create completely **separate conversations**
* The agent can recall information from earlier in the same thread
* Essential for building stateful, multi-turn chatbots and assistants

### Memory Flow

```text
User Message (thread_id: "chat1")
    │
    ▼
Agent + InMemorySaver Checkpointer
    │
    ▼
State Persisted → Thread Memory
    │
    ▼
Next Message in same thread_id
    │
    ▼
Agent recalls previous context
```

---

## Middleware

Middleware lets you intercept and control what happens **inside the agent** — before, during, and after tool calls or responses.

### Use Cases

* Tracking agent behavior with **logging and analytics**
* Transforming prompts and formatting outputs
* Adding **retries**, fallbacks, and early termination
* Applying **rate limits**, guardrails, and PII detection

### Types of Middleware

#### Summarization Middleware
* Automatically summarizes conversation history when approaching **token limits**
* Preserves recent messages while compressing older context
* Ideal for long-running conversations and multi-turn dialogues

#### Human-in-the-Loop Middleware
* Pauses the agent before executing certain tool calls
* Requires **human approval, editing, or rejection** before proceeding
* Critical for high-stakes operations like database writes or financial transactions
* Ensures compliance workflows with mandatory human oversight

---

## What I Learned

Today's session gave me a hands-on understanding of the full LangChain agent pipeline:

* Defining and binding **Tools** to models
* Building **Agents** that autonomously reason and act
* Understanding all **Message types** and when to use each
* Enforcing **Structured Output** using Pydantic, TypedDict, and DataClasses
* Persisting **Agent Memory** across turns with LangGraph checkpointers
* Controlling agent behavior using **Middleware** (Summarization & Human-in-the-Loop)

---

## What's Next?

* Document Loaders & Text Splitters
* Embeddings & Vector Databases
* Retrieval-Augmented Generation (RAG)
* LangChain Expression Language (LCEL)
* Building full end-to-end AI agent projects

---

## Today's Takeaway

LangChain's advanced components — Tools, Agents, Messages, Structured Output, Memory, and Middleware — form the backbone of production-grade AI applications. Together, they enable me to build intelligent, stateful, and controllable agents that go far beyond simple question-answering into truly autonomous AI workflows.

---

## References

* https://python.langchain.com/
* https://docs.langchain.com/
* https://github.com/langchain-ai/langchain
* https://www.langchain.com/langgraph
