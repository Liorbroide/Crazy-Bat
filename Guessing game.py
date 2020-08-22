import random

highest = 10
answer = random.randint(1, highest) #כלל האפשרויות שביניהן מתבצע הרנדומיזציה


print("You've got only three guesses. Please guess number between 1 and {}: ".format(highest))
guess = int(input())
guess_available = 0
guess_capacity = 3

if answer == guess:
    print("Well done! You got it first try!")

while answer != guess and guess_available != guess_capacity:
    if guess > answer:
        print("Please guess lower: ")
        guess = int(input())
        guess_available += 1
        if guess == answer:
            print("Well done!")
            break
    else:
        print("Please guess higher: ")
        guess = int(input())
        guess_available += 1
        if guess == answer:
            print("Well done!")
            break
if guess_capacity == guess_available:
    print("You ran out of guesses!")
