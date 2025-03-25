def function(lst):
    print(lst)
    
def get_lst():
    list = []
    user = input("Enter a value: ")
    while user != "":
        list.append(user)
        user = input("Enter a value: ")
    return list

def main():
    lst1 = get_lst()
    function(lst1)
    
main()