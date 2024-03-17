import sys
arg = sys.argv
file = open(arg[1], "r")
text_to_find = arg[2]
text_len = len(text_to_find)
content = file.read()
count_text = 0

for i in range(len(content) - text_len + 1):
    #print(content[i:i+text_len])
    if content[i:i+text_len] == text_to_find:
        count_text += 1
print(count_text)