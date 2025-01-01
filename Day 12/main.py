import unittest

s = "small_input.txt"
l = "input.txt"


def read_lines(file_input: str) -> list:
    with open(file_input, "r", encoding="utf-8") as file:
        return [line.strip() for line in file]


small_input: list[str] = read_lines(s)
large_input: list[str] = read_lines(l)
print(small_input)


def sum_price(file_input):
    return


class TestFunctions(unittest.TestCase):
    def setUp(self):
        self.small_input: list[str] = read_lines(s)
        self.s = "small_input.txt"

    def test_sum(self):
        self.assertEqual(sum_price(self.s), 1930)