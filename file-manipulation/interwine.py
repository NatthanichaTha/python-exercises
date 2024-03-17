import sys
arg = sys.argv
file_1 = open(arg[1], "r")
file_2 = open(arg[2], "r")
new_file = open(arg[3], "w")

content_1 = file_1.readlines()
content_2 = file_2.readlines()
new_content = []

i = 0
while i < len(content_1) and i < len(content_2):
    line_1 = content_1[i].replace("\n", "")
    line_2 = content_2[i].replace("\n", "")
    new_content.append(line_1)
    new_content.append(line_2)
    i +=1

for j in range(i, len(content_1)):
    line_1 = content_1[i].replace("\n", "")
    new_content.append(line_1)

for j in range(i, len(content_2)):
    line_2 = content_2[i].replace("\n", "")
    new_content.append(line_2)

new_file.write("\n".join(new_content))
