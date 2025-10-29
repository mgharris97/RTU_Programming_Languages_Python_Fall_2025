"""
Task 2 – Greeting Function with String Manipulation
--------------------------------------------------
Write a function `greet_user(name)` that:
- removes extra spaces with .strip()
- capitalizes the first letter with .capitalize()
- returns "Hello, <Name>! Welcome to Python!"
Ask user for their name and print result.
"""


def greet_user(name: str) -> str:
    new_name = name.strip().capitalize()
    final_name = (f"Hello, {new_name}! Welcome to Python!")
    return final_name
    ##I cannot get behind the idea of not specifying a return type for a method

if __name__ == "__main__":
    name_input = input("Enter a name: ")
    print(greet_user(name_input))


