import unittest
from typing import Tuple, List, Any
from functools import lru_cache

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

@lru_cache
def design_possible(design_candidates: list, towel_patterns: list) -> bool:
    new_design_candidates = []
    # stop condition: there is no candidate in design_candidates which would have one of towel_patterns in string -
    # cannot continue recursion and can get a smaller chunk from current candidates

    towel_patterns_in_design_candidates = [True if towel_pattern in design_candidate else False for design_candidate in
                                           design_candidates for towel_pattern in towel_patterns]
    # any(): are there any True in it
    if not any(towel_patterns_in_design_candidates):
        return False
    # make a problem smaller in else - remove towel pattern form design string and append it to another "loop"
    else:
        for design_candidate in design_candidates:
            for pattern in towel_patterns:
                # I check if we have a pattern the same as design (stop recursion)
                if pattern == design_candidate:
                    return True
                if pattern in design_candidate:
                    pattern_first_index = design_candidate.find(pattern)
                    pattern_len = len(pattern)
                    new_design_candidates.append(
                        design_candidate[:pattern_first_index] + design_candidate[pattern_first_index + pattern_len:])

        return design_possible(new_design_candidates, towel_patterns)


# print(design_possible(["ubwu"], read_lines(s)[0])) # FAlse
# print(design_possible(["brwrr"], read_lines(s)[0])) # RETURN TRUE

def count_possible_designs(file_name):
    counter = 0
    towel_patterns, list_of_designs = read_lines(file_name)
    for design in list_of_designs:
        counter += design_possible([design], towel_patterns)
    return counter


# print("First part: ", count_possible_designs(l))


class TestFunctions(unittest.TestCase):
    def setUp(self):
        self.s = "small_input.txt"
        self.towel_patterns_small = read_lines(s)[0]
        self.towel_patterns_large = read_lines(l)[0]

    def test_possible_designs(self):
        self.assertFalse(design_possible(["tone"], self.towel_patterns_small))
        self.assertTrue(design_possible(["brwrr"], self.towel_patterns_small))
        self.assertFalse(design_possible(["ubwu"], self.towel_patterns_small))
        self.assertFalse(design_possible(["bbrgwb"], self.towel_patterns_small))

    def test_count_possible(self):
        self.assertEqual(count_possible_designs(self.s), 6)