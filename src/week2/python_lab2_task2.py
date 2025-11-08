"""
Lab 3.2 – Comprehensions and Transformations

Goals:
- Practice list, set, and dictionary comprehensions.
- Transform and filter data concisely.

Instructions:
Given the list:
    numbers = [3, 8, -2, 7, 0, -5, 10]

1. Create a list `squares` with the square of each number.
2. Create a list `positives` containing only positive numbers.
3. Create a set `even_squares` of the squares of even numbers.
4. Create a dictionary `cubes` mapping each number to its cube.
5. Print all results.
"""
import random

# Fill in your own numbers or generate 10 random integers
numbers = []
for i in range(10):
    numbers.append(random.randint(1,10))

# TODO: Implement comprehensions
squares = []
for i in numbers:
    squares.append(i**2)

positives = []
for i in numbers:
    if i > 0:
        positives.append(i)

even_squares = []
for i in numbers:
    if i%2==0:
        even_squares.append(i**2)

cubes = []
for i in numbers:
    cubes.append(i**3)

# TODO: Print results
print("Squares:", squares)
print("Positives:", positives)
print("Even squares:", even_squares)
print("Cubes:", cubes)
