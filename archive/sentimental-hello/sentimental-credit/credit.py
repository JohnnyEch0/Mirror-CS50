from cs50 import get_string

number = get_string("Number: ")
length = len(number)
print("Length: ", length)
mult = ""
add = 0
mult2 = 0

for i, digit in enumerate(number):
    if i == 0:
        if length % 2 == 0:
            digit_3 = int(digit) * 2
            mult = str(digit_3)
            for j, digit_j in enumerate(mult):
                mult2 += int(digit_j)
                # print("case 0: digit to mult", digit_j, "from", digit)

        else:
            add += int(digit)
            # print("case 0: first digit to add", digit)
            digit2 = number[-1]
            # print("case 0: last digit to add", digit2)
            add += int(digit2)

        # print("Case 0:", add, mult2)


    elif i * 2 < length:
        digit = int(number[-2 * i]) * 2
        mult = str(digit)
        for j, digit_j in enumerate(mult):
                mult2 += int(digit_j)
                # print("digit to mult2", digit_j, "from", digit)
        if (i*2) + 1 < length:
            digit2 = number[(-2*i) - 1]
            # print("digit to add", digit2)
            add += int(digit2)


# print(add, mult2)

if (mult2 + add) % 10 != 0:
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
