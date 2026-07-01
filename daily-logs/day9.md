# Day 9 — GPT, BERT & T5: Understanding Transformer Model Architectures

> **#45DaysOfGenAI** • [LinkedIn](https://www.linkedin.com/in/shani-kumar-041177329/) • [GitHub](https://github.com/shanikumar4)

---

# What I Learned Today

Today, I explored the three major Transformer-based model architectures used in modern NLP: **GPT**, **BERT**, and **T5**. Although all of them are built on the Transformer architecture, they are designed for different purposes and trained using different objectives.

---

## GPT Family (Decoder-Only Models)

The GPT family uses only the **Decoder** part of the Transformer architecture. It is trained using **Causal Language Modeling (CLM)**, where the model predicts the next token based only on previous tokens.

### Key Points

* Decoder-only Transformer architecture
* Uses causal (masked) self-attention
* Predicts the next token one step at a time
* Best for text generation tasks

### Common Applications

* Chatbots
* Content Writing
* Code Generation
* Question Answering
* Large Language Models (LLMs)



---

## BERT (Encoder-Only Models)

BERT uses only the **Encoder** part of the Transformer. It is trained using **Masked Language Modeling (MLM)**, where some words are masked and the model predicts them using both left and right context.

### Key Points

* Encoder-only Transformer architecture
* Bidirectional self-attention
* Learns deep contextual understanding
* Best for language understanding tasks

### Common Applications

* Sentiment Analysis
* Text Classification
* Named Entity Recognition (NER)
* Semantic Search
* Question Answering



---

## T5 (Encoder–Decoder Models)

T5 combines both the **Encoder** and **Decoder** into a single model. It treats every NLP task as a **text-to-text** problem, where both the input and output are plain text.

### Key Points

* Encoder–Decoder Transformer architecture
* Unified text-to-text framework
* Suitable for both understanding and generation
* Highly effective for sequence-to-sequence tasks

### Common Applications

* Machine Translation
* Text Summarization
* Paraphrasing
* Question Answering
* Text Generation



---

## Quick Comparison

| Model | Architecture    | Training Objective       | Best For                       |
| ----- | --------------- | ------------------------ | ------------------------------ |
| GPT   | Decoder-Only    | Next Token Prediction    | Text Generation                |
| BERT  | Encoder-Only    | Masked Language Modeling | Language Understanding         |
| T5    | Encoder–Decoder | Text-to-Text Learning    | Translation, Summarization, QA |

---

## Today's Takeaway

Understanding the differences between **GPT**, **BERT**, and **T5** made it clear that choosing the right architecture depends on the task. GPT excels at generating text, BERT is designed for understanding text, and T5 provides a flexible text-to-text framework that can solve multiple NLP tasks with a single architecture.
