import unittest
from collections import defaultdict, OrderedDict

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


# for dictionary with keys of numbers and values set of numbers that must be printed after that one
def make_dict_to_forward_lookup(file_path) -> tuple:
    forward_dict = defaultdict(set)
    page_ordering_rules, pages_to_produce = read_lines(file_path)
    for rule in page_ordering_rules:
        first, second = rule.split("|")
        forward_dict[int(first)].add(int(second))
    return forward_dict


# for part 2 reorder invalid pages to meet requirements and become valid
def sort_to_valid_pages(file_path, set_of_pages):
    forward_dict = make_dict_to_forward_lookup(file_path)
    how_many_element_in_forward_dicts = defaultdict(int)
    for element_1 in set_of_pages:
        for element_2 in set_of_pages:
            # in which element all elements in forward dict
            # next valid number in an order list must be present in more list/sets of numbers in a forward lookup list
            if element_1 in forward_dict[element_2]:
                how_many_element_in_forward_dicts[element_1] += 1

    for element in set_of_pages:
        if element not in how_many_element_in_forward_dicts:
            how_many_element_in_forward_dicts[element] = 0

    reverse_how_many_element_in_forward_dicts = {value: key for key, value in how_many_element_in_forward_dicts.items()}
    return [key for value, key in sorted(reverse_how_many_element_in_forward_dicts.items())]


def loop_through_pages(file_path):
    sum_valid_middle_elements = 0
    new_valid_counter = 0
    forward_dict = make_dict_to_forward_lookup(file_path)
    page_ordering_rules, pages_to_produce = read_lines(file_path)
    for set_of_pages in pages_to_produce:
        set_of_pages = set_of_pages.split(",")
        set_of_pages = [int(page) for page in set_of_pages]
        all_valid = True

        for i, page in enumerate(set_of_pages):
            current_element_in_page = set_of_pages[i]
            looking_forward_elements = set(set_of_pages[i + 1:])
            if not looking_forward_elements.issubset(forward_dict[current_element_in_page]):
                all_valid = False
        if all_valid:
            the_element = set_of_pages[len(set_of_pages) // 2]
            sum_valid_middle_elements += the_element
        else:
            new_pages = sort_to_valid_pages(file_path, set_of_pages)
            the_element = new_pages[len(new_pages) // 2]
            new_valid_counter += the_element
    return sum_valid_middle_elements, new_valid_counter


print("First part: ", loop_through_pages(l)[0])
print("Second part: ", loop_through_pages(l)[1])


class TestFunctions(unittest.TestCase):
    def setUp(self):
        self.small_input = read_lines(s)

    def test_loop_through_pages(self):
        self.assertEqual(loop_through_pages(s)[0], 143)
        self.assertEqual(loop_through_pages(s)[1], 123)

    def test_sort_to_valid_pages(self):
        self.assertEqual(sort_to_valid_pages(s, [97, 13, 75, 29, 47]), [97, 75, 47, 29, 13])