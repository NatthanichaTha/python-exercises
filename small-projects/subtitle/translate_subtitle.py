from deep_translator import GoogleTranslator
import sys 


filepath = sys.argv[1]
target_lang_code = sys.argv[2]
file = open(filepath, "r")
translated_content = []

for line in file.readlines()[:15]:
    if line == "\n" or " --> " in line or line.isnumeric():
        translated_content.append(line)
    else: 
        translated_line = GoogleTranslator("auto", target_lang_code).translate(line.replace("\n", ""))
        translated_content.append(translated_line + "\n")

translated_file = open(filepath.replace(".srt", "."+target_lang_code+".srt"), "w")

for line in translated_content:
    translated_file.write(line)
