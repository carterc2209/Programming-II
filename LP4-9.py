import random

playernum = int(input("Enter a number between 1 and 20:"))
randomnum = random.randint(1, 20)
print("Players Number: ", playernum)
print("Computers Number: ", randomnum)
if playernum == randomnum:
    print("You guessed correctly.")
else:
    print("You guessed wrong.")