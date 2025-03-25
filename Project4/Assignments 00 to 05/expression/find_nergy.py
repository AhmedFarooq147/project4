def findenergy():
    mass = float(input("Enter kilos of mass: "))
    print("e = m * C^2...")
    print(f"m = {mass} kg")
    print("C = 299792458 m/s")
    c = 299792458
    E = mass*(c**2)
    print(f"{E} joules of energy!")
    
findenergy()