from random import randint

num = randint(1, 10)
guess = eval(input("Enter you guess: "))
if guess  == num:
    print("you got it")
else:
    print("sorry. the number is ", num)    