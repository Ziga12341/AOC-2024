import unittest
import re

s = "small_input.txt"
l = "input.txt"


def read_lines(file: str) -> str:
    with (open(file, "r", encoding="utf-8") as file):
        return file.read()


small_input: str = read_lines(s)
large_input: str = read_lines(l)


def parse_enabled(text: str) -> list[str]:
    split_dont = text.split("don't()")
    first_valid = split_dont[0]
    other_candidates_in_list = split_dont[1:]
    collect_do_candidates = [first_valid]
    for candidate in other_candidates_in_list:
        collect_do_candidates.extend(candidate.split("do()")[1:])
    return collect_do_candidates


def implement_initial_regex(text: str):
    return re.findall("mul[(]\d{1,3}[,]\d{1,3}[)]", text)


def parse_mul(text: str) -> list[list]:
    list_of_valid_numbers = []
    list_of_muls = implement_initial_regex(text)
    for mul in list_of_muls:
        remove_three_char = mul[3:]
        remove_first_last = remove_three_char[1:-1]
        only_numbers_in_string = remove_first_last.split(",")
        list_of_valid_numbers.append([int(number) for number in only_numbers_in_string])
    return list_of_valid_numbers


def multiply_valid_numbers(text: str):
    count_numbers = 0
    list_of_valid_numbers_in_list = parse_mul(text)
    for list_with_two_numbers in list_of_valid_numbers_in_list:
        count_numbers += list_with_two_numbers[0] * list_with_two_numbers[1]
    return count_numbers


def sum_all(file_path):
    text = read_lines(file_path)
    return multiply_valid_numbers(text)


def sum_enables(text: str):
    count_enabled_numbers = 0
    list_of_all_candidates_enabled = parse_enabled(text)
    for candidate in list_of_all_candidates_enabled:
        count_enabled_numbers += multiply_valid_numbers(candidate)
    return count_enabled_numbers


def sum_only_enabled(file_path: str):
    file_in_text = read_lines(file_path)
    return sum_enables(file_in_text)


print("First part: ", sum_all(l))
print("Second part: ", sum_only_enabled(l))


class TestFunctions(unittest.TestCase):
    def setUp(self):
        self.small_input: str = read_lines(s)
        self.second_part_test_str = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"

    def test_multiplying(self):
        self.assertEqual(sum_all(s), 161)

    def test_sum_of_enabled_dos(self):
        self.assertEqual(sum_only_enabled(s), 48)

    def test_parse_enabled(self):
        self.assertEqual(parse_enabled(self.second_part_test_str), ['xmul(2,4)&mul[3,7]!^', '?mul(8,5))'])