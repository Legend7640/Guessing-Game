import random
n = random.randint(1, 100)
guess = int(input("Guess from 1 to 100: "))
while n != "guess":
    print
    if guess < n:
        print ("Too Low!")
        guess = int(input("Try Again: "))
    elif guess > n:
        print ("Too High!")
        guess = int(input("Try Again: "))
    else:
        print ("Correct!")
        break
    print