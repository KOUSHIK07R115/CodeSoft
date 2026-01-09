import random

def get_computer_choice():
    """Generates a random choice for the computer."""
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user, computer):
    """
    Determines the winner based on game logic:
    Rock beats Scissors, Scissors beat Paper, Paper beats Rock.
    """
    if user == computer:
        return "tie"
    
    # Define winning conditions: key beats value
    win_conditions = {
        'rock': 'scissors',
        'scissors': 'paper',
        'paper': 'rock'
    }
    
    if win_conditions[user] == computer:
        return "user"
    else:
        return "computer"

def play_game():
    user_score = 0
    computer_score = 0
    
    print("--- Rock, Paper, Scissors ---")
    print("Rules: Rock beats Scissors | Scissors beat Paper | Paper beats Rock")

    while True:
        print(f"\nScore: You {user_score} - {computer_score} Computer")
        user_choice = input("Enter choice (rock/paper/scissors) or 'q' to quit: ").lower()

        if user_choice == 'q':
            break
        
        if user_choice not in ['rock', 'paper', 'scissors']:
            print("Invalid choice! Please type 'rock', 'paper', or 'scissors'.")
            continue

        computer_choice = get_computer_choice()
        print(f"Computer chose: {computer_choice}")

        result = determine_winner(user_choice, computer_choice)

        if result == "tie":
            print(f"Both chose {user_choice}. It's a tie!")
        elif result == "user":
            print(f"You win! {user_choice.capitalize()} beats {computer_choice}.")
            user_score += 1
        else:
            print(f"You lose! {computer_choice.capitalize()} beats {user_choice}.")
            computer_score += 1

        # Play Again logic
        play_again = input("\nPlay another round? (y/n): ").lower()
        if play_again != 'y':
            break

    print("\n--- Final Results ---")
    print(f"Final Score: You {user_score} | Computer {computer_score}")
    print("Thanks for playing!")

if __name__ == "__main__":
    play_game()
