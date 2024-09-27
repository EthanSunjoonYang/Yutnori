import random
import time

# Lets simplify a Yutnori board into 20 spaces
BOARD_SIZE = 20

# Roll: Returns the number of moves and whether the player gets an extra turn.
def roll_yut():
    sticks = [random.choice([0, 1]) for _ in range(4)]
    total_up = sum(sticks)


    if total_up == 1:
        return 1, False  # Do (one space)
    elif total_up == 2:
        return 2, False  # Gae (two spaces)
    elif total_up == 3:
        return 3, False  # Geol (three spaces)
    elif total_up == 4:
        return 4, True   # Yut (four spaces & extra turn)
    else:
        return 5, True   # Mo (five spaces & extra turn)

# Display the player positions
def display_status(player1_name, player1_pos, player2_name, player2_pos):
    print(f"\n{player1_name}'s position: {player1_pos}")
    time.sleep(0.5)
    print(f"{player2_name}'s position: {player2_pos}")
    time.sleep(0.5)

# Move the players
def move_position(current_pos, moves):
    new_pos = current_pos + moves
    if new_pos >= BOARD_SIZE:
        new_pos = BOARD_SIZE 
    return new_pos

# Play Yutnori
def play_yutnori():

    player1_name = input("Enter the name of Player 1: ")
    player2_name = input("Enter the name of Player 2: ")

    player1_pos = 0
    player2_pos = 0
    
    print("\nWelcome to Yutnori!")
    time.sleep(0.5)
    print(f"Race to complete one lap around the board (20 spaces), {player1_name} and {player2_name}!")
    time.sleep(0.5)
    
    while True:
        # Player 1's turn
        print() 
        input(f"\n{player1_name}'s turn! Press Enter to throw the Yut sticks...")
        player1_moves, player1_extra_turn = roll_yut()
        print(f"{player1_name} rolled a move of {player1_moves} {'and earned an extra turn!' if player1_extra_turn else ''}")
        time.sleep(0.5)
        player1_pos = move_position(player1_pos, player1_moves)
        
        # Check if Player 1 lands on Player 2's position
        if player1_pos == player2_pos:
            print(f"{player1_name} landed on {player2_name}'s position! {player2_name} goes back to the start!")
            time.sleep(0.5)
            player2_pos = 0
            player1_extra_turn = True  # Player 1 earns an extra turn for landing on player 2
        
        display_status(player1_name, player1_pos, player2_name, player2_pos)
        
        # Check if player 1 won
        if player1_pos == BOARD_SIZE:
            print(f"\n{player1_name} wins! Congratulations!")
            time.sleep(0.5)
            break
        
        while player1_extra_turn:
            print() 
            input(f"{player1_name} earned an extra turn! Press Enter to roll again...")
            player1_moves, player1_extra_turn = roll_yut()
            print(f"{player1_name} rolled a move of {player1_moves} {'and earned an extra turn!' if player1_extra_turn else ''}")
            time.sleep(0.5)
            player1_pos = move_position(player1_pos, player1_moves)
            
            # Check again if Player 1 lands on Player 2's position
            if player1_pos == player2_pos:
                print(f"{player1_name} landed on {player2_name}'s position! {player2_name} goes back to the start!")
                time.sleep(0.5)
                player2_pos = 0
                player1_extra_turn = True  # Player 1 earns an extra turn for landing on player 2
            
            display_status(player1_name, player1_pos, player2_name, player2_pos)
            
            # Check again if player 1 won
            if player1_pos == BOARD_SIZE:
                print(f"\n{player1_name} wins! Congratulations!")
                time.sleep(0.5)
                return

        # Pause between Player 1's turn and Player 2's turn
        print() 
        print(f"\nNow, it's {player2_name}'s turn...")
        time.sleep(0.5)

        # Player 2's turn
        print()  
        input(f"\n{player2_name}'s turn! Press Enter to throw the Yut sticks...")
        player2_moves, player2_extra_turn = roll_yut()
        print(f"{player2_name} rolled a move of {player2_moves} {'and earned an extra turn!' if player2_extra_turn else ''}")
        time.sleep(0.5)
        player2_pos = move_position(player2_pos, player2_moves)
        
        # Check if Player 2 lands on Player 1's position
        if player2_pos == player1_pos:
            print(f"{player2_name} landed on {player1_name}'s position! {player1_name} goes back to the start!")
            time.sleep(0.5)
            player1_pos = 0
            player2_extra_turn = True  # Player 2 earns an extra turn for landing on player 1
        
        display_status(player1_name, player1_pos, player2_name, player2_pos)
        
        # Check if player 2 won
        if player2_pos == BOARD_SIZE:
            print(f"\n{player2_name} wins! Congratulations!")
            time.sleep(0.5)
            break
        
        while player2_extra_turn:
            print() 
            input(f"{player2_name} earned an extra turn! Press Enter to roll again...")
            player2_moves, player2_extra_turn = roll_yut()
            print(f"{player2_name} rolled a move of {player2_moves} {'and earned an extra turn!' if player2_extra_turn else ''}")
            time.sleep(0.5)
            player2_pos = move_position(player2_pos, player2_moves)
            
            # Check if Player 2 lands on Player 1's position
            if player2_pos == player1_pos:
                print(f"{player2_name} landed on {player1_name}'s position! {player1_name} goes back to the start!")
                time.sleep(0.5)
                player1_pos = 0
                player2_extra_turn = True  # Player 2 earns an extra turn for landing on player 1
            
            display_status(player1_name, player1_pos, player2_name, player2_pos)
            
            # Check again if player 2 won
            if player2_pos == BOARD_SIZE:
                print(f"\n{player2_name} wins! Congratulations!")
                time.sleep(0.5)
                return

# Start the game
if __name__ == "__main__":
    play_yutnori()