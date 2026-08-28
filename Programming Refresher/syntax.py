import random

def guessNumber(player_guess, range_begin, range_end):
    secrete_number = random.randint(range_begin, range_end)
    # print(f"Guess a number between {range_begin} and {range_end}")

    while player_guess != secrete_number:
        if player_guess > secrete_number:
            print("That's too high!")
        elif player_guess < secrete_number:
            print("That's too low!")
        else:
            print("You must input a valid number.")
        player_guess = int(input(f"Guess a number between {range_begin} and {range_end}: "))

    print(f"You guessed it. The secret number is {secrete_number}")

def main():
    range_begin = 1
    range_end = 24
    player_guess = int(input(f"Guess a number between {range_begin} and {range_end}: "))
    guessNumber(player_guess, range_begin, range_end)

main()