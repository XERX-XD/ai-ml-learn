spam_emails = [
    "Congratulations! You have won NPR 500,000. Claim your prize now!",
    "URGENT: Your bank account has been suspended. Verify immediately.",
    "You have been selected to receive a free iPhone. Click here to claim it.",
]

for email in spam_emails:
    if "Congratulations" in email or "suspended" in email or "free" in email:
        print("spam mail",email)
    else:
        print("not spam",email)