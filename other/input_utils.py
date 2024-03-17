#take string as input and return integer 
#if the user didn't insert integer, ask for input as integer again
from datetime import datetime

def input_int(prompt=""):
    string = input(prompt)
    while not string.isnumeric():
        print("Incorrect input type. Please insert numbers.")
        string = input(prompt)
            
    return int(string)

def input_choice(prompt:str, choices:list):
    string = input(prompt)
    while string not in choices:
        print("Incorrect input type. Please only insert a value in ", choices)
        string = input(prompt)
    return string

def print_menu(menu_choices:list[str]):
    for i, choice in enumerate(menu_choices):
        print(i+1, ")", choice)

def input_menu(menu_choices:list[str]):
    print_menu(menu_choices)
    user_choice = input_int()
    while user_choice > len(menu_choices) or user_choice < 1:
        print("Incorrect input type. Please only insert a value in 1 -", len(menu_choices))
        print_menu(menu_choices)
        user_choice = input_int()
    return user_choice-1 

def input_date(prompt, seperator="/"):
    user_input = input(prompt)
    
    while True:
        try:
            split_input = user_input.split(seperator)
            day = int(split_input[0])
            month = int(split_input[1])
            year = int(split_input[2])
            in_date = datetime(year, month, day)
            break
        except:
            print("Date is not valid. Please try again.")
            user_input = input(prompt)
    return in_date









    




   









