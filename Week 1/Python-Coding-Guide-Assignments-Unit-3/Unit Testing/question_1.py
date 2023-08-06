'''
Create a function that validates email addresses based on following set of rules:
- Proper email format such as presence of “@”, no space in the address
- Presence of valid email providers such as yahoo, gmail and outlook. Make sure
there are no no disposable email providers such as yopmail.
Write unit tests to validate different email addresses against the rules, including valid and
invalid addresses (Use unittest module).
'''

import re
import unittest

def validate_email(email: str) -> bool:
    """
    Validate an email address based on specific rules.

    Args:
        email (str): The email address to be validated.

    Returns:
        bool: True if the email address is valid, False otherwise.
    """
    # Proper email format check
    if not re.match(r'^\S+@\S+\.\S+$', email):
        return False

    # Valid email providers check
    valid_providers = ['yahoo', 'gmail', 'outlook']
    email_provider = email.split('@')[1].split('.')[0]
    if email_provider not in valid_providers:
        return False

    # No disposable email providers check
    if "yopmail" in email:
        return False

    return True

class TestEmailValidation(unittest.TestCase):

    def test_valid_emails(self):
        self.assertTrue(validate_email('a.b@gmail.com'))
        self.assertTrue(validate_email('hi.hello@yahoo.com'))
        self.assertTrue(validate_email('rame.shyame@outlook.com'))

    def test_invalid_emails(self):
        self.assertFalse(validate_email('invalid-email'))
        self.assertFalse(validate_email('a.b@invalid.com'))
        self.assertFalse(validate_email('hi.hello@yopmail.com'))
        self.assertFalse(validate_email('rame.shyame@disposable.com'))

if __name__ == "__main__":
    unittest.main()