import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        if guess < random_number:
            print("Sorry, guess again. Too low.")
        elif guess > random_number:
            print("Sory, guess again. Too high")
    print(f"yay, congrats. You have guessed the number {random_number}")

def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        guess = random.randint(low, high)
        feedback = input(f"Is {guess} too high (H), too low (L), or correct (C)??").lower()
        if feedback == "h":
            high = guess - 1
        elif feedback == "l":
            low = guess + 1

    print("Yay! The computer guessed you number, {guess}, correctly!")

computer_guess(10)
