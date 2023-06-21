import random

def number_game():
    number = random.randint(1,100)
    attempts = 0
    max_attempts = 10

    print("Welcome to Guess the Number!")
    print("I am thinking of a number between 1 and 100")

    while attempts < max_attempts:
        attempts += 1
        guess = int(input("Take a guess: "))
        
        if guess < number:
            print("Too low!")

        elif guess > number:
            print("Too high!")

        else:
            print(f"Congratulations! You got it right in {attempts} tries!")
    
    return

    print(f"Game over, the answer was {number}.")

number_game()


