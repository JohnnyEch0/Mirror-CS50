from cs50 import get_string
# credit in python, it's not pretty, it's porpably not the best, but it works.

number = get_string("Number: ")
length = len(number)
# print("Length: ", length)
mult = ""
add = 0
mult2 = 0

for i, digit in enumerate(number):
    # uneven and even numbers need to be processed differently
    # this we do in the first iteration
    # also we're doin a whole lot of weird typecasting!
    if i == 0:
        # if it is even
        if length % 2 == 0:
            # first character of number
            # multiply by 2 and add seperated digits to the mult integer
            digit_3 = int(digit) * 2
            mult = str(digit_3)
            for j, digit_j in enumerate(mult):
                mult2 += int(digit_j)
            # add the last character to the add integer
            digit2 = number[-1]
            add += int(digit2)
        # if it is uneven
        else:
            # add first and last character to the add int
            add += int(digit)
            digit2 = number[-1]
            add += int(digit2)

    # now all the other characters
    # as were working in 2*i indexes of the number now,
        # check if this is even in range
    elif i * 2 < length:
        # starting from the second last character
        # get char at [-2 * i] and do the mult computation
        digit = int(number[-2 * i]) * 2
        mult = str(digit)
        for j, digit_j in enumerate(mult):
            mult2 += int(digit_j)

        # get char at [-2 * i - 1]
            # if possible
        if (i*2) + 1 < length:
            # add it to add int
            digit2 = number[(-2*i) - 1]
            add += int(digit2)


# check if the verification formular works
if (mult2 + add) % 10 != 0:
    print("INVALID")
# check if its VISA, AMEX, MC or INVALID
    # via length and starting numbers
elif (int(number[0])) == 4 and (length == 13 or length == 16):
    print("VISA")
elif int(number[0]) == 3 and int(number[1] == 4 or int(number[1]) == 7) and length == 15:
    print("AMEX")
else:
    if length == 16 and int(number[0]) == 5 and int(number[1]) < 6:
        print("MASTERCARD")
    else:
        print("INVALID")
