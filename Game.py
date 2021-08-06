import random
num = random.randint(1,20)
# print(num)             # user cannot able to see the number
print(" one random number is generated from 1 to 20, now its your time to guess it:--")

userguess = None
guesses = 0
while userguess != num:
    userguess = int(input("Guess a number: "))
    guesses += 1

    if userguess == num:
       print("Congratulations! You guess the number right.")

    elif userguess > num:
         print("Your guess is wrong! Enter a smaller number.")
    else:
         print("You guess is wrong! Enter a larger number.")

print(f"You guess the correct number in {guesses} guesses")
