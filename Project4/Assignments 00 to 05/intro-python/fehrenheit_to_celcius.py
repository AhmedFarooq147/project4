def faren_to_celcius():
    fahrenheit = float(input("Enter Tempreture in Fahrenheit: "))
    deg_celcius = (fahrenheit - 32) * 5.0/9.0
    print(f"Tempreture: {fahrenheit}F = {deg_celcius}C")
    
faren_to_celcius()