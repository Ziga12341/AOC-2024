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


# def design_possible(design_candidates: list, towel_patterns: list) -> bool:
#     new_design_candidates = []
#     # stop condition: there is no candidate in design_candidates which would have one of towel_patterns in string -
#     # cannot continue recursion and can get a smaller chunk from current candidates
#
#     towel_patterns_in_design_candidates = [True if towel_pattern in design_candidate else False for design_candidate in
#                                            design_candidates for towel_pattern in towel_patterns]
#     # any(): are there any True in it
#     if not any(towel_patterns_in_design_candidates):
#         return False
#     # make a problem smaller in else - remove towel pattern form design string and append it to another "loop"
#     else:
#         for design_candidate in design_candidates:
#             for pattern in towel_patterns:
#                 # I check if we have a pattern the same as design (stop recursion)
#                 if pattern == design_candidate:
#                     return True
#                 if pattern in design_candidate:
#                     pattern_first_index = design_candidate.find(pattern)
#                     pattern_len = len(pattern)
#                     new_design_candidates.append(
#                         design_candidate[:pattern_first_index] + design_candidate[pattern_first_index + pattern_len:])
#
#         return design_possible(new_design_candidates, towel_patterns)


# this do not work lru cache need immutable inputs
# @lru_cache(maxsize=None)
# def design_possible(design_candidates: set, towel_patterns: list) -> bool:
#     new_design_candidates = set()
#     # stop condition: there is no candidate in design_candidates which would have one of towel_patterns in string -
#     # cannot continue recursion and can get a smaller chunk from current candidates
#
#     towel_patterns_in_design_candidates = [True if towel_pattern in design_candidate else False for design_candidate in
#                                            design_candidates for towel_pattern in towel_patterns]
#     # any(): are there any True in it
#     if not any(towel_patterns_in_design_candidates):
#         return False
#     # make a problem smaller in else - remove towel pattern form design string and append it to another "loop"
#     else:
#         for design_candidate in design_candidates:
#             for pattern in towel_patterns:
#                 # I check if we have a pattern the same as design (stop recursion)
#                 if pattern == design_candidate:
#                     return True
#                 if pattern in design_candidate:
#                     pattern_first_index = design_candidate.find(pattern)
#                     pattern_len = len(pattern)
#                     new_design_candidates.add(
#                         design_candidate[:pattern_first_index] + design_candidate[pattern_first_index + pattern_len:])
#
#         return design_possible(new_design_candidates, towel_patterns)
#
#
# print(design_possible({"ubwu"}, read_lines(s)[0]))  # FAlse
# print(design_possible({"brwrr"}, read_lines(s)[0]))  # RETURN TRUE
# towel_patterns = read_lines(l)[0]

#
# @lru_cache(maxsize=None)
# def design_possible(design: str, file_name:str) -> bool:
#     towel_patterns, list_of_designs = read_lines(file_name)
#     # stop condition: none of towel patterens in design
#     if not any([True if towel_pattern in design else False for towel_pattern in towel_patterns]):
#         return False
#     else:
#         for towel_pattern_0 in towel_patterns:
#             # if design small enough to be the same sa towel pattern this is valid (possible) desigen
#             if towel_pattern_0 == design:
#                 return True
#             elif towel_pattern_0 in design:
#                 pattern_first_index = design.find(towel_pattern_0)
#                 pattern_len = len(towel_pattern_0)
#                 new_design = design[:pattern_first_index] + design[pattern_first_index + pattern_len:]
#                 recursion_function = design_possible(new_design, file_name)
#                 if recursion_function:
#                     return True

# this function pass tests but do not pass large input
@lru_cache(maxsize=None)
def design_possible(design: str, file_name:str) -> bool:
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
            if pattern in design:
                pattern_first_index = design.find(pattern)
                pattern_len = len(pattern)
                new_design = design[:pattern_first_index] + design[pattern_first_index + pattern_len:]
                recursion_function = design_possible(new_design, file_name)
                if recursion_function:
                    return True

print(design_possible("ubwu", s))  # FAlse
print(design_possible("brwrr", s))  # RETURN TRUE


def count_possible_designs(file_name):
    counter = 0
    towel_patterns, list_of_designs = read_lines(file_name)
    for design in list_of_designs:
        recursion_function_result = design_possible(design, file_name)
        if recursion_function_result:
            counter += recursion_function_result


    return counter


print("First part: ", count_possible_designs(l))
# first part too high: 400 = this are all possible...

class TestFunctions(unittest.TestCase):
    def setUp(self):
        self.s = "small_input.txt"
        self.towel_patterns_small = read_lines(s)[0]
        self.towel_patterns_large = read_lines(l)[0]

    def test_possible_designs(self):
        self.assertFalse(design_possible("tone", self.s))
        self.assertTrue(design_possible("brwrr", self.s))
        self.assertFalse(design_possible("ubwu", self.s))
        self.assertFalse(design_possible("bbrgwb", self.s))

    def test_count_possible(self):
        self.assertEqual(count_possible_designs(self.s), 6)