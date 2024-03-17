string = input("Please insert anything: ")

def count_letter_digit(s):
    letter = 0
    digit = 0
    for char in s:
        if char.isalpha():
            letter += 1
        if char.isnumeric():
            digit += 1

    return letter, digit

letter, digit = count_letter_digit(string)
print("Number of letters: ", letter, "Number of digits: ", digit)