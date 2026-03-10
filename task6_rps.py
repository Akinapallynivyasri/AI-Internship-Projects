import random

choices = ["rock", "paper", "scissors"]

user_score = 0
computer_score = 0

print("Rock Paper Scissors Game")
print("Type 'quit' to exit\n")

while True:
    user = input("Enter rock, paper, or scissors: ").lower()

    if user == "quit":
        print("\nFinal Score:")
        print("You:", user_score)
        print("Computer:", computer_score)
        print("Thanks for playing!")
        break

    if user not in choices:
        print("Invalid choice! Try again.\n")
        continue

    computer = random.choice(choices)

    print("Computer chose:", computer)

    if user == computer:
        print("It's a Draw!\n")

    elif (user == "rock" and computer == "scissors") or \
         (user == "paper" and computer == "rock") or \
         (user == "scissors" and computer == "paper"):

        print("You Win!\n")
        user_score += 1

    else:
        print("Computer Wins!\n")
        computer_score += 1