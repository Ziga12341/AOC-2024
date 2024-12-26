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


def sum_2000th_secret_number(file_name: str) -> int:
    counter = 0
    for number in read_lines(file_name):
        counter += loop_next_numbers_n_times(number, 2000)
    return counter


print("Part one: ", sum_2000th_secret_number(l))


class TestFunctions(unittest.TestCase):
    def setUp(self):
        self.small_input: list[str] = read_lines(s)
        self.s = "small_input.txt"
        self.l = "input.txt"

    def test_sum_2000(self):
        self.assertEqual(sum_2000th_secret_number(self.s), 37327623)
        self.assertEqual(sum_2000th_secret_number(self.l), 19877757850)