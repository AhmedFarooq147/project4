def book():
    phonebook = {}
    while True:
        user_input = input("Name: ")
        if user_input == "":
            break
        number = input("Number: ")
        phonebook[user_input] = number
    return phonebook

def pint_phonebok(phonebook):
    for item in phonebook:
        print(f"{item} -> {phonebook[item]} " )
        
def look_up(phonebook):
    while True:
        name = input("Enter Name..")
        if name == "":
            break
        if name not in phonebook:
            print(f"{name} is not in the phonebook")
        else:
            print(phonebook[name])

def main():
       final_book = book()
       print = pint_phonebok(final_book)
       look_up(final_book)
       
main()