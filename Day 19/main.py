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


# def design_possible(design:str, towel_patterns:list) -> bool:
#     pattern_not_in_design = []
#     for pattern in towel_patterns:
#         if pattern not in design:
#             pattern_not_in_design.append(True)
#         else:
#             pattern_not_in_design.append(False)
#     # stop condition if there cannot continue with get smaller design
#     if all(pattern_not_in_design):
#         return False
#     else:
#         for pattern in towel_patterns:
#             if pattern == design:
#                 return True
#             elif pattern in design:
#                 pattern_first_index = design.find(pattern)
#                 pattern_len = len(pattern)
#                 design_possible(design[:pattern_first_index] + design[pattern_first_index + pattern_len:], towel_patterns)
def design_possible(design: str, towel_patterns: list) -> bool:
    new_parts_of_design_candidates = [design]
    pattern_not_in_design = []

    # stop condition if there smaller design in candidates
    if not new_parts_of_design_candidates:
        return False
    else:
        for pattern in towel_patterns:
            if pattern in new_parts_of_design_candidates:
                return True
            candidate = new_parts_of_design_candidates.pop(0)
            pattern_first_index = candidate.find(pattern)
            pattern_len = len(pattern)
            new_parts_of_design_candidates.extend(
                candidate[:pattern_first_index] + candidate[pattern_first_index + pattern_len:])

        return design_possible(new_parts_of_design_candidates, towel_patterns)


def design_possible(design: list, towel_patterns: list) -> bool:
    new_parts_of_design_candidates = []

    # stop condition if there smaller design in candidates
    if not new_parts_of_design_candidates:
        return False
    else:
        for pattern in towel_patterns:
            if pattern in new_parts_of_design_candidates:
                return True
            candidate = new_parts_of_design_candidates.pop(0)
            pattern_first_index = candidate.find(pattern)
            pattern_len = len(pattern)
            new_parts_of_design_candidates.extend(
                candidate[:pattern_first_index] + candidate[pattern_first_index + pattern_len:])

        return design_possible(new_parts_of_design_candidates, towel_patterns)


def design_possible(design_candidates: list, towel_patterns: list) -> bool:
    new_design_candidates = []
    towel_patterns_in_design_candidates = []
    # stop condition: there is no candidate in design_candidates which has one of towel_patterns in string

    for design_candidate in design_candidates:
        if design_candidate in towel_patterns:
            return True
        for towel_pattern in towel_patterns:
            if towel_pattern in design_candidate:
                towel_patterns_in_design_candidates.append(True)
            else:
                towel_patterns_in_design_candidates.append(False)
    # in one line
    # towel_patterns_in_design_candidates = [True if towel_pattern in design_candidate else False for design_candidate in design_candidates for towel_pattern in towel_patterns]

    # all(): at least one element is true - return True
    if not all(towel_patterns_in_design_candidates):
        return False
    # make a problem smaller in else - remove towel pattern form design string and append it to another "loop"
    else:
        for design_candidate in design_candidates:
            for pattern in towel_patterns:
                # I already check this up in stop condition
                # if pattern == design_candidate:
                #     return True
                if pattern in design_candidate:
                    pattern_first_index = design_candidate.find(pattern)
                    pattern_len = len(pattern)
                    new_design_candidates.append(design_candidate[:pattern_first_index] + design_candidate[pattern_first_index + pattern_len:])

        return design_possible(new_design_candidates, towel_patterns)


print(design_possible(["brwrr"], read_lines(s)[0]))


class TestFunctions(unittest.TestCase):
    def setUp(self):
        self.small_input = read_lines(s)
        self.towel_patterns_small = read_lines(s)[0]
        self.towel_patterns_large = read_lines(l)[0]

    def test_possible_designs(self):
        self.assertTrue(design_possible("brwrr", self.towel_patterns_small))
        self.assertFalse(design_possible("ubwu", self.towel_patterns_small))
        self.assertFalse(design_possible("bbrgwb", self.towel_patterns_small))