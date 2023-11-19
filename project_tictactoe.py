# Player setup
player1 = input("Ready, player One? What's your name?\n")
player2 = input("Ready, player Two? What's your name?\n")
print("Welcome to 1D-tic-tac-toe Winter Edition, " + player1 +" and " + player2 + "!")

# Assign signs to players
player1_sign = '\N{BLACK STAR}'
player2_sign = '\N{SNOWMAN}'
print(player1 + ", you are going to move the " + player1_sign + ".")
print(player2 + ", you are going to move the " + player2_sign + ".")

# Explain the rules
print("Here are the rules:\nThe first one placing the assigned sign three times next to each other in a 20 space line wins. But first we let the coin decide who starts.")

# Coinflip
from random import randrange
coin = randrange(2)

if coin == 0:
    beginner = player1
    print(beginner, "starts.")
else:
    beginner = player2
    print(beginner, "starts.")

# Evaluate Function
def evaluate(board):
    # Win:
    for sign in [player1_sign, player2_sign]:
        if sign * 3 in board:
            return sign
    # Draw:
    if "-" not in board:
        return "!"
    # Game ongoing:
    return "-"

# Move Function
def move(board, sign, position):
    if 0 <= position < 20: # Position between 0 und 20(19).
        if board[position] == "-":  # Position empty?
            # Create a new board with the sign placed.
            new_board = ""
            for i in range(len(board)):
                if i == position:
                    new_board += sign
                else:
                    new_board += board[i]
            return new_board
        
        return board  # Back if position taken is not valid.

# Player1 move function
def player1_move(board, sign):
    while True:
        try:# I wanted to catch if the input is valid, I had a smilar question in a previous homework and got the hint that I could look up for try function, I hope it's ok I used this even if we havent learned it sofar
            position = int(input(player1 + ", where do you want to place your " + player1_sign + ". Choos e a number between 0-19: "))
            if 0 <= position < 20 and board[position] == "-":
                return move(board, sign, position)
            else:
                print("Nope, not here.")
        except ValueError:
            print("I said between 0 and 19.") # why doesn't it work with input numbers 20+? this only comes when the input of the position is gibberish like "dafjso", but with 99 it says "Nope, not here?"

# After I finished I realized you wanted a game against a computer, I hope it's ok I made a 2-Player Game, I somehow forgot it while working on the game -.-
def player2_move(board, sign):
    while True:
        try:
            position = int(input(player2 + ", where do you want to place your " + player2_sign + ". Choose a number between 0-19: "))
            if 0 <= position < 20 and board[position] == "-":
                return move(board, sign, position)
            else:
                print("Nope, not here.")
        except ValueError:
            print("I said between 0 and 19.") # why doesn't it work with input numbers 20+? this only comes when the input of the position is gibberish like "dafjso", but with 99 it says "Nope, not here?"

# ttt-function:
def tictactoe():
    # Setup:
    board = "-" * 20
    current_player = beginner  #coinflip-winner
    current_sign = player1_sign if current_player == player1 else player2_sign

    while True:
        # Showing the starting board
        print('Board: ' + board)

        # Beginner makes a move
        if current_player == player1:
            board = player1_move(board, current_sign)
        else:
            board = player2_move(board, current_sign)

        # Check the game:
        state = evaluate(board)
        if state != "-":
            print("Board:", board)  # Show final board
            if state == player1_sign:
                print(f"Ho, Ho, Ho! Awesome {player1} wins!")
            elif state == player2_sign:
                print(f"Ho, Ho, Ho! Awesome {player2} wins!")
            else:
                print("Well, I think you have to play again. It's a draw!")
            break  # End the game loop

        # Switching players
        current_player = player1 if current_player == player2 else player2
        current_sign = player1_sign if current_player == player1 else player2_sign

# Start the game
tictactoe()