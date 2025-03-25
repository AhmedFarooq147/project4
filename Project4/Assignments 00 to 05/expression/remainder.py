def remainder():
    value1 = int(input("Please enter an integer to be divided: "))
    value2 = int(input("Please enter an integer to divide by: "))
    quotient = value1 // value2
    remainder = value1 % value2
    print(f"this The result of this division is {quotient} with a remainder of {remainder}")

remainder()