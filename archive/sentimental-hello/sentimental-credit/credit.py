from cs50 import get_string

number = get_string("Number: ")
mult = ""
add = 0
mult2 = 0

for i, digit in enumerate(number):
    if i % 2 == 0:
        digit = int(digit) * 2
        mult = str(digit)
        # print("mult", mult)
        for j, digit in enumerate(mult):
            mult2 += int(digit)
            # print("mult2", mult2)
    else:
        add += int(digit)

res = mult2 + add

# amex 15, MC 16, visa 13 and 16
    # print(i, mult2)
