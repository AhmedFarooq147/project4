def main():
    list = [1,2,3,4]
    for item in range(len(list)):
        get_element_index = list[item]
        list[item] = get_element_index * 2
    print(list)
    
main()