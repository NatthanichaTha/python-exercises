from input_utils import input_menu, input_int
from random import randint

def game():
    number_to_guess = randint(0, 100)
    attemps = 0
    user_guess = None
    while user_guess != number_to_guess:
        user_guess = input_int("Guess the number: ")
        if user_guess < number_to_guess:
            print("No. It's greater. Try again!")
        elif user_guess > number_to_guess:
            print("No. It's lower. Try again!")        
        attemps += 1
    print("Correct answer! Attemps: ", attemps)

menu_list = ["New game", "Exit"]
user_choice = input_menu(menu_list) 
while user_choice != 1:    
    game()
    user_choice = input_menu(menu_list) 
        


