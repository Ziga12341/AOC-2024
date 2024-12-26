import unittest

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


print(loop_next_numbers_n_times(123, 10))


def sum_2000th_secret_number(file_name: str) -> int:
    counter = 0
    for number in read_lines(file_name):
        counter += loop_next_numbers_n_times(number, 2000)
    return counter

from collections import defaultdict
def get_changes_in_prices(initial_number: int):
    
    tuple_changes_by_4 = defaultdict(int)
    current_loop = 1
    previous_value = int(str(initial_number)[-1])
    four_changes_with_price = []
    while current_loop <= 2000:
        if len(four_changes_with_price) == 4:
            if not tuple_changes_by_4[tuple(four_changes_with_price)] or tuple_changes_by_4[tuple(four_changes_with_price)] < previous_value:

                tuple_changes_by_4[tuple(four_changes_with_price)] = previous_value
            four_changes_with_price = four_changes_with_price[1:]
        else:
            initial_number = get_next_secret_number(initial_number)
            initial_last_number = int(str(initial_number)[-1])
            change_in_price = initial_last_number - previous_value
            four_changes_with_price.append(change_in_price)
            previous_value = initial_last_number
            current_loop += 1
    return tuple_changes_by_4



# print("Part one: ", sum_2000th_secret_number(l))

print(get_changes_in_prices(123))

class TestFunctions(unittest.TestCase):
    def setUp(self):
        self.small_input: list[str] = read_lines(s)
        self.s = "small_input.txt"
        self.l = "input.txt"

    def test_sum_2000(self):
        self.assertEqual(sum_2000th_secret_number(self.s), 37327623)
        self.assertEqual(sum_2000th_secret_number(self.l), 19877757850)