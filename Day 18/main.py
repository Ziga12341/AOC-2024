import unittest
from collections import defaultdict

s = "small_input.txt"
l = "input.txt"

# L - left
# R - right
# D - down
# U - up


directions = {
    "L": (-1, 0),
    "R": (1, 0),
    "D": (0, 1),
    "U": (0, -1),
}


def read_byte_positions_from_file(file_name: str, read_number_of_lines: int) -> list:
    with open(file_name, "r", encoding="utf-8") as file_name:
        list_of_all_lines = []
        for line in file_name:
            x, y = line.strip().split(",")
            x = int(x)
            y = int(y)
            list_of_all_lines.append((x, y))
        return list_of_all_lines[:read_number_of_lines]


small_input: list[int] = read_byte_positions_from_file(s, 12)
large_input: list[int] = read_byte_positions_from_file(l, 1024)


def initialize_memory_space(n):
    return ["." * n] * n


def add_byte_position_to_grid_with_wall(grid_dimensions: int, file_name, read_number_of_lines):
    grid = initialize_memory_space(grid_dimensions)
    for x, y in read_byte_positions_from_file(file_name, read_number_of_lines):
        grid[y] = grid[y][:x] + "#" + grid[y][x + 1:]
    return grid


def next_step(directions, x, y, direction):
    dx, dy = directions[direction]
    return x + dx, y + dy


def get_neighbours(directions, x, y):
    return [next_step(directions, x, y, direction) for direction in directions]


def flood_fill_levels(grid, start, stop, directions):
    position_levels = defaultdict(int)
    level = 0
    position_levels[start] = level
    visited = set()
    visited.add(start)
    queue = []
    queue.append(start)
    while queue:
        x, y = queue.pop(0)
        if (x, y) == stop:
            return position_levels

        # Get neighbors and process them
        for neighbour in get_neighbours(directions, x, y):
            x0, y0 = neighbour
            if neighbour not in visited and 0 <= x0 < len(grid[0]) and 0 <= y0 < len(grid) and grid[y0][x0] != "#":
                queue.append(neighbour)
                visited.add(neighbour)
                position_levels[neighbour] = position_levels[(x, y)] + 1


print("Part 1: ",
      flood_fill_levels(add_byte_position_to_grid_with_wall(71, l, 1024), (0, 0), (70, 70), directions)[(70, 70)])
print("Part 2: ", flood_fill_levels(add_byte_position_to_grid_with_wall(71, l, 2960), (0, 0), (70, 70), directions))
print("Part 2: ", flood_fill_levels(add_byte_position_to_grid_with_wall(71, l, 2961), (0, 0), (70, 70), directions))
# the right answer for part 2 : 61,50

class TestFunctions(unittest.TestCase):
    def setUp(self):
        self.small_input: list[str] = read_byte_positions_from_file(s, 12)

    def test_shortest_path(self):
        self.assertEqual(
            flood_fill_levels(add_byte_position_to_grid_with_wall(7, s, 12), (0, 0), (6, 6), directions)[(6, 6)], 22)
        self.assertEqual(
            flood_fill_levels(add_byte_position_to_grid_with_wall(71, l, 1024), (0, 0), (70, 70), directions)[(70, 70)],
            436)