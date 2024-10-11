import random
choices = ["rock", "paper", "scissors"]
def get_computer_choice():
    return random.choice(choices)
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "user"
    else:
        return "computer"
def display_result(user_choice, computer_choice, winner):
    print(f"\nYou chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")
    if winner == "tie":
        print("It's a tie!")
    elif winner == "user":
        print("You win!")
    else:
        print("Computer wins!")
def play_round():
    user_choice = input("Choose rock, paper, or scissors: ").lower()
    if user_choice not in choices:
        print("Invalid choice, try again.")
        return None, None
    computer_choice = get_computer_choice()
    winner = determine_winner(user_choice, computer_choice)
    display_result(user_choice, computer_choice, winner)
    return winner
def play_game():
    user_score = 0
    computer_score = 0
    while True:
        winner = None
        winner = play_round()        
        if winner == "user":
            user_score += 1
        elif winner == "computer":
            computer_score += 1
        print(f"\nCurrent Score: You {user_score} - {computer_score} Computer")
        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            break
    print(f"\nFinal Score: You {user_score} - {computer_score} Computer")
    print("Thanks for playing!")
if __name__ == "__main__":
    print("Welcome to Rock-Paper-Scissors!")
    play_game()