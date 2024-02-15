import cs50

text = cs50.get_string("Text: ")
sentences = 0
spaces = 0
letters = 0
length = len(text)

for c in text:
    if c == "." or c == "?" or c == "!":
        sentences += 1
    elif c == " ":
        spaces += 1
    elif c.isalpha:
        letters += 1

words = spaces+1
print(words, letters, sentences)

av_word_length = (letters) / words * 100 # letters?
sen_p_words = sentences / words * 100
# print(av_word_length, sen_p_words)

cl_index = round(0.0588 * av_word_length - 0.296 * sen_p_words - 15.8)

if cl_index < 1:
    print("Before Grade 1")
elif cl_index > 16:
    print("Grade 16+")
else:
    print(f"Grade {cl_index}")

# 0.0588 * L - 0.296 * S - 15.8, where L is the average number of letters per 100 words in the text, and S is the average number of sentences per 100 words in the text.

# 62 until bank
# 22 until to do
# 53 until reading
# 
