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

def collatzSeq(number):
    if number % 2 == 0:
        result = number // 2
        print(result)

    else:
        result = 3 * number + 1
        print(result)

    return result

def myFriends():
    friends = []
    name = input("Enter your friend's name: ")
    while True:
        print('Enter the name of friend' + str(len(friends) + 1) + '(or nothing to stop.): ')
        name = input()
        if name == '':
            break
        friends = friends + [name]

    print("My friends' names are: ")
    for n in friends:
        print(' '+ n)

def putCamma(things):
    listItems = ''
    for item in things:
        if things[len(things)-1] == item:
            listItems += 'and '+item
        else:
            listItems += item+', '

    return listItems

def main():
    range_begin = 1
    range_end = 24
    # player_guess = int(input(f"Guess a number between {range_begin} and {range_end}: "))
    # guessNumber(player_guess, range_begin, range_end)

    # in_number = int(input("Enter a number: "))
    # collatz_result = collatzSeq(in_number)
    # while collatz_result != 1:
    #     collatz_result = collatzSeq(collatz_result)
    # print(collatz_result)
    things = ['apples', 'bananas', 'tofu', 'cats']
    print(putCamma(things))

    # myFriends()

main()