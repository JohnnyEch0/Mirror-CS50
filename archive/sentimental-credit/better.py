

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
print(luhn_valid(number))

