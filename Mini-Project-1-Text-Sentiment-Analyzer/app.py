from transformers import pipeline

# Load sentiment analysis pipeline
classifier = pipeline(
    "sentiment-analysis",
    model="distilbert-base-uncased-finetuned-sst-2-english"
)

# User input
review = input("Enter Movie Review:\n")

if len(review.strip()) == 0:
    print("Please Enter review.") 

# Prediction
result = classifier(review)

prediction = result[0]

print("\nPrediction")
print("----------------------")
print("Sentiment :", prediction["label"])
print("Confidence:", round(prediction["score"] * 100, 2), "%")