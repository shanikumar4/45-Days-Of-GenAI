# Day 5 — CNNs, RNNs, LSTMs & Why Transformers Replaced RNNs

> **#45DaysOfGenAI** • [LinkedIn](https://www.linkedin.com/in/shani-kumar-041177329/) • [GitHub](https://github.com/shanikumar4)

---

# What I Learned Today

---

# Why Different Neural Networks Exist

A standard **Feed Forward Neural Network (MLP)** assumes every input feature is independent.

This works well for structured/tabular data but fails for images and text because they contain relationships between neighboring pixels or words.

Different data types require different neural network architectures.

| Data Type              | Best Model  |
| ---------------------- | ----------- |
| Tabular Data           | MLP         |
| Images                 | CNN         |
| Sequential Data        | RNN / LSTM  |
| Modern Language Models | Transformer |

---

# CNN (Convolutional Neural Network)

CNNs are designed for **spatial data**, especially images.

Instead of looking at the whole image at once, CNNs use small filters (kernels) that slide across the image to detect local patterns like edges, corners, textures, and shapes.

These simple features combine layer by layer to recognize complex objects.

```
Image
   ↓
Convolution
   ↓
ReLU
   ↓
Pooling
   ↓
Convolution
   ↓
Pooling
   ↓
Flatten
   ↓
Dense Layer
   ↓
Prediction
```

### Why CNNs are Powerful

* Preserve spatial relationships between pixels
* Learn hierarchical features automatically
* Require far fewer parameters than fully connected networks
* Excellent for computer vision tasks

### Applications

* Image Classification
* Face Recognition
* Object Detection
* Medical Imaging
* OCR
* Self-Driving Cars

---

# RNN (Recurrent Neural Network)

Unlike images, language and time-series data have **order**.

```
"I love AI"
```

is completely different from

```
"AI love I"
```

RNNs solve this problem by introducing **memory**.

Each word updates a hidden state that is passed to the next step.

```
Word1
   ↓
Hidden State
   ↓
Word2
   ↓
Hidden State
   ↓
Word3
   ↓
Prediction
```

This allows the model to remember previous information while processing sequences.

### Applications

* Language Modeling
* Machine Translation
* Speech Recognition
* Time-Series Forecasting
* Music Generation

---

# Why RNNs Fail

Although RNNs have memory, they struggle with **long sequences**.

Consider:

```
"The movie released in 1997 won multiple awards because it was..."
```

To predict the correct word later, the model must remember information introduced many words earlier.

Unfortunately, RNNs gradually forget older information.

---

# Vanishing Gradient Problem

During backpropagation, gradients become smaller after every step.

```
1
↓
0.5
↓
0.25
↓
0.125
↓
0.06
↓
≈ 0
```

As gradients approach zero:

* Earlier layers stop learning
* Long-term information disappears
* The model mainly remembers recent words

This is called the **Vanishing Gradient Problem**.

---

# LSTM (Long Short-Term Memory)

LSTMs were developed to solve the memory limitations of RNNs.

Instead of one simple hidden state, LSTMs maintain a **memory cell** controlled by three gates.

### Forget Gate

Removes unnecessary information.

### Input Gate

Stores important new information.

### Output Gate

Selects what information should be passed to the next step.

```
Previous Memory
        ↓
 Forget Gate
        ↓
 Input Gate
        ↓
 Updated Memory
        ↓
 Output Gate
        ↓
 Next Time Step
```

LSTMs remember information much longer than standard RNNs.

---

# Why Transformers Were Needed

Even though LSTMs improved memory, they still process words **one at a time**.

```
Word1
  ↓
Word2
  ↓
Word3
  ↓
Word4
```

This creates several problems:

* Slow training
* No parallel processing
* Difficult to scale
* Expensive for very long sequences

Researchers needed a faster and more scalable architecture.

---

# Enter Transformers

Transformers completely removed recurrence.

Instead, they introduced **Self-Attention**, allowing every word to directly interact with every other word in the sentence.

```
Input Sentence
        ↓
Self-Attention
        ↓
Context-Aware Representations
        ↓
Prediction
```

This enables the model to understand long-range relationships without passing information step by step.

### Advantages

* Captures long-term dependencies
* Processes all tokens in parallel
* Faster GPU training
* Highly scalable
* Foundation of modern LLMs

Examples:

* GPT
* Gemini
* Claude
* Llama

---


# Evolution of Deep Learning

```
MLP
 ↓
CNN (Images)
 ↓
RNN (Sequential Data)
 ↓
LSTM (Long-Term Memory)
 ↓
Transformer (Attention)
 ↓
GPT • Gemini • Claude • Llama
```

---

# Quick Summary

```
Tabular Data
        ↓
      MLP

Images
        ↓
      CNN

Sequential Data
        ↓
      RNN

Long Sequential Data
        ↓
      LSTM

Large Language Models
        ↓
 Transformer + Self-Attention
```

* **CNNs** learn spatial patterns from images.
* **RNNs** introduce memory for sequential data.
* **LSTMs** solve long-term memory problems using gated memory cells.
* **Transformers** replace recurrence with Self-Attention, enabling parallel processing and long-range understanding.
* Modern AI systems like **GPT, Gemini, Claude, and Llama** are all built on the Transformer architecture.

---

