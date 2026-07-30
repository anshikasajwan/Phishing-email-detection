import joblib

from preprocess import clean_text

# Load model
model = joblib.load("models/phishing_model.pkl")

vectorizer = joblib.load(
    "models/tfidf_vectorizer.pkl"
)

print("=" * 50)
print("PHISHING EMAIL DETECTOR")
print("=" * 50)

email = input("\nEnter Email:\n")

cleaned = clean_text(email)

email_vector = vectorizer.transform([cleaned])

prediction = model.predict(email_vector)[0]

if prediction == 1:
    print("\n⚠️ PHISHING EMAIL DETECTED")
else:
    print("\n✅ SAFE EMAIL")