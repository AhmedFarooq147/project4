max_length = 3
def function(length):
    while len(length) > max_length:
        remove_list = length.pop()
        print(f"The list can only have 3 elements, but it had more than 3, so I deleted the extra ones. {remove_list}")
    
def get_lst():
    list = []
    user = input("Please enter an element of the list or press enter to stop: ")
    while user != "":
        list.append(user)
        user = input("Please enter an element of the list or press enter to stop: ")
    return list

def main():
    lst1 = get_lst()
    function(lst1)
    
main()