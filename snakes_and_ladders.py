import random
import time

# Constants
BOARD_SIZE = 100
WINNING_POSITION = 100

# Game setup
def setup_game():
    """Sets up the game by getting player names and initializing their positions."""
    print("--- Welcome to Snakes and Ladders! ---")
    
    # Define snakes and ladders using dictionaries {start_position: end_position}
    snakes = {
        99: 41, 95: 75, 88: 24, 62: 19, 48: 26, 36: 6, 32: 10
    }
    ladders = {
        1: 38, 4: 14, 9: 31, 21: 42, 28: 84, 51: 67, 72: 91, 80: 98
    }

    while True:
        try:
            num_players = int(input("Enter the number of players (2-4): "))
            if 2 <= num_players <= 4:
                break
            else:
                print("Please enter a number between 2 and 4.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    player_names = [input(f"Enter name for Player {i+1}: ") for i in range(num_players)]
    player_positions = {name: 0 for name in player_names}
    
    return player_names, player_positions, snakes, ladders

def roll_dice():
    """Simulates rolling a six-sided die."""
    print("    Rolling the dice...")
    time.sleep(1) # Add a small delay for suspense
    roll = random.randint(1, 6)
    print(f"    🎲 You rolled a {roll}!")
    return roll

def move_player(player, current_position, roll):
    """Calculates the new position of the player after a roll."""
    new_position = current_position + roll
    
    if new_position > WINNING_POSITION:
        print(f"    Oops! Your roll of {roll} is too high. You need exactly {WINNING_POSITION - current_position} to win.")
        return current_position # Player doesn't move if roll is too high
    
    print(f"    {player} moves from {current_position} to {new_position}.")
    return new_position

def check_snakes_and_ladders(player, position, snakes, ladders):
    """Checks if a player landed on a snake or a ladder and updates position."""
    if position in snakes:
        final_position = snakes[position]
        print(f"    Oh no! 🐍 {player} landed on a snake at {position} and slid down to {final_position}.")
        return final_position
    elif position in ladders:
        final_position = ladders[position]
        print(f"    Wow! 🪜 {player} found a ladder at {position} and climbed up to {final_position}!")
        return final_position
    return position

def main():
    """The main game loop."""
    player_names, player_positions, snakes, ladders = setup_game()
    current_player_index = 0
    winner = None

    while not winner:
        # Get the current player
        current_player_name = player_names[current_player_index]
        current_player_position = player_positions[current_player_name]

        print("\n" + "="*30)
        print(f"It's {current_player_name}'s turn. Current position: {current_player_position}")
        input("Press Enter to roll the dice...")

        # Core turn logic
        dice_roll = roll_dice()
        new_position = move_player(current_player_name, current_player_position, dice_roll)
        final_position = check_snakes_and_ladders(current_player_name, new_position, snakes, ladders)
        
        player_positions[current_player_name] = final_position
        print(f"    {current_player_name}'s final position is {final_position}.")

        # Check for a winner
        if final_position == WINNING_POSITION:
            winner = current_player_name
            print("\n" + "*"*30)
            print(f"🎉 Congratulations, {winner}! You have won the game! 🎉")
            print("*"*30)
            break
        
        # Move to the next player
        current_player_index = (current_player_index + 1) % len(player_names)

if __name__ == "__main__":
    main()