import random

board = set()
for i in range(5):
    for j in range(5):
        board.add((i,j))

print(random.choice(list(board)))