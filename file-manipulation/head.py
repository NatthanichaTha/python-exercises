import sys

argument = sys.argv
filepath = sys.argv[1]
file = open(filepath, "r")
mode = sys.argv[2]
lines = int(sys.argv[3]) if len(sys.argv) > 3 else 10

if mode == "head":
    for i in range(lines):
        content = file.readline()
        if content:
            print(content)
        else:
            break

elif mode == "tail":
    content = file.readlines()
    print("n/".join(content[-lines:]))



