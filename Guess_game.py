import random
print("Welcome to my computer quiz!")

playing = input("Do you want to play? ").lower()

if playing != "yes":
    quit()


    
player_score = 0
computer_score = 0
count = 0

def guess_game():
    computer = random.randint(1,20)
    attempt = 0
    while True:
        user = int(input("Enter the number :"))
        attempt+=1

        if attempt >=5:
            print("too many attempts")
            break
        else:
            if computer > user:
                print("Your guessing low number")
            elif computer < user:
                print("Your guessing high number")
            else:
                print("Congrats you guess the right number")
                break
    print("Number of attempts",attempt)

guess_game()
        
