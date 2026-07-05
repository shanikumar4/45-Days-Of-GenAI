# Day 11 — Prompt Engineering: Zero-shot, Few-shot, Role Prompting, Prompt Injection & Hallucinations

> **#45DaysOfGenAI** • [LinkedIn](https://www.linkedin.com/in/shani-kumar-041177329/) • [GitHub](https://github.com/shanikumar4)

---

# What I Learned Today

Today, I learned about **Prompt Engineering**, one of the most important skills for effectively working with Large Language Models (LLMs). I explored different prompting techniques such as **zero-shot**, **few-shot**, **role prompting**, and **instruction prompting**. I also understood how to generate structured outputs, the difference between **system prompts** and **user prompts**, and learned about common challenges like **prompt injection** and **hallucinations**, along with ways to reduce them.

---

## Prompt Engineering

Prompt engineering is the practice of writing clear and effective prompts to guide an AI model toward producing accurate, relevant, and useful responses.

### Key Points

* Helps improve the quality of AI-generated responses
* Clear instructions lead to better outputs
* Includes context, constraints, and desired output format
* Essential for building reliable AI applications

---

## Zero-shot Prompting

Zero-shot prompting asks the model to perform a task without providing any examples. The model relies entirely on its pre-trained knowledge.

### Key Points

* No examples are provided
* Suitable for common and simple tasks
* Quick and easy to use
* May struggle with complex or ambiguous tasks

---

## Few-shot Prompting

Few-shot prompting provides a few examples before asking the model to perform the task, helping it understand the expected pattern.

### Key Points

* Uses example inputs and outputs
* Improves consistency and accuracy
* Useful for classification and formatting tasks
* Helps the model learn the desired response style

---

## Chain-of-Thought Prompting

Chain-of-thought prompting encourages the model to solve problems step by step before producing the final answer.

### Key Points

* Breaks complex problems into smaller steps
* Improves reasoning for math and logic tasks
* Produces more structured solutions
* Helpful for multi-step problem solving

---

## Role Prompting

Role prompting assigns the model a specific role, allowing it to respond with the appropriate expertise and tone.

### Key Points

* Defines the AI's role before the task
* Produces more focused responses
* Useful for educational and professional tasks
* Improves consistency in communication style

---

## Instruction Prompting

Instruction prompting clearly specifies what the model should do, including format, style, and constraints.

### Key Points

* Uses explicit and detailed instructions
* Reduces ambiguity
* Improves response quality
* Makes outputs more predictable

---

## Structured Output

Structured output asks the model to return responses in a predefined format such as JSON, tables, or Markdown.

### Key Points

* Produces machine-readable responses
* Easy to integrate with applications
* Improves consistency
* Useful for APIs and automation

---

## Prompt Injection

Prompt injection is an attack where malicious instructions attempt to override the original prompt or system instructions.

### Key Points

* Tries to manipulate the model's behavior
* Can expose confidential information
* Common security risk in AI applications
* Requires careful prompt and system design

---

## Hallucinations

Hallucinations occur when an AI generates incorrect or fabricated information while presenting it confidently.

### Key Points

* May generate false facts
* Often caused by insufficient context
* Can be reduced with better prompts
* Important to verify factual information

---

## System Prompt vs User Prompt

A **system prompt** defines the model's behavior and rules, while a **user prompt** contains the specific task or question.

### Key Points

* System prompts have higher priority
* User prompts define the current task
* System prompts control overall behavior
* User prompts guide individual responses



## Today's Takeaway

Today's learning showed me that **prompt engineering is much more than simply asking questions**. Writing clear prompts, providing the right context, and selecting the appropriate prompting technique can significantly improve the quality of AI-generated responses. Understanding prompt injection, hallucinations, and the difference between system and user prompts is also essential for building safe, reliable, and effective AI applications.


## Refernce 

[Medium Blog](https://rkniyer999.medium.com/prompt-engineering-explained-from-basic-to-advanced-techniques-2995198eebb6?sharedUserId=shani2405sk) 