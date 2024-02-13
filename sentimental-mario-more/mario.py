x = 0
while True:
    x = int(input("Height:"))
    if x < 9 and x > 0:
        break
    else:
        print("Usage: int 1-8")

for i in range(x):
    line = str((" " * (x - i-1)) + ("#" * (i+1)) + "  " + ("#" * (i+1)) + (" " * (x - i-1)))
    print(line)
