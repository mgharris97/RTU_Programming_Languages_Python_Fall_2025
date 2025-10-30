"""
Task 4 – Text-based Arithmetic Analyzer
--------------------------------------
Create a text-based analyzer that:
1. Counts non-space characters.
2. Counts words.
3. Extracts numbers and computes their sum and average.
Use helper functions:
- count_characters(text)
- count_words(text)
- extract_numbers(text)
- analyze_text(text)
Print formatted summary in main.
"""
import re

def count_characters(text: str) -> int: #retun type int
    """Count non-space characters in a string."""
    # TODO: implement
    char_count = len(text.replace(" ", ""))  ##remove all white spaces then count the chars
    return char_count

def count_words(text: str) -> int:
    """Count number of words in a string."""
    # TODO: implement
    word_count = len(text.split()) ##make a list of words split by white spaces where each word is an item in the list
    return word_count

def extract_numbers(text: str) -> list[int]:
    """Return list of integers found in text."""
    # TODO: implement
    nums = re.findall(r"\d+", text)
    nums_list = []
    for n in nums:
        nums_list.append(int(n))
    return nums_list


def analyze_text(text: str):
    """Perform text-based arithmetic analysis."""
    # TODO: call helper functions and compute total, average, etc.
    print("Summary: ")
    print(f"Total word count: {count_words(text)}")
    print(f"Character count excluding spaces: {count_characters(text)}")
    print(f"Numbers in text: {extract_numbers(text)}")




if __name__ == "__main__":
    # TODO: read input, call analyze_text(), and print results
    text = input("Input text: ")
    analyze_text(text)
