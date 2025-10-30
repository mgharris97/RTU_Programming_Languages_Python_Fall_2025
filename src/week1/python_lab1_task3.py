"""
Task 3 – Function with Combined Logic
------------------------------------
Write a function `analyze_sentence(text)` that returns:
1. total character count (len)
2. word count (split)
3. whether it contains the word "Python" (case-insensitive)
Return results as a tuple and print summary in main.
"""
##iterate over each char
##

def analyze_sentence(text):
    """Return length, word count, and whether 'Python' appears in text."""
    # TODO: implement function logic
    text_length = len(text)
    word_count = len(text.split())
    is_python = "python" in text.lower()
    ##tuple
    return (text_length, word_count, is_python)

if __name__ == "__main__":
    # TODO: read sentence from input, call function, and print results
    sentence = input("Enter text: ")
    results = analyze_sentence(sentence)

    print(f"Total chars: {results[0]}")
    print(f"Word count: {results[1]}")
    print(f"Contains 'Python': {results[2]}")
##
