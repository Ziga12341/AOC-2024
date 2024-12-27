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

def design_possible(design:str, towel_patterns:list) -> bool:
    pattern_not_in_design = []
    for pattern in towel_patterns:
        if pattern not in design:
            pattern_not_in_design.append(True)
        else:
            pattern_not_in_design.append(False)
    # stop condition if there cannot continue with get smaller design
    if all(pattern_not_in_design):
        return False
    else:
        for pattern in towel_patterns:
            if pattern == design:
                return True
            elif pattern in design:
                pattern_first_index = design.find(pattern)
                pattern_len = len(pattern)
                design_possible(design[:pattern_first_index] + design[pattern_first_index + pattern_len:], towel_patterns)

print(design_possible("brwrr", read_lines(s)[0]))

class TestFunctions(unittest.TestCase):
    def setUp(self):
        self.small_input = read_lines(s)
        self.towel_patterns_small = read_lines(s)[0]
        self.towel_patterns_large = read_lines(l)[0]

    def test_possible_designs(self):
        self.assertTrue(design_possible("brwrr", self.towel_patterns_small))
        self.assertFalse(design_possible("ubwu", self.towel_patterns_small))
        self.assertFalse(design_possible("bbrgwb", self.towel_patterns_small))