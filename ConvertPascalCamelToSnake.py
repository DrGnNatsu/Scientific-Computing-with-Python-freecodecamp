def convert_to_snake_case(pascal_or_camel_cased_string):
    # Convert PascalCase or camelCase to snake_case

    # Input String: The function accepts a string that is either in
    # PascalCase (where each word starts with a capital letter and there are no spaces, e.g., PascalCaseString) or
    # camelCase (the first word is lowercase, and subsequent words start with a capital letter, e.g.,
    # camelCaseString).

    # List Comprehension: It uses a list comprehension to iterate over each character in the input string.
    # Condition Check: For each character (char) in the input string,
    # it checks if the character is uppercase (char.isupper()).
    # If the character is uppercase, it prepends an underscore ('_') to the character and converts it to lowercase (
    # char.lower()). This is done to separate words in snake_case format.
    # If the character is not uppercase, it is left unchanged.

    # Joining Characters: The list of characters (now potentially with underscores and
    # lowercase letters) is joined back together into a single string using ''.join(snake_cased_char_list). .

    # Stripping Leading Underscore: Finally, any leading underscore that might have
    # been added (in case the first character of the input string was uppercase) is removed using .strip('_').
    snake_cased_char_list = [
        '_' + char.lower() if char.isupper()
        else char
        for char in pascal_or_camel_cased_string
    ]

    return ''.join(snake_cased_char_list).strip('_')


# Test
if __name__ == '__main__':
    print(convert_to_snake_case('camelCaseString'))  # camel_case_string
    print(convert_to_snake_case('PascalCaseString'))  # pascal_case_string
    print(convert_to_snake_case('snake_case_string'))  # snake_case_string
