def copy(list,data):
    for i in range(3):
        list2 = list.append(data)
        
def main():
    data = input("Enter a messagae to copy: ")
    list = []
    print(f"Before {list}")
    copy(list,data)
    print(f"List after {list}")
main()