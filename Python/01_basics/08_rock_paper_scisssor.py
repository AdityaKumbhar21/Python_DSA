import random

print("Welcome to the Rock,Paper and Scissor game")
print("The rules:")
print("1. Rock \n2.Scissors\n3.Paper")

start_game = int(input("Enter 0 to start the game: "))
is_game_on = 0

if(start_game == 0):
    is_game_on = 1

if(is_game_on):
    
    score_comp = 0
    score_user = 0


    comp_value = random.randint(1,3)
    user_value = int(input("Enter your choice: "))
    print()

    if(comp_value == 1 and user_value == 2):
        score_comp = score_comp + 1
        print("Score: \nComp: ",score_comp,"\nUser: ",score_user)
        print("Computer wins!")
        print()
        

    elif comp_value == 2 and user_value == 3:
        score_comp = score_comp + 1
        
        print("Score: \nComp: ",score_comp,"\nUser: ",score_user)
        print("Computer wins!")
        print()
        

    elif comp_value == 3 and user_value == 1:
        score_comp = score_comp + 1
        
        print("Score: \nComp: ",score_comp,"\nUser: ",score_user)
        print("Computer wins!")
        print()
        

    else:
        score_user = score_user + 1
        print("Score: \nComp: ",score_comp,"\nUser: ",score_user)
        print("User wins!")
        print()
        

    print("Game ended")


