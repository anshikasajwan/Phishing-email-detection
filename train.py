import pandas as pd
import joblib

from preprocess import clean_text

from sklearn.model_selection import train_test_split

from sklearn.feature_extraction.text import TfidfVectorizer

from sklearn.linear_model import LogisticRegression

from sklearn.naive_bayes import MultinomialNB

from sklearn.svm import LinearSVC

from sklearn.metrics import accuracy_score

df = pd.read_csv("dataset/phishing_emails.csv")

print("\nColumns:")
print(df.columns)

print("\nFirst 5 rows:")
print(df.head())

df.dropna(inplace=True)

df["clean_text"] = df["text_combined"].apply(clean_text)

y = df["label"]

X = df["clean_text"]

y = df["label"]

vectorizer = TfidfVectorizer(max_features=5000)

X = vectorizer.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

models = {
    "Logistic Regression": LogisticRegression(max_iter=1000),
    "Naive Bayes": MultinomialNB(),
    "Linear SVM": LinearSVC()
}

best_accuracy = 0
best_model = None
best_model_name = ""

for name, model in models.items():

    model.fit(X_train, y_train)

    predictions = model.predict(X_test)

    accuracy = accuracy_score(y_test, predictions)

    print(f"{name}: {accuracy:.4f}")

    if accuracy > best_accuracy:
        best_accuracy = accuracy
        best_model = model
        best_model_name = name

joblib.dump(best_model, "models/phishing_model.pkl")

joblib.dump(vectorizer, "models/tfidf_vectorizer.pkl")

print("\nBest Model:", best_model_name)
print("Accuracy:", best_accuracy)