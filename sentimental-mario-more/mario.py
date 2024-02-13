from cs50 import get_int
x = 0
while True:
    x = get_int("Height:")

    if x < 9 and x > 0:
        break
    else:
        print("Usage: int 1-8")

for i in range(x):
    line = str((" " * (x - i-1)) + ("#" * (i+1)) + "  " + ("#" * (i+1)))
    print(line)
