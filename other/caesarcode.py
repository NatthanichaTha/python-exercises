from input_utils import input_int, input_choice

def caesar_cypher(text: str, code: int):
    crack = ""
    for char in text:
        if char.isalpha():
            crack += chr((ord(char)+code))
        else:
            crack += char
    return crack


text = input("Please enter the text: ")
code = input_int("Please enter the code(1-25): ")
action = input_choice("Cypher or Decypher?(C/D)", ["C", "D"])

if action == "D":
    code = -code

print(caesar_cypher(text, code))

#ord("a") = 97
#chr(97) = "a"



