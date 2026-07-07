# Day 13 — Prompt Engineering Challenge: Building a Prompt Battle Notebook with GPT API

> **#45DaysOfGenAI** • [LinkedIn](https://www.linkedin.com/in/shani-kumar-041177329/) • [GitHub](https://github.com/shanikumar4)

---

# What I Learned Today

Today, I applied everything I had learned over the past few days by building a **Prompt Engineering Challenge** project. Instead of training a model or fine-tuning one, I solved multiple **NLP tasks using only prompting** with an LLM.

I created a notebook that performs tasks like **Sentiment Analysis, Summarization, Translation, Grammar Correction, Text Classification, Named Entity Recognition, Question Answering, Information Extraction, Keyword Extraction, and Email Generation** using prompts and the OpenAI-compatible API.

This project taught me that **good prompts can significantly improve AI responses without changing the model itself.**

---

## Mini Project 2 — Prompt Engineering Challenge

The goal of this project was to solve multiple NLP tasks using only prompt engineering techniques.

### Key Points

* Built a Prompt Engineering notebook
* Used GPT through an OpenAI-compatible API
* Solved 10 classic NLP tasks
* No model training or fine-tuning required

---

## Project Structure

To make the project organized and reusable, I separated prompts, outputs, and helper functions.

### Key Points

* Stored prompts in separate `.txt` files
* Created a reusable `helper.py`
* Saved API keys securely using `.env`
* Generated outputs inside an `outputs` folder

---

## Prompt Engineering Techniques

I explored different ways to design prompts instead of relying on model training.

### Key Points

* Zero-shot Prompting
* Role Prompting
* Structured Output
* Prompt Formatting
* Temperature Control

---

## NLP Tasks Covered

The notebook demonstrates how a single LLM can solve different language tasks using carefully designed prompts.

### Key Points

* Sentiment Analysis
* Text Summarization
* Translation
* Grammar Correction
* Named Entity Recognition
* Keyword Extraction
* Question Answering
* Text Classification
* Email Writing
* Information Extraction

---

## Saving and Evaluating Outputs

Instead of just printing responses, I stored every experiment for future analysis.

### Key Points

* Saved outputs as JSON
* Created CSV files for comparison
* Evaluated prompt quality
* Compared different prompting approaches

---

## Challenges I Faced

This project wasn't difficult because of the AI concepts—it was challenging because of the small implementation details.

I spent a lot of time debugging issues like:

* Python virtual environment configuration
* Installing missing packages
* Jupyter kernel using the wrong interpreter
* Understanding API keys and environment variables
* Difference between OpenAI API and OpenRouter API
* API quota and billing errors
* Organizing project folders
* Saving outputs correctly as JSON
* Writing a proper `.gitignore`
* Understanding what happens behind the scenes when an API request is made

Initially, these looked like tiny issues, but solving them helped me understand how real AI projects are built.

One thing I realized today is that **AI development is not just about writing prompts—it also requires understanding project structure, debugging, APIs, environment management, and software engineering practices.**

---

## Biggest Lesson

Today taught me that building AI applications is much more than calling an API.

Writing the prompt is only one part of the process. Organizing code, managing environments, handling errors, saving outputs, evaluating results, and understanding the complete request-response workflow are equally important.

Every debugging session, even for a small issue, improved my understanding of how AI applications work behind the scenes.

---

## Today's Takeaway

Day 13 was one of the most practical days in my #45DaysOfGenAI journey.

I not only learned Prompt Engineering concepts but also experienced the real-world challenges of building an AI project from scratch. Although I spent a lot of time fixing small configuration issues, those struggles helped me understand the development process much better. Every error I solved increased my confidence, and by the end of the day, I had a structured Prompt Engineering project that I can continue improving with more prompting techniques and evaluation methods.

---

## Reference

- https://platform.openai.com/docs
- https://openrouter.ai/docs
- https://github.com/openai/openai-python