def verify_card_number(card_number):
    sum_of_odd_digits = 0
    card_number_reversed = card_number[::-1]
    odd_digits = card_number_reversed[::2]

    for digit in odd_digits:
        sum_of_odd_digits += int(digit)

    sum_of_even_digits = 0
    even_digits = card_number_reversed[1::2]
    for digit in even_digits:
        number = int(digit) * 2
        if number >= 10:
            number = (number // 10) + (number % 10)
        sum_of_even_digits += number
    total = sum_of_odd_digits + sum_of_even_digits

    return total % 10 == 0


def main():
    card_number = '4111-1111-4555-111'
    # The maketrans function is used to create a translation table that maps each character in the first argument into
    # the character at the same position in the second argument.
    card_translation = str.maketrans({'-': '', ' ': ''})
    # The 'translate' method is used to translate the characters in the string using the translation table created with

    translated_card_number = card_number.translate(card_translation)

    if verify_card_number(translated_card_number):
        print('VALID!')
    else:
        print('INVALID!')


if __name__ == '__main__':
    main()
