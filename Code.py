import random
Computer_guess = (random.randint(0, 10))
print(Computer_guess) # We can remove this to hide the number from user

for i in range(4): 
     user_input = int(input("Enter a number: "))
     if user_input>Computer_guess:
       print("High Guess!!!")
     elif user_input<Computer_guess:
        print("Too Low!!!") 
     elif user_input==Computer_guess:
        print("You Won!!!")   
     else :
       print("Try Again:/")
print("Game Over! Good luck next time:)")       