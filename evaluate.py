import pandas as pd
import joblib

from preprocess import clean_text

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
    classification_report
)

from sklearn.model_selection import train_test_split

# Load dataset
df = pd.read_csv("dataset/phishing_emails.csv")

df.dropna(inplace=True)

# Clean emails
df["clean_text"] = df["text_combined"].apply(clean_text)

X = df["clean_text"]
y = df["label"]

# Load vectorizer
vectorizer = joblib.load("models/tfidf_vectorizer.pkl")

X = vectorizer.transform(X)

# Split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Load model
model = joblib.load("models/phishing_model.pkl")

# Predict
y_pred = model.predict(X_test)

print("\nModel Evaluation")
print("=" * 50)

print("Accuracy :", accuracy_score(y_test, y_pred))
print("Precision:", precision_score(y_test, y_pred))
print("Recall   :", recall_score(y_test, y_pred))
print("F1 Score :", f1_score(y_test, y_pred))

print("\nConfusion Matrix")
print(confusion_matrix(y_test, y_pred))

print("\nClassification Report")
print(classification_report(y_test, y_pred))