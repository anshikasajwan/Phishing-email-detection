from feature_engineering import extract_features

email = """
URGENT!

Verify your account immediately.

Click here:
https://bank.com/login

Congratulations!
"""

features = extract_features(email)

print(features)
