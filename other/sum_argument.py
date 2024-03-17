import sys

argument = sys.argv[1:]
total = 0
for item in argument:
    total += int(item)
print(total)