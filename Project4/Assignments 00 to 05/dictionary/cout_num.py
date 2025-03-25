def get_input():
    user_list = []
    while True:
        user_input = input("Enter a number: ")
        if user_input == "":
            break
        user_in = int(user_input)
        user_list.append(user_in)
        
    return user_list

def count(list):
    dect = {}
    for num in list:
        if num not in dect:
            dect[num] = 1
        else:
            dect[num] += 1
    return dect
def print_count(dictionary):
    for number in dictionary:
        print(f"{number} appears {dictionary[number]} times")
        
def main():
    final_input = get_input()
    final_counr = count(final_input)
    print_count(final_counr)
    
main()
    
           