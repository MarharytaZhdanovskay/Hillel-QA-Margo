"""
Hometask 10. regex

Task description:
open input.txt file and find all small english letters
that match such conditions:
target small letter round exactly with three capital english letters
on the left and on the right
Match examples:
sdTRYaUVKn  -> matches "a"
NTRSjARTb   -> no match ( not exactly 3 capital letters on the left)
zDFGbOPNq   -> matches "b"
Print Output as : "Result: "<your_found_human_readable_string">
"""


import re
import os


def find_matching_letters(input_file):
    # Get the current directory
    current_directory = os.path.dirname(__file__)

    # Build the full path to the input file
    input_file_path = os.path.join(current_directory, input_file)

    with open(input_file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    pattern = r'(?<=[A-Z]{3})([a-z])(?=[A-Z]{3})'
    matches = re.findall(pattern, content)

    if matches:
        result = f"Result: {''.join(matches)}"
    else:
        result = "No matches found"

    print(result)

# Input file name


input_file = "input.txt"

# Call the function to search for matching letters
find_matching_letters(input_file)
