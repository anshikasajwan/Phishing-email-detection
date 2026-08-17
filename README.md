# 🛡️ AI-Powered Phishing Email Detection System

## 📌 Project Overview

The **AI-Powered Phishing Email Detection System** is a machine learning-based cybersecurity application designed to identify potentially phishing emails.

The system uses **Natural Language Processing (NLP)** and a **fine-tuned DistilBERT transformer model** to analyze the textual content of an email and classify it into one of two categories:

- **Phishing**
- **Legitimate**

A simple **Streamlit web application** is provided for users to enter an email and receive a prediction from the trained machine learning model.

The project demonstrates the practical application of **Machine Learning, Natural Language Processing, Deep Learning, and Cybersecurity** for detecting phishing emails.

---

# 🎯 Objectives

* Detect potentially phishing emails using machine learning.
* Apply Natural Language Processing to email text.
* Fine-tune a DistilBERT model for email classification.
* Prepare and process labelled email datasets.
* Evaluate the trained model using standard classification metrics.
* Perform error analysis on incorrect predictions.
* Provide a simple interface for real-time email classification.
* Demonstrate the application of machine learning in cybersecurity.

---

# ✨ Features

* ✅ Email text preprocessing
* ✅ Natural Language Processing (NLP)
* ✅ Transformer-based text classification
* ✅ Fine-tuned DistilBERT model
* ✅ Binary email classification
* ✅ Phishing / Legitimate prediction
* ✅ Prediction confidence score
* ✅ Accuracy evaluation
* ✅ Precision evaluation
* ✅ Recall evaluation
* ✅ F1-Score evaluation
* ✅ Confusion Matrix
* ✅ Classification Report
* ✅ Error analysis
* ✅ Real-world email evaluation
* ✅ Simple Streamlit interface
* ✅ Local trained model inference

---

# 🛠️ Technologies Used

* Python
* PyTorch
* Hugging Face Transformers
* DistilBERT
* Pandas
* NumPy
* Scikit-learn
* Streamlit
* Natural Language Processing (NLP)

---

# 📂 Project Structure

```text
Phishing-email-detection/
│
├── app.py
├── README.md
├── LICENSE
├── .gitignore
│
├── dataset_v2/
│   ├── train.csv
│   ├── validation.csv
│   └── test.csv
│
├── models/
│   └── tokenizer/
│       ├── special_tokens_map.json
│       ├── tokenizer.json
│       ├── tokenizer_config.json
│       └── vocab.txt
│
├── src/
│   ├── add_realistic_data.py
│   ├── app.py
│   ├── evaluate.py
│   ├── evaluate_real.py
│   ├── feature_engineering.py
│   ├── predict.py
│   ├── preprocess.py
│   ├── sender_verification.py
│   ├── train.py
│   └── utils.py
│
├── generate_dataset.py
├── test.py
└── test_features.py
