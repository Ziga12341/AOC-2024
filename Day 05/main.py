import unittest
from collections import defaultdict

s = "small_input.txt"
l = "input.txt"


def read_lines(file_path: str) -> tuple[list[str], list[str]]:
    with open(file_path, "r", encoding="utf-8") as file_path:
        new_line_break_point = False
        page_ordering_rules = []
        pages_to_produce = []
        for line in file_path:
            if line == "\n":
                new_line_break_point = True
            elif new_line_break_point:
                pages_to_produce.append(line.strip())
            else:
                page_ordering_rules.append(line.strip())

        return page_ordering_rules, pages_to_produce


small_input: tuple[list[str], list[str]] = read_lines(s)
large_input: tuple[list[str], list[str]] = read_lines(l)


# make dict for after one number
# make another dict to look up before number
def make_dict_to_forward_and_backward_lookup(file_path) -> tuple:
    forward_dict = defaultdict(set)
    backward_dict = defaultdict(set)
    page_ordering_rules, pages_to_produce = read_lines(file_path)
    for rule in page_ordering_rules:
        first, second = rule.split("|")
        forward_dict[int(first)].add(int(second))
        backward_dict[int(second)].add(int(first))
    return forward_dict, backward_dict


def loop_through_pages(file_path):
    sum_valid_middle_elements = 0
    forward_dict, backward_dict = make_dict_to_forward_and_backward_lookup(file_path)
    page_ordering_rules, pages_to_produce = read_lines(file_path)
    for set_of_pages in pages_to_produce:
        set_of_pages = set_of_pages.split(",")
        set_of_pages = [int(page) for page in set_of_pages]
        all_valid = True

        for i, page in enumerate(set_of_pages):
            current_element_in_page = set_of_pages[i]
            looking_forward_elements = set(set_of_pages[i + 1:])
            looking_backward_elements = set(set_of_pages[:i])
            if not looking_forward_elements.issubset(
                    forward_dict[current_element_in_page]) and looking_backward_elements.issubset(
                backward_dict[current_element_in_page]):
                all_valid = False
        if all_valid:
            the_element = set_of_pages[len(set_of_pages) // 2]
            sum_valid_middle_elements += the_element
    return sum_valid_middle_elements


print("First part: ", loop_through_pages(l))


class TestFunctions(unittest.TestCase):
    def setUp(self):
        self.small_input = read_lines(s)

    def test_loop_through_pages(self):
        self.assertEqual(loop_through_pages(s), 143)