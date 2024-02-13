from cs50 import get_string

number = get_string("Number: ")
mult = ""
add = 0
mult2 = 0

for i, digit in enumerate(number):
    if i % 2 == 0:
        mult = str((int(digit*2)))
        for j, digit in enumerate(mult):

            mult2 += int(digit)
            print(mult, mult2)
    else:
        add += int(digit)


    # print(i, mult2)
