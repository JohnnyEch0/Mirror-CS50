import cs50
text = cs50.get_string("Text: ")
sentences = 0
words = 0

for c in text:
    if c == "." or c == "?" or c == "!":
        sentences +=1
    elif c == " ":
        words += 1

print(sentences)
