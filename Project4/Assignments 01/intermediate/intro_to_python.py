# Define gravitational constants relative to Earth's gravity
GRAVITY_MULTIPLES = {
    "Mercury": 0.38,
    "Venus": 0.91,
    "Earth": 1.00,
    "Mars": 0.38,
    "Jupiter": 2.34,
    "Saturn": 1.06,
    "Uranus": 0.92,
    "Neptune": 1.19
}

# Prompt the user for their weight on Earth
earth_weight_str = input("Enter your weight on Earth (kg): ")
earth_weight = float(earth_weight_str)

# Prompt the user for the name of a planet
planet = input("Enter a planet: ")

# Check if the planet is valid and calculate weight
if planet in GRAVITY_MULTIPLES:
    planetary_weight = earth_weight * GRAVITY_MULTIPLES[planet]
    rounded_planetary_weight = round(planetary_weight, 2)
    print(f"The equivalent weight on {planet}: {rounded_planetary_weight} kg")
else:
    print("Invalid planet name. Please enter a valid planet.")
