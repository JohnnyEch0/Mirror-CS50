from cs50 import get_string

number = get_string("Number: ")
length = len(number)
mult = ""
add = 0
mult2 = 0

for i, digit in enumerate(number):
    if i == 0:
        if length % 2 == 0:
            digit = int(digit) * 2
            mult = str(digit)
            for j, digit in enumerate(mult):
                mult2 += int(digit)
        else:
            add += int(digit)
            digit2 = number[-1]
            add += int(digit2)


    elif i * 2 < length:
        digit = number[-2 * i]
        mult = str(digit)
        for j, digit in enumerate(mult):
                mult2 += int(digit)
        if (i*2) + 1 < length:
            digit2 = number[(-2*i) - 1]
            add += int(digit2)

print(mult2, add)

if mult2 + add != 20:
    print("INVALID")
elif number[0] == 4:
    print("VISA")
elif number[0] == 3 and number[1] == 4 or number[1] == 7:
    print("AMEX")
else:
    print("MASTERCARD")

# amex 15, MC 16, visa 13 and 16
# all amex start with 34 or 37
# all visa start with 4
# all mc start with 51, 52, 53, 54 or 55
    # print(i, mult2)
