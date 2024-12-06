import unittest

s = "small_input.txt"
l = "input.txt"


def read_lines(file: str) -> list:
    with open(file, "r", encoding="utf-8") as file:
        return [line.strip() for line in file]


small_input: list[str] = read_lines(s)
large_input: list[str] = read_lines(l)

# U - UP, R - RIGHT, D - DOWN, L - LEFT
turn = {
    "U": "R",
    "R": "D",
    "D": "L",
    "L": "U"
}


def add_star(engine):
    first_last_line = ["*" * (len(engine[0]) + 2)]
    new_engine = [f"*{row}*" for row in engine]
    return first_last_line + new_engine + first_last_line


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


def path_ends(engine, directions, x, y, direction):
    dx, dy = directions[direction]
    char_in_new_position = engine[y + dy][x + dx]
    return char_in_new_position == "*"


def is_obstacle(engine, directions, x, y, direction):
    dx, dy = directions[direction]
    char_in_new_position = engine[y + dy][x + dx]
    return char_in_new_position == "#"


def change_direction(direction):
    return turn[direction]


def starting_point_position(engine):
    for x, engine_line in enumerate(engine):
        for y, char in enumerate(engine_line):
            if engine[y][x] == "^":
                return x, y


def next_step(engine, directions, x, y, direction):
    dx, dy = directions[direction]
    return x + dx, y + dy


def path(engine):
    direction = "U"
    starting_point = starting_point_position(engine)
    x, y = starting_point
    visited = set()
    while not path_ends(engine, directions, x, y, direction):
        visited.add(starting_point)
        if is_obstacle(engine, directions, x, y, direction):
            direction = change_direction(direction)
        else:
            x, y = next_step(engine, directions, x, y, direction)
            visited.add((x, y))
    return len(visited)


print("First part: ", path(add_star(read_lines(l))))


class TestFunctions(unittest.TestCase):
    def setUp(self):
        self.small_engine = add_star(read_lines(s))
        self.engine = add_star(read_lines(l))

    def test_path(self):
        self.assertEqual(path(self.small_engine), 41)
        self.assertEqual(path(self.engine), 4982)