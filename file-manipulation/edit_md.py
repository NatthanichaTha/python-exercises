file = open("./text.md", "r")
content = file.readlines()
new_content = ""

for line in content:
    edited_line = line
    if "## " in edited_line:
        edited_line = edited_line.replace("## ", "<h2>")
        edited_line = edited_line.replace("\n", "</h2>\n")
        new_content += edited_line
        
    elif "# " in edited_line:
        edited_line = edited_line.replace("# ", "<h1>")
        edited_line = edited_line.replace("\n", "</h1>\n")
        new_content += edited_line
    else:
        new_content += edited_line

file = open("./text.md", "w")

for line in new_content:
    file.write(line)



        

