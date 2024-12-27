import unittest
from typing import Tuple, List, Any

s = "small_input.txt"
l = "input.txt"


def read_lines(file_name: str) -> tuple[list[Any] | list[str], list[str]]:
    with open(file_name, "r", encoding="utf-8") as file_name:
        towel_patterns = []
        list_of_designs = []
        is_new_line = False
        for line in file_name:
            if line == "\n":
                is_new_line = True

            elif not is_new_line:
                towel_patterns = (line.strip().split(", "))
            else:
                list_of_designs.append(line.strip())
        return towel_patterns, list_of_designs


small_input = read_lines(s)
large_input = read_lines(l)
print(small_input)


class TestFunctions(unittest.TestCase):
    def setUp(self):
        self.small_input = read_lines(s)