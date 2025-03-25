def main():
    fruits = {'apple': 1.5, 'durian': 50, 'jackfruit': 80, 'kiwi': 1, 'rambutan': 1.5, 'mango': 5}
    total_ptice = 0
    for fruit in fruits:
        price = fruits[fruit]
        cust_bout = int(input(f"How many ({fruit}) do you want?: "))
        
        total_ptice += price * cust_bout
    print(f"Your total is ${total_ptice}")
    
main()