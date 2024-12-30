import unittest
from typing import Tuple, List, Any
from functools import cache

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


@cache
def design_possible(design: str, file_name: str) -> bool:
    towel_patterns, list_of_designs = read_lines(file_name)
    pattern_in_design = []
    for pattern in towel_patterns:
        if pattern in design:
            pattern_in_design.append(True)
        else:
            pattern_in_design.append(False)
    if not any(pattern_in_design):
        return False
    else:
        for pattern in towel_patterns:
            # I check if we have a pattern the same as design (stop recursion)
            if pattern == design:
                return True
            # i should check only the beginning of pattern and slice from there
            if design.startswith(pattern):
                new_design = design[len(pattern):]
                if design_possible(new_design, file_name):
                    return True
    return False  # i got none because i forgot this false !!


## shorter version
# @cache
# def design_possible(design: str, file_name: str) -> bool:
#     towel_patterns, list_of_designs = read_lines(file_name)
#     # stop condition successfully destruct design - main point of function
#     if not design:
#         return True
#
#     if design in towel_patterns:
#         return True
#
#     for pattern in towel_patterns:
#         # i should check only the beginning of pattern and slice from there
#         if design.startswith(pattern):
#             new_design = design[len(pattern):]
#             if design_possible(new_design, file_name):
#                 return True
#
#     return False  # Return False # we did now destruct design

def count_ways_to_make_different_design(design: str, file_name):
    towel_patterns, list_of_designs = read_lines(file_name)
    count_ways = 0
    if not design:
        return 1

    else:
        all_options = []
        for pattern in towel_patterns:
            # i should check only the beginning of pattern and slice from there
            if design.startswith(pattern):
                new_design = design[len(pattern):]
                all_options.append(new_design)
        for option in all_options:
            count_ways += count_ways_to_make_different_design(option, file_name)
    return count_ways


def all_possible_ways(file_name):
    counter = 0
    towel_patterns, list_of_designs = read_lines(file_name)
    for design in list_of_designs:
        counter += count_ways_to_make_different_design(design, file_name)

    return counter


def count_possible_designs(file_name):
    counter = 0
    towel_patterns, list_of_designs = read_lines(file_name)
    for design in list_of_designs:
        counter += design_possible(design, file_name)

    return counter


# print("First part: ", count_possible_designs(l))
# print("Second part: ", all_possible_ways(l))


class TestFunctions(unittest.TestCase):
    def setUp(self):
        self.s = "small_input.txt"
        self.l = "input.txt"
        self.towel_patterns_small = read_lines(s)[0]
        self.towel_patterns_large = read_lines(l)[0]

    def test_possible_designs(self):
        self.assertFalse(design_possible("tone", self.s))
        self.assertTrue(design_possible("brwrr", self.s))
        self.assertFalse(design_possible("ubwu", self.s))
        self.assertFalse(design_possible("bbrgwb", self.s))
        self.assertTrue(design_possible("rgbwu", self.s))

    def test_count_possible(self):
        self.assertEqual(count_possible_designs(self.s), 6)
        self.assertEqual(count_possible_designs(self.l), 336)

    def test_different_ways(self):
        self.assertEqual(count_ways_to_make_different_design("rrbgbr", self.s), 6)
        self.assertEqual(count_ways_to_make_different_design("gbbr", self.s), 4)
        self.assertEqual(count_ways_to_make_different_design("bwurrg", self.s), 1)
        self.assertEqual(count_ways_to_make_different_design("brgr", self.s), 2)

    def test_count_ways_to_make_design_part_2(self):
        self.assertEqual(all_possible_ways(self.s), 16)