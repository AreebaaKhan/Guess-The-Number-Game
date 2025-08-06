import random
target = random.randint(1, 100)
while True:
    user_choice = input("Guess a number between 1 and 100 or type 'Q' to quit: ")
    if (user_choice == "Q"):
        break
                
    user_choice = int(user_choice)
    if user_choice == target:
        print( "Success: Congratulations! You guessed the number correctly.")
                
    elif user_choice > target:
        print("Fail: Your choice is big, guess a smaller number.")
                    
    else:  
        print("Fail: Your choice is small, guess a bigger number.")
 
print("-----GAME OVER-----")
