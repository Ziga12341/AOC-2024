import unittest
from collections import defaultdict

s = "small_input.txt"
l = "input.txt"


def read_lines(file: str) -> list:
    with open(file, "r", encoding="utf-8") as file:
        return [line.strip() for line in file]


small_input: list[str] = read_lines(s)
large_input: list[str] = read_lines(l)

print(read_lines(s))


def get_antinodes_location(grid: list[str], x, y, x0, y0) -> set:
    collect_antiondes = set()

    dx_first, dy_first = x - x0, y - y0
    dx_second, dy_second = x0 - x, y0 - y

    # candidates for antinodes:
    x_anti_first, y_anit_first = x + dx_first, y + dy_first
    x_anti_second, y_anti_second = x0 + dx_second, y0 + dy_second

    if 0 <= x_anti_first <= len(grid[0]) and 0 <= y_anit_first <= len(grid):
        collect_antiondes.add((x_anti_first, y_anit_first))

    if 0 <= x_anti_second <= len(grid[0]) and 0 <= y_anti_second <= len(grid):
        collect_antiondes.add((x_anti_second, y_anti_second))

    return collect_antiondes


def get_locations_of_antionodes_for_the_same_frequency(grid, set_of_antennas):
    set_all_antinodes_of_frequency = set()
    for antena_1 in set_of_antennas:
        x, y = antena_1
        for antena_2 in set_of_antennas:
            x0, y0 = antena_2

            set_all_antinodes_of_frequency = set_all_antinodes_of_frequency.union(get_antinodes_location(grid, x, y, x0, y0))
    return set_all_antinodes_of_frequency


def get_all_frequencies_antennas_location(grid):
    all_frequencies = defaultdict(set)
    for y, engine_line in enumerate(grid):
        for x, char in enumerate(engine_line):
            all_frequencies[char].add((x, y))
    return all_frequencies


def count_antinodes(grid):
    all_antinodes = set()
    for char, set_of_antenna_location in get_all_frequencies_antennas_location(grid).items():
        all_antinodes = all_antinodes.union(get_locations_of_antionodes_for_the_same_frequency(grid, set_of_antenna_location))
    return len(all_antinodes)

print("First part: ", count_antinodes(small_input))
print("First part: ", count_antinodes(large_input))

class TestFunctions(unittest.TestCase):
    def setUp(self):
        self.small_input: list[str] = read_lines(s)

    def test_get_antinodes_location(self):
        self.assertEqual(get_antinodes_location(self.small_input, 8, 1, 5, 2), {(11, 0), (2, 3)})
        self.assertEqual(get_antinodes_location(self.small_input, 8, 1, 7, 3), {(6, 5)})