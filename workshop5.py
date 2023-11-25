import random

def guess_random_number(tries, start, stop):
    num = random.randint(start, stop)
    while tries != 0:
        print("Number of tries left:", tries)
        guess = input("Guess a number between 0 and 10: ")
        ans = int(guess)
        while ans < start or ans > stop:
            guess = input("Number outside of guessing range. Please guess a number between 0 and 10: ")
            ans = int(guess)
        if ans == num:
            print("You guessed the correct number!")
            return
        elif ans < num:
            print("Guess higher!")
        elif ans > num:
            print("Guess lower!")
        tries -= 1
    # if tries == 0:
    print("You have failed to guess the number:", num)

def guess_random_num_linear(tries, start, stop):
    num = random.randint(start, stop)
    print("The number for the program to guess is:", num)
    for i in range(start, stop + 1):
        print("Number of tries left:", tries)
        print("The program is guessing...", i)
        if i == num:
            print("The program has guessed the correct number!")
            return
        tries -= 1
        if tries == 0:
            print("The program has failed to guess the correct number.")
            return
        
def guess_random_num_binary(tries, start, stop):
    num = random.randint(start, stop)
    print("Random number to find:", num)
    highNum = stop
    lowNum = start
    while tries != 0:
        pivot = (highNum + lowNum) // 2
        # print("The program is guessing...", pivot)
        if pivot == num:
            print("The program has guessed the correct number!")
            return
        elif pivot > num:
            print("Guessing lower!")
            highNum = pivot - 1
        elif pivot < num:
            print("Guessing higher!")
            lowNum = pivot + 1
        tries -= 1
    print("Your program failed to find the number.")

# guess_random_num_binary(5, 0, 100)
# guess_random_number(5, 0, 10)
# guess_random_num_linear(5, 0, 10)
