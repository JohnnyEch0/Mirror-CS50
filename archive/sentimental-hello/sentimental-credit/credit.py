from cs50 import get_string

number = get_string("Number: ")
mult = ""
add = 0
for i, digit in enumerate(number):
    if i % 2 == 0:
        mult += (digit)
        # print(mult, i)
    else:
        add += int(digit)
mult2 = 0
for i, digit in enumerate(mult):
    mult2 += int(digit)*2
    print(i, mult2)
