# 🎬 Mini Project 1: Text Sentiment Analyzer

A beginner-friendly Natural Language Processing (NLP) project that uses the Hugging Face `pipeline()` API to classify the sentiment of movie reviews.

This project demonstrates how to use a pre-trained Transformer model for sentiment analysis without training a model from scratch.

---

## 🚀 Features

- Analyze movie reviews
- Predict **Positive** or **Negative** sentiment
- Display confidence score
- Beginner-friendly code
- Uses Hugging Face Transformers

---

## 🛠️ Tech Stack

- Python 3.x
- Hugging Face Transformers
- PyTorch

---

## 📂 Project Structure

```
Mini-Project-1-Text-Sentiment-Analyzer/
│
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 📦 Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/Mini-Project-1-Text-Sentiment-Analyzer.git
```

### 2. Navigate to the project

```bash
cd Mini-Project-1-Text-Sentiment-Analyzer
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Project

```bash
python app.py
```

---

## 💻 Example

### Input

```
Enter Movie Review:

This movie was absolutely amazing!
```

### Output

```
Prediction
----------------------
Sentiment : POSITIVE
Confidence : 99.87%
```

---

## 📄 Sample Code

```python
from transformers import pipeline

classifier = pipeline("sentiment-analysis")

review = input("Enter Movie Review:\n")

result = classifier(review)

prediction = result[0]

print("\nPrediction")
print("----------------------")
print("Sentiment :", prediction["label"])
print("Confidence:", round(prediction["score"] * 100, 2), "%")
```

---

## 📚 What I Learned

- What is NLP (Natural Language Processing)
- Hugging Face `pipeline()`
- Using pre-trained Transformer models
- Performing sentiment analysis
- Processing model predictions
- Building a simple AI application with Python

---

## 📌 Future Improvements

- Analyze multiple reviews at once
- Export results to CSV
- Build a Streamlit web app
- Add a graphical user interface (GUI)
- Support more sentiment analysis models

---

## 📷 Demo

```
Enter Movie Review:

Worst movie ever.

Prediction
----------------------
Sentiment : NEGATIVE
Confidence : 99.91%
```

---

## 🤝 Contributing

Contributions are welcome!

Feel free to fork the repository and submit a pull request.

---

## ⭐ If you found this project helpful

Give this repository a ⭐ on GitHub!

---

## 📜 License

This project is licensed under the MIT License.