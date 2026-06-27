# Day 7 — Self-Attention (Q, K, V) & Multi-Head Attention

> **#45DaysOfGenAI** • [LinkedIn](https://www.linkedin.com/in/shani-kumar-041177329/) • [GitHub](https://github.com/shanikumar4)

---

# What I Learned Today

Today, I learned the core concept behind **Transformer models**—**Self-Attention**. I understood how **Query (Q), Key (K), and Value (V)** help a model identify important words in a sentence. I also explored **Multi-Head Attention**, which allows Transformers to capture different relationships simultaneously.

---

# Self-Attention

Self-Attention enables every word in a sentence to focus on other relevant words, helping the model understand context more effectively.

Example:

```text
The cat sat on the mat.
```

When processing **"sat"**, the model pays more attention to words like **"cat"** and **"mat"**.

---

# Query (Q), Key (K), and Value (V)

Every word embedding is transformed into three vectors:

```python
Q = XWQ
K = XWK
V = XWV
```

* **Query (Q):** What am I looking for?
* **Key (K):** Am I relevant?
* **Value (V):** The information to share.

---

# Attention Calculation

The model compares Queries with Keys:

```text
Attention Score = Q × Kᵀ
```

The scores are passed through **Softmax** to create attention weights, which are then multiplied with the **Value** vectors to produce a contextual representation of each word.

---

# Multi-Head Attention

Instead of using one attention mechanism, Transformers use multiple attention heads.

Each head learns different relationships, such as:

* Grammar
* Context
* Word dependencies
* Semantic meaning

Their outputs are combined to create richer word representations.

---

# Why Multi-Head Attention?

Using multiple heads helps the model understand a sentence from different perspectives at the same time, leading to better language understanding and performance.

---

# Key Takeaways

* Learned how Self-Attention captures word relationships.
* Understood the roles of Query, Key, and Value.
* Learned how attention scores are computed.
* Explored the purpose of Softmax in attention.
* Understood why Multi-Head Attention improves Transformer models.

---

# References

## Attention Is All You Need

https://arxiv.org/abs/1706.03762

## The Illustrated Transformer

https://jalammar.github.io/illustrated-transformer/

## Hugging Face Transformers

https://huggingface.co/docs/transformers

---

**#45DaysOfGenAI 🚀**

Every day, one step closer to becoming an AI Engineer.
