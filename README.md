# 🛡️ AI-Powered Phishing Email Detection System

## 📌 Project Overview

The **AI-Powered Phishing Email Detection System** is a machine learning application that detects phishing emails using Natural Language Processing (NLP) and supervised learning techniques. It analyzes email content, URLs, suspicious keywords, and other textual features to determine whether an email is **Phishing** or **Safe**.

The project demonstrates how machine learning can be applied in cybersecurity to improve email security by automatically identifying potentially malicious messages.

---

# 🎯 Objectives

* Detect phishing emails using machine learning.
* Train a classification model on phishing and legitimate emails.
* Extract meaningful textual and URL-based features.
* Evaluate model performance using standard classification metrics.
* Provide real-time predictions through an interactive application.

---

# ✨ Features

* ✅ Email text preprocessing
* ✅ Natural Language Processing (NLP)
* ✅ TF-IDF feature extraction
* ✅ Suspicious keyword detection
* ✅ URL detection and analysis
* ✅ Machine learning-based email classification
* ✅ Confidence score prediction
* ✅ Accuracy, Precision, Recall, and F1-Score evaluation
* ✅ Confusion Matrix visualization
* ✅ Interactive user interface (Streamlit)
* ✅ Model persistence using Joblib

---

# 🛠️ Technologies Used

* Python
* Scikit-learn
* Pandas
* NumPy
* NLTK
* Regular Expressions (`re`)
* Matplotlib
* Seaborn
* Joblib
* Streamlit

---

# 📂 Project Structure

```text
AI-Phishing-Detection/
│
├── app.py
├── train.py
├── predict.py
├── preprocess.py
├── feature_engineering.py
├── evaluate.py
│
├── dataset/
│   └── phishing_emails.csv
│
├── models/
│   ├── phishing_model.pkl
│   └── tfidf_vectorizer.pkl
│
├── reports/
│   ├── confusion_matrix.png
│   └── classification_report.txt
│
├── notebooks/
│   └── exploratory_data_analysis.ipynb
│
├── requirements.txt
├── README.md
└── LICENSE
```

---

# ⚙️ How It Works

1. Load a labeled phishing email dataset.
2. Clean and preprocess email text.
3. Extract textual and structural features.
4. Convert text into numerical vectors using TF-IDF.
5. Train multiple machine learning models.
6. Evaluate each model using classification metrics.
7. Save the best-performing model.
8. Accept user input for real-time email classification.
9. Predict whether the email is **Phishing** or **Safe**.
10. Display confidence score and prediction results.

---

# 🔍 Feature Extraction

The system analyzes several features, including:

* Email body text
* URL count
* Suspicious keywords
* Email length
* Number of hyperlinks
* Uppercase letter frequency
* Special character usage
* Punctuation patterns

---

# 🤖 Machine Learning Models

The project compares multiple supervised learning algorithms:

* Multinomial Naive Bayes
* Logistic Regression
* Random Forest Classifier
* Linear Support Vector Machine (SVM)

The best-performing model is selected based on evaluation metrics.

---

# 📊 Model Evaluation

The model is evaluated using:

* Accuracy
* Precision
* Recall
* F1-Score
* Confusion Matrix
* Classification Report

---

# 📈 Sample Output

```text
======================================
AI PHISHING EMAIL DETECTION SYSTEM
======================================

Enter Email:

Congratulations!

You have won a prize.

Click the link below to claim your reward.

Prediction

⚠️ PHISHING

Confidence Score

98.7%

Detected Indicators

✓ Suspicious keywords
✓ URL detected
✓ Promotional language
```

---

# 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/anshikasajwan/Phishing-email-detection.git
```

Navigate to the project directory:

```bash
cd Phishing-email-detection
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

Run the training script:

```bash
python train.py
```

Launch the application:

```bash
streamlit run app.py
```

---

# 📚 Learning Outcomes

This project helps develop practical knowledge of:

* Machine Learning
* Natural Language Processing (NLP)
* Text Classification
* Feature Engineering
* Cybersecurity
* Phishing Detection
* Model Evaluation
* Data Visualization
* Secure Software Development

---

# 🚀 Future Enhancements

* Deep learning models (LSTM, BERT)
* Email attachment analysis
* URL reputation checking
* Real-time email monitoring
* Browser extension integration
* REST API deployment
* Cloud deployment
* Multi-language phishing detection
* Explainable AI (XAI) for prediction transparency

---

# 👨‍💻 Author

**Name:** *Anshika Sajwan*

**Project:** AI-Powered Phishing Email Detection System

**Language:** Python

---

# 📜 License

This project is developed for educational and research purposes. It demonstrates how machine learning and Natural Language Processing can be applied to detect phishing emails and improve cybersecurity awareness.
