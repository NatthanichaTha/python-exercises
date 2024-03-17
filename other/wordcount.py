#count the specific word in the sentence

sentence = input("Insert the sentence: ").lower()
word_to_count = input("Insert the word that you want to count: ").lower()

count = 0

corrected_sentence = ""
for i in range(len(sentence)):
    if sentence[i].isalpha() or sentence[i] == " ":
        corrected_sentence += sentence[i]
    else:
        corrected_sentence += " "

words = corrected_sentence.split(" ")

for i in range(len(words)):
    if word_to_count in words[i]:
        count += 1

print(count)


    