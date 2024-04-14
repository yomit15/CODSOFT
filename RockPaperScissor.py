import random

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return "You win!"
    else:
        return "You lose!"

def play_game():
    print("Welcome to Rock, Paper, Scissors!")
    print("Choose one: rock, paper, or scissors")

    user_choice = input("Your choice: ").lower()
    if user_choice not in ['rock', 'paper', 'scissors']:
        print("Invalid choice! Please choose rock, paper, or scissors.")
        return

    computer_choice = random.choice(['rock', 'paper', 'scissors'])

    print("You chose:", user_choice)
    print("Computer chose:", computer_choice)

    result = determine_winner(user_choice, computer_choice)
    print(result)

def main():
    play_game()
    while input("Do you want to play again? (yes/no): ").lower() == 'yes':
        play_game()

if __name__ == "__main__":
    main()
