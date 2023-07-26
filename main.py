import random

def main():
    """Core functionality of the game."""
    try:
        choice = int(input("Hello, welcome to Rock Paper Scissors, please, select from [0]Rock, [1]Paper, [2]Scissors to begin playing: \n"))
    except ValueError:
        choice = int(input("Invalid choice, please, select from [0]Rock, [1]Paper, [2]Scissors to begin playing: \n"))
    ai_choice = random.randint(0,2)
    match ai_choice:
        case 0:
            print("The AI chose: Rock")
            match choice:
                case 1:
                    print("You win!")
                case 2:
                    print("You lose.")
        case 1:
            print("The AI chose: Paper")
            match choice:
                case 0:
                    print("You lose.")
                case 2:
                    print("You win!")
        case 2:
            print("The AI chose: Scissors")
            match choice:
                case 0:
                    print("You win!")
                case 1:
                    print("You lose.")
    if ai_choice == choice:
        print("It's a draw!")
    restart = input("Do you want to play again? Y/N:  ").lower()
    if restart == "y":
        main()


if __name__ == "__main__":
    main()