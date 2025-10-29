"""
Task 1 – Simple Function with Arithmetic
---------------------------------------
Write a function `circle_area(radius)` that returns the area of a circle.
Formula: area = π × radius²
Use the math module for π.
Ask user for radius and print result with 2 decimals.
"""

# TODO: import math
import math

##def circle_area(radius):

def circle_area(radius):
    pi = 3.14
    output = (radius**2) * math.pi
    return output


if __name__ == "__main__":
    # TODO: ask for user input, call circle_area(), and print formatted result
    ##print("Please enter a value for radius\n")
    radius_prompt = float(input("Enter radius: "))
    print(f"The area of the circle with a radius of {radius_prompt} is: {circle_area(radius_prompt):.3f}")
