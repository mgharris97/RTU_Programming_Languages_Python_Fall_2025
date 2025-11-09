
"""
Lab 3.3 – Operator Frequency Counter

Goals:
- Practice using strings and dictionaries.
- Count character frequencies in user-provided text.

Instructions:
1. Ask the user for an arithmetic expression, e.g. "3 + 5 * (2 - 1) + 7 / 2".
2. Count how many times each operator occurs:
   +  -  *  /  (  )
3. Store counts in a dictionary.
4. Print the result.
"""

# TODO: Get input from the user
expression = input("Enter an arithmetic expression: ")

# Define possible operator symbols
operators = ['+', '-', '*', '/', '(', ')']

# TODO: Initialize frequency dictionary
operator_counts = {}


# TODO: Count operator occurrences
for i in expression:
    if i in operators:
        operator_counts[i] = operator_counts.get(i, 0) + 1  #checks for i in dictionary. If it exists, returns its value, if not, assigns a default value of 0

# TODO: Print results
print("Operator counts:", operator_counts)
