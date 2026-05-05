import re

# Email validation
def is_valid_email(email):
    pattern = r"[^@]+@[^@]+\.[^@]+"
    return re.match(pattern, email)


# Password validation
def is_valid_password(password):
    # At least 8 chars, 1 letter, 1 number
    if len(password) < 8:
        return False

    has_letter = re.search(r"[A-Za-z]", password)
    has_number = re.search(r"\d", password)

    return bool(has_letter and has_number)


# Required fields validation
def validate_required_fields(data, fields):
    missing = []

    for field in fields:
        if not data.get(field):
            missing.append(field)

    return missing


# Category validation (based on assignment expectation)
ALLOWED_CATEGORIES = [
    "Internship",
    "Full-Time",
    "Part-Time",
    "Volunteer",
    "Contract"
]

def is_valid_category(category):
    return category in ALLOWED_CATEGORIES