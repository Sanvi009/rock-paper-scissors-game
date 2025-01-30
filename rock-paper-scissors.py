import random
from colorama import Fore, Back, Style

computer = 0
user = 0

data = ("🪨", "✂️", "📄")
print("WELCOME TO ROCK PAPER SCISSORS GAME\n")

while True:
    computer_choice = random.choice(data)
    ask_user = input("\nEnter your choice (rock, paper, scissors, quit): ").lower()

    # Converting user input to emoji
    user_choice_emoji = ""
    if ask_user == "rock":
        user_choice_emoji = "🪨"
    elif ask_user == "paper":
        user_choice_emoji = "📄"
    elif ask_user == "scissors":
        user_choice_emoji = "✂️"

    # Match Draw Cases
    if user_choice_emoji == computer_choice:
        print(Fore.BLUE + f"{user_choice_emoji} vs {computer_choice} - Match Draw!" + Fore.RESET)

    # Winning Conditions
    elif (user_choice_emoji == "🪨" and computer_choice == "✂️") or \
         (user_choice_emoji == "📄" and computer_choice == "🪨") or \
         (user_choice_emoji == "✂️" and computer_choice == "📄"):
        print(Fore.GREEN + f"{user_choice_emoji} vs {computer_choice} - You Win!" + Fore.RESET)
        user += 1
        print(f"Your Score: {user} | Computer Score: {computer}")

    # Losing Conditions
    elif (user_choice_emoji == "🪨" and computer_choice == "📄") or \
         (user_choice_emoji == "📄" and computer_choice == "✂️") or \
         (user_choice_emoji == "✂️" and computer_choice == "🪨"):
        print(Fore.RED + f"{user_choice_emoji} vs {computer_choice} - You Lose!" + Fore.RESET)
        computer += 1
        print(f"Your Score: {user} | Computer Score: {computer}")

    # Quit Condition
    elif ask_user == "quit":
        print("Thanks for playing!")
        print(f"Your score: {user} | Computer's score: {computer}")
        break

    # Invalid Input
    else:
        print(Fore.RED + "Invalid input! Please enter rock, paper, scissors, or quit." + Fore.RESET)
