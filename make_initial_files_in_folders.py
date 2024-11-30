import os
import shutil

# Define the code to write into each main.py file as a string
code_to_write = '''import unittest

s = "small_input.txt"
l = "input.txt"


def read_lines(file: str) -> list:
    with open(file, "r", encoding="utf-8") as file:
        return [line.strip() for line in file]


small_input: list[str] = read_lines(s)
large_input: list[str] = read_lines(l)


class TestFunctions(unittest.TestCase):
    def setUp(self):
        self.small_input: list[str] = read_lines(s)

'''

for day in range(1, 26):
    day_str = f"Day {day:02d}"  # Zero-pad the day number to two digits
    new_path = os.path.join(os.getcwd(), day_str)

    # Create the directory if it doesn't exist
    if not os.path.exists(new_path):
        os.makedirs(new_path)

    # Copy input files into the directory
    shutil.copy("input.txt", os.path.join(new_path, "input.txt"))
    shutil.copy("small_input.txt", os.path.join(new_path, "small_input.txt"))

    # Write the specified code into main.py only if it doesn't already exist
    main_py_path = os.path.join(new_path, "main.py")
    if not os.path.exists(main_py_path):
        with open(main_py_path, 'w', encoding='utf-8') as f:
            f.write(code_to_write)