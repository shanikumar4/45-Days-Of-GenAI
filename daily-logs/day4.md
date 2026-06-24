# Day 4 — Tokenization Basics: How Text Becomes Numbers + Embeddings: Word2Vec Intuition & Vector Space

> **#45DaysOfGenAI** • [LinkedIn](https://www.linkedin.com/in/shani-kumar-041177329/) • [GitHub](https://github.com/shanikumar4)

---

## What I Learned Today

---

## Tokenization

LLMs (or any AI model) don't understand languages like English or Hindi directly. When a model receives a sentence, it first breaks it down into smaller pieces — these can be whole words, subwords, or individual characters depending on the model. These pieces are called **Tokens**, and each token is then mapped to a number called a **Token ID**. The entire process of converting raw text into these numerical representations is called **Tokenization**.

### Types of Tokenization

| Type | Example (input: "playing") | Used In |
|---|---|---|
| Word-level | `["playing"]` | older NLP models |
| Subword-level | `["play", "##ing"]` | modern LLMs (GPT, BERT) |
| Character-level | `["p","l","a","y","i","n","g"]` | some seq2seq models |

Right now, **Subword Tokenization** is the go-to approach in LLMs. The two most popular algorithms are:
- **BPE (Byte Pair Encoding)** — used in GPT models
- **WordPiece** — used in BERT

Why subwords? Because they handle rare words and new words (like "ChatGPT") without completely failing. A word-level tokenizer would just say "unknown" — subword tokenizers break it into known pieces instead.

Each model also has a fixed **Vocabulary Size** — for example, GPT-2 has ~50,257 tokens. Everything the model can ever say or understand is represented within that vocabulary.

---

## Embeddings

After tokenization, we have Token IDs — but a model can't understand *relationships* from numbers alone. The number 42 has no connection to 43 just because they're close numerically.

So to give words actual **meaning**, we convert each Token ID into a **dense numerical vector** called an **Embedding**. These vectors are learned during training — they're not hand-crafted.

For example, in a 4-dimensional embedding space:

```
"King"  → [0.99,  0.85, 0.11, 0.70]
"Queen" → [0.97,  0.83, 0.09, 0.68]
"Apple" → [0.10,  0.14, 0.88, 0.20]
```

Notice King and Queen have very similar vectors — the model has learned they're semantically related. Apple is far away from both.

---

## Word2Vec

Word2Vec is a technique introduced by Google (Mikolov et al., 2013) that learns word embeddings automatically from large amounts of text. Before this, creating good word representations was a manual, painful process.

Its core idea:

> *"You shall know a word by the company it keeps."*

Words that appear in similar contexts end up with similar vector representations. Word2Vec does this through two training architectures:

- **CBOW (Continuous Bag of Words)** — given the surrounding words, predict the center word
- **Skip-gram** — given the center word, predict the surrounding words

For example, since "doctor" and "physician" often appear near similar words (hospital, patient, medicine), their vectors end up close to each other in the vector space.

---

## Vector Space

Imagine every word as a point floating in a multi-dimensional space. Words with similar meanings cluster together, while unrelated words are far apart.

In reality, modern embeddings have **768 to 1536+ dimensions** (GPT-3 uses 12,288 dimensions!), but we often visualize them in 2D or 3D using techniques like **t-SNE** or **PCA** to reduce dimensions while preserving structure.

---

## Semantic Relationships

One of the most fascinating properties of embeddings is that **mathematical relationships emerge naturally** — the model was never explicitly told about these, it just picked them up from patterns in text.

The classic example:

```
King − Man + Woman ≈ Queen
```

Which means:

```
Vector("King") − Vector("Man") + Vector("Woman") ≈ Vector("Queen")
```

This works because the model learned that the *difference* between King and Man captures the concept of "royalty + gender." Adding Woman shifts it back correctly.

More such analogies that actually work:

```
Paris − France + Germany ≈ Berlin
Doctor − Man + Woman ≈ Nurse
Walking − Walk + Run ≈ Running
```

This is wild to me — the model never explicitly learned geography or gender. It just read a lot of text and figured it out.

---

## Quick Summary

```
Raw Text → Tokenizer → Token IDs → Embedding Layer → Dense Vectors → Model
```

- **Tokenization** breaks text into manageable pieces (subwords preferred)
- **Token IDs** are just numbers pointing to a vocabulary
- **Embeddings** give those numbers semantic meaning as vectors
- **Word2Vec** was the breakthrough that showed us embeddings could be learned automatically
- **Vector Space** is where all the magic lives — similar meanings = similar directions

---

*Day 4 done. Tomorrow diving deeper into how these embeddings actually flow through a Transformer. Stay tuned.*
