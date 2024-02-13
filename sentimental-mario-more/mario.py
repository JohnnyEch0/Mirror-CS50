x = 0
while (x < 9 and x > 1):
    x = int(input("Height:"))

for i in range(x):
    line = str((" " * (x - i)) + ("#" * x) + "  " + ("#" * x) + (" " * (x - i)))
    print(line)
