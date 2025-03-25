import cs50

while True:
    try:
        card_number = cs50.get_string("Card Number: ")
        if card_number.isdigit() and int(card_number) and 13 <= len(card_number) <= 16:
            break
    except ValueError:
        pass

card_number = int(card_number)

#amex (15 digits - starts with 34 or 37) ; mastercard (16 digits - starts with 51,52,53,54,55) ; visa (13 and 16 digits - starts with 4)

luhn_sum = 0
length = len(str(card_number))
start_digits = int(str(card_number)[:2])
first_digit = int(str(card_number)[0])

card_number_str = str(card_number)
reverse_digits = card_number_str[::-1]

for i, digit in enumerate(reverse_digits):
    n = int(digit)
    if i % 2 == 1:
        n *= 2
    if n > 9:
        n = n // 10 + n % 10
    luhn_sum += n

# Check validity using Luhn's algorithm
if luhn_sum % 10 == 0:  # Valid card number
    # Identify card type
    if length == 15 and (start_digits == 34 or start_digits == 37):
        print("AMEX")
    elif length == 16 and 51 <= start_digits <= 55:
        print("MASTERCARD")
    elif (length == 13 or length == 16) and first_digit == 4:
        print("VISA")
    else:
        print("INVALID")  # Doesn't match known patterns
else:
    print("INVALID")  # Fails Luhn's algorithm
