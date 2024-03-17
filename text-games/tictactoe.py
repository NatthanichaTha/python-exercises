import os
from input_utils import input_int

class Board:
    def __init__(self):
        # Create a 9 item list initialized to all zeros
        self.board = [0]*9

    def __repr__(self):
        # Print the board this way
        # 0 0 0
        # 0 0 0
        # 0 0 0

        board_string = ""
        for i in range(len(self.board)):
            sign = " "
            if self.board[i] == 1:
                sign = "x"
            elif self.board[i] == 2:
                sign = "o"
    
            if (i+1) % 3 != 0:
                board_string += " " + sign + " |"
            else:
                board_string += " " + sign + "\n"
                if i != len(self.board)-1:
                    board_string += " - - - - - " + "\n"

        return board_string

    def is_empty(self, cell_idx: int) -> bool:
        # Return true if board at the specified cell is empty. False otherwise
        if self.board[cell_idx] != 0:
            return False
        return True

    def move(self, cell_idx: int, player: int):
        # player can be either 1 or 2
        # make the move for player on the board at the
        # specified index.
        self.board[cell_idx] = player

    def check_win(self):
        # Return 0 if the game is finished in a draw. 1 if the player 1 wins,
        # 2 if the player 2 wins. -1 if the game is still ongoing.
        
        for i in range(0, len(self.board), 3):
            #check win on the horizontal
            if self.board[i] != 0:
                if self.board[i] == self.board[i+1] == self.board[i+1+1]:
                    return self.board[i]
        for i in range(3):
            #check win on the vertical
            if self.board[i] != 0:
                if self.board[i] == self.board[i+3] == self.board[i+3+3]:
                    return self.board[i]
        
        if self.board[i] != 0 and self.board[0] == self.board[4] == self.board[8]:
            return self.board[0]
        if self.board[i] != 0 and self.board[2] == self.board[4] == self.board[6]:
            return self.board[2]

        if 0 not in self.board:
            return 0
        
        return -1

if __name__ == "__main__":
    board = Board()
    player = 1

    while board.check_win() == -1:
        os.system('clear')
        print(board)
        curr_player_input = input_int(f"Player {player}: make a move --> ") - 1
        while curr_player_input < 0 or curr_player_input > 8 or not board.is_empty(curr_player_input):
            print("Please choose the empty cell!")
            curr_player_input = input_int(f"Player {player}: make a move --> ") - 1
        
        board.move(curr_player_input, player)
        os.system('clear')
        print(board)
        player = 2 if player == 1 else 1
    
    if board.check_win() == 0:
        print("The game ended in a draw")
    else:
        print(f"Player {board.check_win()} wins!")