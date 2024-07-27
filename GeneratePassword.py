import re
import secrets
import string


def generate_password(length=16, nums=1, special_chars=1, uppercase=1, lowercase=1):
    # Define the possible characters for the password
    letters = string.ascii_letters  # Includes both uppercase and lowercase letters
    digits = string.digits  # Includes numeric digits from 0 to 9
    symbols = string.punctuation  # Includes special characters like !, @, #, etc.

    # Combine all characters to form the pool from which to draw password characters
    all_characters = letters + digits + symbols

    while True:
        password = ''
        # Generate password by randomly selecting characters from the combined pool
        for _ in range(length):
            password += secrets.choice(all_characters)
            # secrets.choice ensures cryptographically secure random
            # selection

        # Define constraints for the password
        constraints = [
            (nums, r'\d'),  # At least `nums` number of digits
            (special_chars, fr'[{symbols}]'),  # At least `special_chars` number of special characters
            (uppercase, r'[A-Z]'),  # At least `uppercase` number of uppercase letters
            (lowercase, r'[a-z]')  # At least `lowercase` number of lowercase letters
        ]

        # Check if the generated password meets all constraints
        if all(
                constraint <= len(re.findall(pattern, password))
                # Use regular expressions to find matches for each constraint
                for constraint, pattern in constraints
        ):
            break  # If all constraints are met, exit the loop

    return password  # Return the generated password that meets all specified constraints


if __name__ == '__main__':
    new_password = generate_password()
    print('Generated password:', new_password)
