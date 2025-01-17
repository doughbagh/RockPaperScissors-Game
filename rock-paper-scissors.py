import random

# Function to determine the outcome of the game
def game(user_action, computer_action):
    if user_action == computer_action:
        print(f"Both players selected {user_action}. It's a tie!")
    elif computer_action == 'rock':
        if user_action == 'scissors':
            print("Rock smashes scissors! You lose.")
        elif user_action == 'paper':
            print("Paper covers rock! You win.")
    elif computer_action == 'paper':
        if user_action == 'rock':
            print("Paper covers rock! You lose.")
        elif user_action == 'scissors':
            print("Scissors cuts paper! You win.")
    elif computer_action == 'scissors':
        if user_action == 'paper':
            print("Scissors cuts paper! You lose.")
        elif user_action == 'rock':
            print("Rock smashes scissors! You win.")

# Main game loop
while True:
    # Get user input
    user_action = input("Enter a choice (rock, paper, scissors): ").lower()
    possible_actions = ["rock", "paper", "scissors"]
    
    # Randomly select an action for the computer
    computer_action = random.choice(possible_actions)
    print(f"\nYou chose {user_action}, computer chose {computer_action}.\n")
    
    # Determine the outcome of the game
    game(user_action, computer_action)
    
    # Ask the user if they want to play again
    play_again = input("Play again? (yes/no): ").lower()
    if play_again != "yes":
        break