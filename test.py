from preprocess import clean_text

email = """
Congratulations!!!

You have WON ₹50,000.

Click here:

https://abc.com

Verify your account NOW!!!

"""

print(clean_text(email))
