import random

# It's time to actually make a simple command line game so put together everything
# you've learned so far about Python. The game goes like this:

# 1. The computer will think of 3 digit number that has no repeating digits.
# 2. You will then guess a 3 digit number
# 3. The computer will then give back clues, the possible clues are:
#
#     Close: You've guessed a correct number but in the wrong position
#     Match: You've guessed a correct number in the correct position
#     Nope: You haven't guess any of the numbers correctly
#
# 4. Based on these clues you will guess again until you break the code with a
#    perfect match!

# There are a few things you will have to discover for yourself for this game!
# Here are some useful hints:


def check_guess_against_secret(guess, target):
    if guess == target:
        return "Code Cracked!"
    clues = []
    for i in range(len(guess)):
        if guess[i] == target[i]:
            clues.append("Match")
        elif guess[i] in target:
            clues.append("Close")
    if not clues:
        return ["Nope"]
    else:
        return clues


def get_guess():
    return input("What is your guess? ")


def generate_code():
    digits = [str(num) for num in range(10)]
    random.shuffle(digits)
    return digits[0] + digits[1] + digits[2]


print("Welcome to Code Cracker game!")
secret_code = generate_code()
ans = ""
while ans != 'Code Cracked!':
    user_guess = get_guess()
    ans = check_guess_against_secret(user_guess, target=secret_code)
    for a in ans:
        print(a)

