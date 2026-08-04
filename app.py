import streamlit as st
import joblib

from preprocess import clean_text

# Page config
st.set_page_config(
    page_title="Phishing Email Detector",
    page_icon="🛡️",
    layout="wide"
)

# Load model
model = joblib.load(
    "models/phishing_model.pkl"
)

vectorizer = joblib.load(
    "models/tfidf_vectorizer.pkl"
)

st.title("🛡️ AI Phishing Email Detector")

st.markdown(
    "Detect phishing emails using Machine Learning and NLP."
)

email_text = st.text_area(
    "Paste Email Content",
    height=250
)

if st.button("Analyze Email"):

    if email_text.strip():

        cleaned = clean_text(email_text)

        vector = vectorizer.transform(
            [cleaned]
        )

        prediction = model.predict(vector)[0]

        if prediction == 1:

            st.error(
                "⚠️ This email appears to be PHISHING."
            )

        else:

            st.success(
                "✅ This email appears SAFE."
            )

    else:

        st.warning(
            "Please enter email content."
        )