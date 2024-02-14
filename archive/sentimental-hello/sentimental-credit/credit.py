from cs50 import get_string

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
        # get 
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
elif (int(number[0])) == 4 and (length == 13 or length == 16):
    print("VISA")
elif int(number[0]) == 3 and int(number[1] == 4 or int(number[1]) == 7) and length == 15:
    print("AMEX")
else:
    if length == 16 and int(number[0]) == 5 and int(number[1]) < 6:
        print("MASTERCARD")
    else:
        print("INVALID")
