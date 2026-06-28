# Day 8 — Positional Encoding + Encoder , Decoder and types of transformer models 

> **#45DaysOfGenAI** • [LinkedIn](https://www.linkedin.com/in/shani-kumar-041177329/) • [GitHub](https://github.com/shanikumar4)

*What I Learned Today*


## Positional Ecoding 

Positional encoding is a techinique that add more information about the position of toaken in the sequence to the input embededings.
This he;ps Transformers to understand the relative or absolute position of tokens which is important for defernecing between words in different position and capturing the structure of a sentence.

*The most common method for calculating positional encodings is based on sinusoidal functions.*

**notebook : notebooks/positionalEncoding.ipynb**

## Encoder 

An encoder is a neural network component that transforms input sequences (like text) into meaningful numerical representations called embeddings. In transformers, the encoder processes the entire input sequence to capture relationships between all positions. The encoder maps variable-length input sequences to fixed-dimensional feature representations. A common use case is encoding a sentence for classification or question answering.

### Working Principle of Encoders

    1. Embedding input to convert tokens to vector representations
    2. Positional Encoding added to input embeddings
    3. Multi-Layer Processing, applying N layers sequentially
    4. Apply non-linear transformation using Feed Forward Network
    5. Output Representation Generation

**notebook : notebooks/encoder.ipynb**


## Decoder

A decoder in deep learning, especially in Transformer architectures, is the part of the model responsible for generating output sequences from encoded representations. In sequence-to-sequence tasks like machine translation, text summarization, or image captioning, the decoder takes the output from the encoder and converts it into a target language or format. It does this step-by-step, attending to both the encoded input and the already generated outputs.

### Working Principle

    1. Input Embeddings are passed into the decoder with positional encodings.
    2. Masked Self-Attention Layer ensures the model can’t “see” future tokens.
    3. Encoder-Decoder Attention allows the decoder to focus on relevant input tokens.
    4. Feedforward Layers refine representations.
    5. A linear layer maps the final output to the vocabulary space.
    6. Softmax provides a probability distribution over tokens for generation.

**notebook : notebooks/decoder.ipynb**

## Encoder-Only Models (e.g., BERT)

* Uses only the **Encoder** part of the Transformer.
* Applies **bidirectional self-attention**, allowing each token to attend to both previous and future tokens.
* Best for **understanding** text rather than generating it.
* Common tasks: Sentiment Analysis, Text Classification, NER, Search, and Question Answering.

---

## Decoder-Only Models (e.g., GPT, LLaMA)

* Uses only the **Decoder** part of the Transformer.
* Applies **causal (masked) self-attention**, where each token can attend only to previous tokens.
* Generates text **one token at a time**.
* Best for Chatbots, Text Generation, Code Generation, and Large Language Models (LLMs).

---

## Encoder-Decoder Models (e.g., T5, BART)

* Combines both the **Encoder** and **Decoder**.
* The encoder understands the input, while the decoder generates the output using cross-attention.
* Best for **sequence-to-sequence** tasks such as Machine Translation, Summarization, Paraphrasing, and Question Answering.

