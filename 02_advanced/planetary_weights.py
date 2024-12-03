# Constants 
gravity_constants = {
    "Mercury": 0.38,
    "Venus": 0.91,
    "Mars": 0.38,
    "Jupiter": 2.34,
    "Saturn": 1.06,
    "Uranus": 0.92,
    "Neptune": 1.19,
}

# Weight Calculation
def calculate_weight_on_planet(earth_weight, planet):
    if planet in gravity_constants:
        weight_on_planet = earth_weight * gravity_constants[planet]
        return f"Your weight on {planet} is: {weight_on_planet:.2f} kg"
    else:
        return "Invalid planet name."

def main():
    while True:
        try:
            earth_weight = float(input("Enter your weight on Earth (in kg): "))
            break
        except ValueError:
            print("Weight must be a numeric value. Please try again.")

    planet = input("Enter the name of a planet in our solar system: ")
    print(calculate_weight_on_planet(earth_weight, planet))

# Call the main function
if __name__ == "__main__":
    main()
