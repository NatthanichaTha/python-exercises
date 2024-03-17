import sys
argument = sys.argv
filepath = argument[1]
new_content = argument[2]
pos = int(argument[3])

file = open(filepath, "r+")
old_content = file.read()

file.seek(pos, 0)
file.write(new_content + old_content[pos:])