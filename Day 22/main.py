import unittest
from collections import defaultdict

s = "small_input.txt"
l = "input.txt"


def read_lines(file: str) -> list:
    with open(file, "r", encoding="utf-8") as file:
        return [int(line.strip()) for line in file]


small_input: list[str] = read_lines(s)
large_input: list[str] = read_lines(l)


def prune(secret_number: int) -> int:
    return secret_number % 16777216


def mix(initial_secret_number: int, result: int) -> int:
    return initial_secret_number ^ result


def first_step(secret_number: int) -> int:
    result = secret_number * 64
    mixing = mix(secret_number, result)
    return prune(mixing)


def second_step(secret_number: int) -> int:
    result = secret_number // 32
    mixing = mix(secret_number, result)
    return prune(mixing)


def third_step(secret_number: int) -> int:
    result = secret_number * 2048
    mixing = mix(secret_number, result)
    return prune(mixing)


def get_next_secret_number(secret_number: int) -> int:
    result_of_first_step = first_step(secret_number)
    result_of_second_step = second_step(result_of_first_step)
    return third_step(result_of_second_step)


def loop_next_numbers_n_times(initial_number: int, n: int):
    current_loop = 1
    while current_loop <= n:
        initial_number = get_next_secret_number(initial_number)
        current_loop += 1
    return initial_number


def sum_2000th_secret_number(file_name: str) -> int:
    counter = 0
    for number in read_lines(file_name):
        counter += loop_next_numbers_n_times(number, 2000)
    return counter


# for one secret number get dict of all sequences by changes and (last) value
def determine_sequence_all_result_for_one_secret_number(initial_secret_number):
    sequence_four_changes_and_value = {}
    current_loop = 0
    previous_value = int(str(initial_secret_number)[-1])
    four_changes_with_price = []
    while current_loop < 2000:
        initial_secret_number = get_next_secret_number(initial_secret_number)
        current_value = int(str(initial_secret_number)[-1])
        change_in_price = current_value - previous_value
        four_changes_with_price.append(change_in_price)
        if len(four_changes_with_price) >= 4:
            sequence = tuple(four_changes_with_price[-4:])
            if sequence not in sequence_four_changes_and_value:
                sequence_four_changes_and_value[sequence] = current_value
        previous_value = current_value
        current_loop += 1
    return sequence_four_changes_and_value


# for all initial secret numbers collect all sequences by four and append values from different secret numbers to this sequences
def collect_sequences_for_all_initial_secret_numbers(file_name):
    all_sequences_together = defaultdict(list)
    for initial_secret_number in read_lines(file_name):
        for key, value in determine_sequence_all_result_for_one_secret_number(initial_secret_number).items():
            all_sequences_together[key].append(value)
    return all_sequences_together


# just sum what values are in each sequence (sum list of values per sequence)
def sum_values_for_each_sequence(file_name):
    return sorted(
        [(sum(value), key) for key, value in collect_sequences_for_all_initial_secret_numbers(file_name).items()])


# get sum of values for best sequence
def get_sum_from_best_sequence(file_name):
    return sum_values_for_each_sequence(file_name)[-1][0]


print("Part one: ", sum_2000th_secret_number(l))
print("Part two: ", get_sum_from_best_sequence(l))


class TestFunctions(unittest.TestCase):
    def setUp(self):
        self.small_input: list[str] = read_lines(s)
        self.s = "small_input.txt"
        self.l = "input.txt"

    def test_sum_2000(self):
        self.assertEqual(sum_2000th_secret_number(self.s), 37327623)
        self.assertEqual(sum_2000th_secret_number(self.l), 19877757850)
        self.assertEqual(sum_2000th_secret_number("test_last_one_part_2.txt"), 18183557)
        self.assertEqual(sum_2000th_secret_number("test_first_one_part_2.txt"), 8876699)

    def test_final_sum_part_2(self):
        self.assertEqual(get_sum_from_best_sequence("test_last_one_part_2.txt"), 27)
        self.assertEqual(get_sum_from_best_sequence("test_first_one_part_2.txt"), 27)
        self.assertEqual(get_sum_from_best_sequence("small_input_part_2.txt"), 23)