import re

SUSPICIOUS_KEYWORDS = [
    "verify",
    "account",
    "bank",
    "password",
    "urgent",
    "click",
    "login",
    "confirm",
    "reward",
    "winner",
    "claim",
    "free",
    "gift",
    "security",
    "limited",
    "offer"
]


def count_urls(text):
    urls = re.findall(r"http[s]?://\S+|www\.\S+", text)
    return len(urls)


def count_suspicious_keywords(text):
    text = text.lower()

    count = 0

    for word in SUSPICIOUS_KEYWORDS:
        if word in text:
            count += 1

    return count


def count_uppercase(text):
    return sum(1 for char in text if char.isupper())


def count_exclamations(text):
    return text.count("!")


def email_length(text):
    return len(text)


def extract_features(text):
    return {
        "url_count": count_urls(text),
        "keyword_count": count_suspicious_keywords(text),
        "uppercase_count": count_uppercase(text),
        "exclamation_count": count_exclamations(text),
        "email_length": email_length(text)
    }