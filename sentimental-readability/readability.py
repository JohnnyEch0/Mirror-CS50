import cs50
text = cs50.get_string("Text: ")
sentences = 0
words = 0
letters = 0

for c in text:
    if c == "." or c == "?" or c == "!":
        sentences +=1
    elif c == " ":
        words += 1
    else:
        letters +=1

cl_index = 

# 0.0588 * L - 0.296 * S - 15.8, where L is the average number of letters per 100 words in the text, and S is the average number of sentences per 100 words in the text.
print(sentences)
