import random

def my_number():
    my_num = random.randint(1,99)
    i = 10
    print("Guess the number between 1-99")
    print("You have 10 attempts")
    while i >0:
        user_guess = int(input("Enter a new number:"))
        if user_guess > my_num:
            print(f"Your guess is to high")
        if user_guess < my_num:
            print("your guees is to low")
        i -= 1
        if i != 0:
            print(f"you have {i} attemps remaining")
    
        if user_guess == my_num:
            print(f" Congrats! The number was: {my_num}")
            break

        
my_number()
        