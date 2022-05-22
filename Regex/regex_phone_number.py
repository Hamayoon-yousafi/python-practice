import re
# a regex that extracts phone number from a given string
def extract_phone(input):
    phone_regex = re.compile(r"\d{3} \d{3}-\d{4}")
    match = phone_regex.search(input)
    if not match:
        return None
    return match.group()

# print(extract_phone("my phone number is 432 567-1232. Please call me when you get home."))

def is_valid_phone(input):
    phone_regex = re.compile(r"^\d{3} \d{3}-\d{4}$")
    match = phone_regex.search(input)
    if not match:
        return "Invalid Phone Number!"
    return match.group()

print(is_valid_phone("324 432-2341"))
print(is_valid_phone("324 432-2341 34"))