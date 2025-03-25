import random
def play():
   
    computer = random.choice(['r','p','s'])
    while True:
        user = input("'R' for rock, 'P' for paper, 'S' for scissor and 'E' for exit: ").lower()
        computer = random.choice(['r','p','s'])
        if user == computer:
            print("Game was draw")
    
        else:
            win(user,computer)
        if user == "e":
            break
        
    
def win(user,computer):
    score = 0
    if (user == 'r' and computer == 's' ) or (user == 'p' and computer == 'r') or (user == 's' and computer == 'p'):
        print("You Won")
        score += 1
        print(f"Your score is {score}")
    elif (computer == 'r' and user == 's' ) or (computer == 'p' and user == 'r') or (computer == 's' and user == 'p'):
        print("You lost!")
    elif user == 'e':
        print("Exit the game")
    else:
        print("Enter a valid character!")
        
 
play()       