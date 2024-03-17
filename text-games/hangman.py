import os
import random

class Hangman:
    def __init__(self):
        self.word = self.get_random_word()
        self.life = 6
        self.userguess = ["_"]*len(self.word)
    
    def get_random_word(self):
        word_file = open("../../Downloads/hangman_words.txt")
        word_list = word_file.readlines()
        word = word_list[random.randint(0, len(word_list)-1)].replace("\n", "")
        while len(word) < 4:
            word = random.randint(0, len(word_list)-1).replace("\n", "")
        return word
    
    def print_hangman(self):
        if self.life == 6:
            print("_________ \n"+
                "|       |\n"+      
                "|        \n"+
                "|        \n"+
                "|        \n"+
                "|               ") 
        elif self.life == 5:
            print("_________ \n"+
                "|       |\n"+      
                "|       O \n"+
                "|        \n"+
                "|        \n"+
                "|               ") 
        elif self.life == 4:
            print("_________ \n"+
                "|       |\n"+      
                "|       O \n"+
                "|       | \n"+
                "|        \n"+
                "|               ") 
        elif self.life == 3:
            print("_________ \n"+
                "|       |\n"+      
                "|       O \n"+
                "|      /| \n"+
                "|        \n"+
                "|               ") 
        elif self.life == 2:
            print("_________ \n"+
                "|       |\n"+      
                "|       O \n"+
                "|      /|\ \n"+
                "|        \n"+
                "|               ")  
        elif self.life == 1:
            print("_________ \n"+
                  "|       |\n"+      
                  "|       O \n"+
                    "|      /|\ \n"+
                   "|       / \n"+
                   "|               ")  
        elif self.life == 0:
            print("_________ \n"+
                  "|       |\n"+      
                  "|       O \n"+
                    "|      /|\ \n"+
                   "|       /\ \n"+
                   "|               ")     
        print("\n" + " ".join(self.userguess))

    def check_letter(self, given_letter):
        if given_letter in self.word:
            for i, char in enumerate(self.word):
                if char == given_letter:
                    self.userguess[i] = given_letter

        elif given_letter not in self.word:
            self.life -= 1
    
    def get_letter(self):
        given_letter = input("Guess the letter(a-z): ")
        while not given_letter.isalpha():
            print(given_letter + "is not an alphabet. Try again.")
            given_letter = input("Guess the letter(a-z): ")

        while given_letter in self.userguess:
            print(given_letter + "is taken. Choose a new letter.")
            given_letter = input("Guess the letter(a-z): ")
        
        return given_letter 
    
    def check_win(self):
        if self.life > 0 and "".join(self.userguess) == self.word:
            return 1
        elif self.life == 0 and "".join(self.userguess) != self.word:
            return -1
        return 0
    
if __name__ == "__main__":
    hangman = Hangman()
    while hangman.check_win() == 0:
        os.system("clear")
        hangman.print_hangman()
        given_letter = hangman.get_letter()
        hangman.check_letter(given_letter)
        if hangman.check_win() == -1:
            os.system("clear")
            hangman.print_hangman()
            print("You lose. The correct word is " + hangman.word)
        elif hangman.check_win() == 1:
            os.system("clear")
            hangman.print_hangman()
            print("Congratulations. You win.")
            