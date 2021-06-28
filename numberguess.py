import random
import math

lower = int(input("Enter Lower bound:- "))

upper = int(input("Enter Upper bound:- "))


x = random.randint(lower, upper)

print("\nYou've only 5 chances to guess the correct number")


count = 0


while count < 5:
	count += 1

	
	guess = int(input("Guess a number:- "))

	
	if x == guess:
		print("Congratulations you did it in ",
			count, " try")
		break
	elif x > guess:
		print("You guessed too small!")
	elif x < guess:
		print("You Guessed too high!")


if count >= 5:
	print("\nThe number is %d" % x)
	print("\tBetter Luck Next time!")


