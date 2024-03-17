from random import randint
from input_utils import input_menu
    
def game():
    gamechoice = ["Rock", "Paper", "Scissor"]
    chances = 5
    user_score = 0
    pc_score = 0
    for i in range(chances):
        pc_choice = randint(0, len(gamechoice)-1)
        user_choice = input_menu(gamechoice)
        if user_choice == pc_choice:
            user_score += 0
            pc_score += 0
        elif (user_choice == 0 and pc_choice == 1) or (user_choice == 1 and pc_choice == 2) or (user_choice == 3 and pc_choice == 0):
            pc_score += 1
        else:
            user_score += 1

        print("You:", gamechoice[user_choice], "/", "PC:", gamechoice[pc_choice])
        print("Your score:", user_score, "/", "Pc score:", pc_score)
        if user_score > chances/2:
            print("Congratulations. You win!")
            return
        elif pc_score > chances/2:
            print("You loss.")
            return
    print("Tie.")

menu_list = ["New game", "Exit"]
user_choice = input_menu(menu_list) 
while user_choice != 1:    
    game()
    user_choice = input_menu(menu_list) 
     