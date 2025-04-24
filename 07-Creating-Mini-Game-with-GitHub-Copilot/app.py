import random

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(player, computer):
    if player == computer:
        return "tie"
    elif (player == "rock" and computer == "scissors") or \
         (player == "scissors" and computer == "paper") or \
         (player == "paper" and computer == "rock"):
        return "win"
    else:
        return "lose"

def main():
    print("Welcome to Rock, Paper, Scissors!")
    player_score = 0
    rounds = 0

    while True:
        player_choice = input("Enter your choice (rock, paper, scissors): ").strip().lower()
        if player_choice not in ["rock", "paper", "scissors"]:
            print("Invalid choice. Please choose rock, paper, or scissors.")
            continue

        computer_choice = get_computer_choice()
        print(f"Computer chose: {computer_choice}")

        result = determine_winner(player_choice, computer_choice)
        if result == "win":
            print("You win this round!")
            player_score += 1
        elif result == "lose":
            print("You lose this round!")
        else:
            print("It's a tie!")

        rounds += 1
        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        if play_again != "yes":
            break

    print(f"Game over! You won {player_score} out of {rounds} rounds.")
    print("Thanks for playing!")

if __name__ == "__main__":
    main()