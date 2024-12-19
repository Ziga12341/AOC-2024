import unittest
from collections import defaultdict

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
s = "small_input.txt"
l = "input.txt"


def read_lines(file: str) -> list:
    with open(file, "r", encoding="utf-8") as file:
        return [line.strip() for line in file]


small_input: list[str] = read_lines(s)
large_input: list[str] = read_lines(l)


def add_star(engine):
    first_last_line = ["*" * (len(engine[0]) + 2)]
    new_engine = [f"*{row}*" for row in engine]
    return first_last_line + new_engine + first_last_line


def get_number_from_position(grid, trail_height: int):
    trail_position = set()
    for y, engine_line in enumerate(grid):
        for x, char in enumerate(engine_line):
            if char == str(trail_height):
                trail_position.add((x, y))
    return trail_position


def grid_to_dict_by_trail_heights(grid):
    all_hiking_trails = defaultdict(set)
    for i in range(10):
        all_hiking_trails[i] = get_number_from_position(grid, i)
    return all_hiking_trails


def all_trailhead(grid):
    initial_dict_with_starting_points = defaultdict(list)
    for starting_point in grid_to_dict_by_trail_heights(grid)[0]:
        initial_dict_with_starting_points[0].append([starting_point])
    return initial_dict_with_starting_points


def is_neighbour(x, y, x1, y1, directions):
    is_any_true = []
    for direction in directions:
        dx, dy = directions[direction]
        is_any_true.append(x + dx == x1 and y + dy == y1)
    return any(is_any_true)


def all_pairs(grid, directions):
    pairs = defaultdict(list)
    for i in range(10):
        for x, y in grid_to_dict_by_trail_heights(grid)[i]:
            for x1, y1 in grid_to_dict_by_trail_heights(grid)[i + 1]:
                if is_neighbour(x, y, x1, y1, directions):
                    pairs[(x, y)].append((x1, y1))
    return pairs


def collect_all_pairs(grid, directions):
    set_of_pairs = set()
    pairs = all_pairs(grid, directions).items()
    for current, next_candidates in pairs:
        for next_candidate in next_candidates:
            set_of_pairs.add((current, next_candidate))
    return set_of_pairs


def find_one_more_step(tuple_with_previous_steps, pairs):
    set_with_new_step = set()
    previous_steps = tuple_with_previous_steps

    for tuple_one in previous_steps:
        last_1 = tuple_one[-1]

        for tuple_two in pairs:
            first_2 = tuple_two[0]
            last_2 = tuple_two[-1]

            if last_1 == first_2:
                set_with_new_step.add(tuple_one + (last_2,))
    return set_with_new_step


def find_all_paths(set_pairs, pair, n=7):
    # set_of_tuples = list(set_pairs)
    set_of_tuples = find_one_more_step(set_pairs, pair)

    if n == 0:
        return set_of_tuples
    else:
        set_pairs = set_of_tuples
        return find_all_paths(set_pairs, pair, n - 1)


# count last one which should be unique...last one should be unique

def count_only_which_finished_in_nine_once(grid_input, directions):
    counter = 0
    visited = set()
    for path in find_all_paths(collect_all_pairs(grid_input, directions), collect_all_pairs(grid_input, directions)):
        # if path[0] in grid_to_dict_by_trail_heights(grid_input)[0] and path[-1] in \
        #         grid_to_dict_by_trail_heights(grid_input)[9]:
        if (path[0], path[-1]) not in visited:
            counter += 1
            visited.add((path[0], path[-1]))
    return counter


print("Part 1: ", count_only_which_finished_in_nine_once(large_input, directions))
print("Part 2: ",
      len(find_all_paths(collect_all_pairs(large_input, directions), collect_all_pairs(large_input, directions))))


class TestFunctions(unittest.TestCase):
    def setUp(self):
        self.small_input: list[str] = read_lines(s)
        self.large_input: list[str] = read_lines(l)

    def test_count_valid_paths(self):
        self.assertEqual(count_only_which_finished_in_nine_once(self.small_input, directions), 36)
        self.assertEqual(
            len(find_all_paths(collect_all_pairs(self.small_input, directions), collect_all_pairs(self.small_input, directions))),
            81)

        # self.assertEqual(count_only_which_finished_in_nine_once(self.large_input, directions), 789)