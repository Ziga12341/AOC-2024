import unittest

s = "small_input.txt"
l = "input.txt"


def read_lines(file: str) -> list:
    with open(file, "r", encoding="utf-8") as file:
        return [line.strip() for line in file]


small_input: list[str] = read_lines(s)
large_input: list[str] = read_lines(l)


# you need to add dots over input... to avoid index otu of range
def add_four_dots(engine):
    first_last_line = ["." * (len(engine[0]) + 8)]
    new_engine = [f"....{row}...." for row in engine]
    return first_last_line * 4 + new_engine + first_last_line * 4


def add_one_dot(engine):
    first_last_line = ["." * (len(engine[0]) + 2)]
    new_engine = [f".{row}." for row in engine]
    return first_last_line + new_engine + first_last_line


print(add_four_dots(small_input))

# L - left
# R - right
# D - down
# U - up
# LD - left down
# RD - right down
# LU - left up
# RU - right up

directions = {
    "L": [(-1, 0), (-2, 0), (-3, 0)],
    "R": [(1, 0), (2, 0), (3, 0)],
    "D": [(0, 1), (0, 2), (0, 3)],
    "U": [(0, -1), (0, -2), (0, -3)],
    "LD": [(-1, 1), (-2, 2), (-3, 3)],
    "RD": [(1, 1), (2, 2), (3, 3)],
    "LU": [(-1, -1), (-2, -2), (-3, -3)],
    "RU": [(1, -1), (2, -2), (3, -3)],
}


def is_xmas_in_direction(engine, directions, x, y, direction):
    # index all numbers... go left right diagonal for each number end check if there is XMAS
    # right down diagonale - df +(4,4)
    # get list of all directions
    x = x + 4
    y = y + 4
    list_of_all_part_directions = directions[direction]
    collect_chars = [engine[y][x]]
    for part_of_direction in list_of_all_part_directions:
        dx, dy = part_of_direction
        char_in_new_position = engine[y + dy][x + dx]
        collect_chars.extend(char_in_new_position)
    # check if special char in new position
    join_all = "".join(collect_chars)
    return join_all == "XMAS"


def is_valid_all_directions_xmas(engine, directions, x, y):
    return sum(is_xmas_in_direction(engine, directions, x, y, direction) for direction in directions)


def sum_all_valid_directions_for_xmas(file_path):
    sum_all_direction = 0
    file_input = read_lines(file_path)
    engine = add_four_dots(file_input)

    for x, engine_line in enumerate(file_input):
        for y, char in enumerate(engine_line):
            sum_all_direction += is_valid_all_directions_xmas(engine, directions, x, y)
    return sum_all_direction


#  M.S | S.M | M.M | S.S |
#  .A. | .A. | .A. | .A. |
#  M.S | S.M | S.S | M.M |


def from_position_3_times_3_to_string(engine, x: int, y: int) -> str:
    str_from_position = ""
    for dy in range(3):
        for dx in range(3):
            str_from_position += engine[y + dy][x + dx]
    return str_from_position


def check_if_mas_within_x_in_position(engine, x, y):
    # [::2] - takes every second element
    # first = "M.S.A.M.S"
    # second = "S.M.A.S.M"
    # third = "M.M.A.S.S"
    # fourth = "S.S.A.M.M"
    valid_x_mas = [
        "MSAMS",
        "SMASM",
        "MMASS",
        "SSAMM"
    ]
    return from_position_3_times_3_to_string(engine, x, y)[::2] in valid_x_mas


def all_x_mas(file_path):
    sum_all_x_mas = 0
    file_input = read_lines(file_path)
    engine = add_one_dot(file_input)

    for x, engine_line in enumerate(file_input):
        for y, char in enumerate(engine_line):
            sum_all_x_mas += check_if_mas_within_x_in_position(engine, x, y)
    return sum_all_x_mas


print("First_part: ", sum_all_valid_directions_for_xmas(l))
print("second part: ", all_x_mas(l))


class TestFunctions(unittest.TestCase):
    def setUp(self):
        self.small_input: list[str] = read_lines(s)
        self.small_engine = add_four_dots(small_input)
        self.small_engine_one_dot = add_one_dot(small_input)

    def test_direction(self):
        self.assertTrue(is_xmas_in_direction(self.small_engine, directions, 5, 0, 'R'))
        self.assertTrue(is_xmas_in_direction(self.small_engine, directions, 6, 4, 'U'))

    # 6,4 + 4
    def test_all_directions(self):
        self.assertEqual(is_valid_all_directions_xmas(self.small_engine, directions, 6, 4), 2)

    def test_from_position_3_times_3_to_string(self):
        self.assertEqual(from_position_3_times_3_to_string(small_input, 0, 0), "MMMMSAAMX")
        self.assertEqual(from_position_3_times_3_to_string(small_input, 1, 0), "MMSSAMMXS")

    def test_check_if_mas_within_x_in_position(self):
        self.assertFalse(check_if_mas_within_x_in_position(small_input, 0, 0))
        self.assertTrue(check_if_mas_within_x_in_position(small_input, 1, 0))

    def test_all_x_mas(self):
        self.assertEqual(all_x_mas(s), 9)