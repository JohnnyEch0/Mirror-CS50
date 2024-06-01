import re

# re patterns for easy format checking
visa_pattern = r"^4\d{12}(?:\d{3})?$"
amex_pattern = r"^3[47]\d{13}$"
mastercard_pattern = r"^5[1-5]\d{14}$"

def luhn_valid(number):
    digits = [int(d) for d in number[::-1]]
    # :: omits start and end values, so uses entire string
    # -1 iterates in reverse

    checksum = 0
    for i, digit in enumerate(digits):
        if i % 2 != 0:
            digit *= 2
            if digit > 9:
                # clever trick, if digit*2 is more then one digit, substract 9 to get quersum
                digit -= 9
        checksum += digit
    return checksum % 10 == 0


number = input("Number: ")
if luhn_valid(number):
    if re.match(visa_pattern, number):
        print("VISA")
    elif re.match(amex_pattern, number):
        print("AMEX")
    elif re.match(mastercard_pattern, number):
        print("MASTERCARD")
    else:
        print("INVALID")
else:
    print("INVALID")


