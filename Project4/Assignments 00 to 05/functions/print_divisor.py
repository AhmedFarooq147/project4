def print_division():
    num = int(input("Enter a number:"))
    print("Here are the divisors of", num, end=" ")
    for i in range(num):
        curr_divisor = i + 1
        if num % curr_divisor == 0:
            print( curr_divisor , end=" ")
            
            
print_division()
        