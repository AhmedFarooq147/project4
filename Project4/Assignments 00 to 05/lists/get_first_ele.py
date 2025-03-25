def function(lst):
    print(lst[0])
    
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