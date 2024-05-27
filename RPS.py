import random 

while True:
    you = input("Enter a choice(Rock, Paper, scissors):")
    choose =  ["Rock","Paper","Scissors"]
    computer = random.choice(choose)
    print("\n mychoose{you}, yourchoose{computer}\n")

    if you == computer:
        print(f"both players selected{you}.equal")
    elif you == "Rock":
        if computer == "scissors":
            print("you win")
        else:
            print("computer win")    
    elif you == "Paper": 
        if computer == "Rock":
            print("you win") 
    else:
        print("computer win")
        
    elif you == "scissors": 
        if computer == "Paper":
            print("you win") 
    else:
        print("computer win")
       
    
    play_again = input("play again?(y/n):")
    if play_again.lower() != "yes":
        break
        
        