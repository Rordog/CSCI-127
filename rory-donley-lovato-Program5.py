import numpy as np
import string

# ---------------------------------------
# CSCI 127, Joy and Beauty of Data      |
# Program 5: DigiPeg Solitaire          |
# Rory Donley-Lovato                    |
# Last Modified: November 18, 2020      |
# ---------------------------------------
# Creates an interactive DigiPeg game
# that uses user inputs to move around
# pegs on a board size of the user's
# choosing.
# ---------------------------------------

# ---------------------------------------
# Start of DigiPeg Class                |
# ---------------------------------------

class DigiPeg:

    def __init__(self, rows, columns, empty_row, empty_col):
        self.board = np.full((rows, columns), True)
        self.board[empty_row][empty_col] = False
        self.pegs_left = rows * columns - 1
        self.rows = rows
        self.columns = columns
# ---------------------------------------

    def __str__(self):
        answer = "   "
        for column in range(self.board.shape[1]):
            answer += " " + str(column + 1) + "  "
        answer += "\n"
        answer += self.separator()
        for row in range(self.board.shape[0]):
            answer += str(row + 1) + " |"
            for col in range(self.board.shape[1]):
                if self.board[row][col]:
                    answer += " o |"
                else:
                    answer += "   |"
            answer += "\n"
            answer += self.separator()
        return answer
    
# ---------------------------------------

    def separator(self):
        answer = "  +"
        for _ in range(self.board.shape[1]):
            answer += "---+"
        answer += "\n"
        return answer

# ---------------------------------------
# The four missing methods go here.  Do |
# not modify anything else.             |
# --------------------------------------|

    # Checks input values for a valid move
    def legal_move(self, row_start, col_start, row_end, col_end):
        if(self.board[row_start][col_start] == True) and (self.board[row_end][col_end] == False):
            # Checks Vertical Movement
            if(row_start == row_end):
                if(self.board[row_start][col_start-2] == self.board[row_end][col_end]) or (self.board[row_start][col_start+2] == self.board[row_end][col_end]):
                    if(self.board[row_start][col_start-1] == True) or (self.board[row_start][col_start+1] == True):
                        return True
            # Checks Horizontal Movement 
            elif(col_start == col_end):
                if(self.board[row_start-2][col_start] == self.board[row_end][col_end]) or (self.board[row_start+2][col_start] == self.board[row_end][col_end]):
                    if(self.board[row_start-1][col_start] == True) or (self.board[row_start+1][col_start] == True):
                        return True
            # Checks Down-Left Movement
            elif(row_start-2 == row_end) and (col_start-2 == col_end):
                if(self.board[row_start-1][col_start-1] == True):
                    return True
            # Checks Up-Right Movement
            elif(row_start+2 == row_end) and (col_start+2 == col_end):
                if(self.board[row_start+1][col_start+1] == True):
                    return True
            # Checks Up-Left Movement
            elif(row_start+2 == row_end) and (col_start-2 == col_end):
                if(self.board[row_start+1][col_start-1] == True):
                    return True
            # Checks Down-Right Movement
            elif(row_start-2 == row_end) and (col_start+2 == col_end):
                if(self.board[row_start-1][col_start+1] == True):
                    return True
            else:
                return False

    # Move the pegs if the move is legal
    def make_move(self, row_start, col_start, row_end, col_end):
        # Vertical Movement
        if(row_start == row_end):
            if(self.board[row_start][col_start-2] == self.board[row_end][col_end] and col_start > col_end):
                self.board[row_start][col_start-1] = False
            elif(self.board[row_start][col_start+2] == self.board[row_end][col_end] and col_start < col_end):
                self.board[row_start][col_start+1] = False
        # Lateral Movement
        elif(col_start == col_end):
            if(self.board[row_start-2][col_start] == self.board[row_end][col_end] and row_start > row_end):
                self.board[row_start-1][col_start] = False
            elif(self.board[row_start+2][col_start] == self.board[row_end][col_end] and row_start < row_end):
                self.board[row_start+1][col_start] = False
        # Down-Left Movement
        elif(row_start-2 == row_end and row_start > row_end) and (col_start-2 == col_end and col_start > col_end):
            self.board[row_start-1][col_start-1] = False
        # Up-Right Movement
        elif(row_start+2 == row_end and row_start < row_end) and (col_start+2 == col_end and col_start < col_end):
            self.board[row_start+1][col_start+1] = False
        # Up-Left Movement
        elif(row_start+2 == row_end and row_start < row_end) and (col_start-2 == col_end and col_start > col_end):
            self.board[row_start+1][col_start-1] = False
        # Down-Right Movement
        elif(row_start-2 == row_end and row_start > row_end) and (col_start+2 == col_end and col_start < col_end):
            self.board[row_start-1][col_start+1] = False        
        # Changes state of affected pegs
        self.board[row_start][col_start] = False
        self.board[row_end][col_end] = True
        

    def game_over(self):
        rows = self.rows
        columns = self.columns
##        no_moves = False
        for x in range(rows):
            for y in range(columns):
                if self.board[x][y] == True:
                    if(y+2 <= columns) and (x+2 <= rows):
                        if(self.board[x+1][y+1] == True) and (self.board[x+2][y+2] == False):
                            return False
##                            no_moves = False
                    elif(x+2 <= rows) and (y-2 >= 0):
                        if(self.board[x+1][y-1] == True) and (self.board[x+2][y-2] == False):
                            return False
##                            no_moves = False
                    elif(x-2 >= 0) and (y+2 <= columns):
                        if(self.board[x-1][y+1] == True) and (self.board[x-2][y+2] == False):
                            return False
##                            no_moves = False
                    elif(x-2 >= 0) and (y-2 >= 0):
                        if(self.board[x-1][y-1] == True) and (self.board[x-2][y-2] == False):
                            return False
##                            no_moves = False
                    elif(y+2 <=columns):
                        if(self.board[x][y+1] == True) and (self.board[x][y+2] == False):
                            return False
##                            no_moves = False
                    elif(y-2 >= 0):
                        if(self.board[x][y-1] == True) and (self.board[x][y-2] == False):
                            return False
##                            no_moves = False
                    elif(x+2 <= rows):
                        if(self.board[x+1][y] == True) and (self.board[x+2][y] == False):
                            return False
##                            no_moves = False
                    elif(x-2 >=0):
                        if(self.board[x-1][y] == True) and (self.board[x-2][y] == False):
                            return False
##                            no_moves = False
##
##                    try:
##                        if(self.board[x+1][y] == True) and (self.board[x+2][y] == False) and (x+1 < rows) and (x+2 <= rows):
##                            no_moves = False
##                        elif(self.board[x-1][y] == True) and (self.board[x-2][y] == False) and (x-1 > 0) and (x-2 >= 0):
##                            no_moves = False
##                        elif(self.board[x][y+1] == True) and (self.board[x][y+2] == False) and (y+1 < columns) and (y+2 <= columns):
##                            no_moves = False
##                        elif(self.board[x][y-1] == True) and (self.board[x][y-2] == False) and (y-1 > 0) and (y-2 >= 0):
##                            no_moves = False
##                        elif(self.board[x+1][y+1] == True) and (self.board[x+2][y+2] == False) and (x+1 < rows) and (x+2 <= rows) and (y+1 < columns) and (y+2 <= columns):
##                            no_moves = False
##                        elif(self.board[x+1][y-1] == True) and (self.board[x+2][y-2] == False) and (x+1 < rows) and (x+2 <= rows) and (y-1 > 0) and (y-2 >= 0):
##                            no_moves = False
##                        elif(self.board[x-1][y+1] == True) and (self.board[x-2][y+2] == False) and (x-1 > 0) and (x-2 >= 0) and (y+1 < columns) and (y+2 <= columns):
##                            no_moves = False
##                        elif(self.board[x-1][y-1] == True) and (self.board[x-2][y-2] == False) and (x-1 > 0) and (x-2 >= 0) and (y-1 > 0) and (y-2 >= 0):
##                            no_moves = False
##                    except:
##                        pass
##        if no_moves == False:
##            return False
##        else:
##            return True

    def final_message(self):
        f = 0
        # Counts the number of pegs on the board
        for x in range(self.rows):
            for y in range(self.columns):
                if self.board[x][y] == True:
                    f += 1
        if self.game_over() == True:
            print("Number of pegs left:", f)
            if f <= 2:
                print("You're a DigiPeg-enius!")
            elif 2 < f <= 4:
                print("I've worked with better. But not many.")
            elif 4 < f <=6:
                print(f, "left? Really? You're gonna have to do better than that.")
            else:
                print("DigiPeg-naramous! Rack'em up and redeem yourself.")


# ---------------------------------------
# End of DigiPeg Class                  |
# ---------------------------------------

def get_choice(low, high, message):
    message += " [" + str(low) + " - " + str(high) + "]: "
    legal_choice = False
    while not legal_choice:
        legal_choice = True
        answer = input(message)
        for character in answer:
            if character not in string.digits:
                legal_choice = False
                print("That is not a number, try again.")
                break 
        if legal_choice:
            answer = int(answer)
            if (answer < low) or (answer > high):
                legal_choice = False
                print("That is not a valid choice, try again.")
    return answer

# ---------------------------------------

def main():
    print("Welcome to DigiPeg Solitaire!")
    print("-----------------------------------\n")
    
    rows = get_choice(1, 9, "Enter the number of rows")
    columns = get_choice(1, 9, "Enter the number of columns")
    row = get_choice(1, rows, "Enter the empty space row") - 1
    column = get_choice(1, columns, "Enter empty space column") - 1   
    game = DigiPeg(rows, columns, row, column)
    print()

    print(game)
    while (not game.game_over()):
        row_start = get_choice(1, rows, "Enter the row of the peg to move") - 1
        col_start = get_choice(1, columns, "Enter the column of the peg to move") - 1
        row_end = get_choice(1, rows, "Enter the row where the peg lands") - 1
        col_end = get_choice(1, columns, "Enter the column where the peg lands") - 1
        if game.legal_move(row_start, col_start, row_end, col_end):
            game.make_move(row_start, col_start, row_end, col_end)
        else:
            print("Sorry.  That move is not allowed.")
        print()
        print(game)

    game.final_message()

# ---------------------------------------

main()
