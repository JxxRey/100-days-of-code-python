import random

print("Welcome to the number guessing game!")
print("I'm thinking of a number between 1 and 100.")
difficulty = input("Choose 'easy' or 'hard': ")

def easy_difficulty():
    attempts = 10
    answer = random.choice(range(100))
    while attempts > 0:
        guess = int(input("Make a guess: "))
        attempts -= 1
        if guess > answer:
            print("Too high")
            print("Guess again")

        elif guess < answer:
            print("Too low")
            print("Guess again")
        elif guess == answer:
            print("Correct you win")
            exit()
        else:
            print("Wrong input try again")
        print(f"{attempts} Attempts remaining")



def hard_difficulty():
    attempts = 5
    answer = random.choice(range(100))
    while attempts > 0:
        guess = int(input("Make a guess: "))
        attempts -= 1
        if guess > answer:
            print("Too high")
            print("Guess again")

        elif guess < answer:
            print("Too low")
            print("Guess again")
        elif guess == answer:
            print("Correct you win")
            exit()
        else:
            print("Wrong input try again")
        print(f"{attempts} Attempts remaining")

if difficulty == "easy":
    easy_difficulty()

elif difficulty == "hard":
    hard_difficulty()
else:
    print("Wrong input fool")
    exit()