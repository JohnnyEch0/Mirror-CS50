from cs50 import get_string

number = get_string("Number: ")
mult = 0
add = 0
for i, digit in enumerate(number):
    if i % 2 == 0:
        mult += int(digit) * 2
        print(mult)
    else:
        add += int(digit)

    print(i)
