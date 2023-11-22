# Player setup
player1 = input("Ready, player One? What's your name?\n")
player2 = "Computer-Player"
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
    for sign in [player1_sign, player2_sign]: # Checking if either sign1 or sign2 is placed 3 times next to each other
        if sign * 3 in board:
            return sign
    # Draw:
    if "-" not in board: # If the first "if" isnt true, it checks every field in the board is filled (no "-" inside), so it's draw
        return "!"
    # Game ongoing:
    return "-" # If neither of the first two if's are true, its going to the next round

# Move Function
def move(board, sign, position):
    if 0 <= position < 20: # Position between 0 und 20(19).
        if board[position] == "-":  # Position empty?
            # Create a new board with the sign placed.
            new_board = ""
            for i in range(len(board)): # Now checking every character in the board
                if i == position: # As soon at it hits the "position" it fills the sign
                    new_board += sign
                else: # Every other character (not position), gets filled up again with the original board signs
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
                print("Nope, not here. A non taken place between 0 and 19.")
        except ValueError:
            print("Must be a number.") # I misunderstood the try/except function, but I think now I get it, its about the validation of the kind of input (str, int)

# Pc move function
def pc_move(board, sign):
    while True:
        position = randrange(20)
        print(f"{player2} choose position {position}")
        if 0 <= position < 20 and board[position] == "-":
            return move(board, sign, position)
        else:
            print("Nope, not here. A non taken place between 0 and 19.")


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
            board = pc_move(board, current_sign)

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
