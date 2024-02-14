import cs50
import math

text = cs50.get_string("Text: ")
sentences = 0
spaces = 0
letters = 0
length = len(text)

for c in text:
    if c == "." or c == "?" or c == "!":
        sentences +=1
    elif c == " ":
        spaces += 1
    else:
        letters +=1

words = spaces+1

av_word_length = (length - spaces - sentences) / words * 100
sen_p_words = sentences / words * 100
cl_index = math.ceil(0.0588 * av_word_length - 0.296 * sen_p_words - 15.8)

if cl_index < 1:
    print("Before Grade 1")
elif cl_index > 16:
    print("Grade 16+")
else:
    print(f"Grade {cl_index}")

# 0.0588 * L - 0.296 * S - 15.8, where L is the average number of letters per 100 words in the text, and S is the average number of sentences per 100 words in the text.

