import random

def main():
    print("Welcome to the Rock, Paper, Scissors Game!")
    print("\nRules of the game:")
    print("1. You will choose one of 'rock', 'paper', or 'scissors'.")
    print("2. The computer will also make a choice.")
    print("3. Both choices will be revealed, and the winner is determined based on:")
    print("   - Rock beats Scissors (by crushing them)")
    print("   - Scissors beats Paper (by cutting it)")
    print("   - Paper beats Rock (by covering it)")
    print("4. If both choices are the same, it’s a tie.\n")

    # Game loop
    while True:
        player_choice = input("Choose rock, paper, or scissors (or type 'quit' to end): ").lower()
        
        if player_choice == 'quit':
            print("Thanks for playing!")
            break

        if player_choice not in ['rock', 'paper', 'scissors']:
            print("Invalid choice, please try again.")
            continue

        # Generate computer choice
        computer_choice = random.choice(['rock', 'paper', 'scissors'])
        print(f"Computer chose: {computer_choice}")

        # Determine the winner
        if player_choice == computer_choice:
            print("It's a tie!")
        elif (player_choice == 'rock' and computer_choice == 'scissors') or \
             (player_choice == 'scissors' and computer_choice == 'paper') or \
             (player_choice == 'paper' and computer_choice == 'rock'):
            print("You win this round!")
        else:
            print("Computer wins this round!")

if _name_ == "_main_":
    main()