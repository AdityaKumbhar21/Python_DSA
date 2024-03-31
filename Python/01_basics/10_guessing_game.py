
import random
guess_number = random.randint(1,10)

print('''
     Welcome to guessing game
''')

num_of_guess = 4

while(num_of_guess != 0):
  if(num_of_guess != 0):
        user_guess = int(input("Guess the number: "))
        if(user_guess == guess_number):
            print("You guessed it right")
            print('''
                 !!!!! You won the game  !!!!!
            ''')
            exit()
        elif(user_guess > guess_number):
            print("The number is more smaller.")
            num_of_guess -=1
            print("Number of guess left: ",num_of_guess)
        else:
            print("The number is bigger.")
            num_of_guess -= 1
            print("Number of guess left: ",num_of_guess)

print()
print('''
    Game Ended!!
''')
    
    
