import os

for i in range(1):
    directory = os.path.join(os.path.curdir,"gtsrb", f"{i}")
    for filename in os.listdir(directory):
        file = os.path.join(directory, filename)

        if os.path.isfile(file):
            print(file)
   