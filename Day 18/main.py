import unittest

s = "small_input.txt"
l = "input.txt"


def read_lines(file: str, read_n_lines: int) -> list:
    with open(file, "r", encoding="utf-8") as file:
        list_of_all_lines = []
        for line in file:
            x, y = line.strip().split(",")
            x = int(x)
            y = int(y)
            list_of_all_lines.append((x, y))
        return list_of_all_lines[:read_n_lines]


small_input: list[str] = read_lines(s, 12)
large_input: list[str] = read_lines(l, 1024)


def initialize_memory_space(n):
    return ["." * n] * n

example_memory_space = initialize_memory_space(6)
print(small_input)
print(example_memory_space)

class TestFunctions(unittest.TestCase):
    def setUp(self):
        self.small_input: list[str] = read_lines(s)