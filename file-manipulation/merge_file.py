import sys
argument = sys.argv
to_merge_1 = open(argument[1], "r")
to_merge_2 = open(argument[2], "r")
new_file = open(argument[3], "w")

content_1 = to_merge_1.read()
content_2 = to_merge_2.read()
new_file.write(content_1 + content_2)

