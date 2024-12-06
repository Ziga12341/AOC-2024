import unittest

s = "small_input.txt"
l = "input.txt"


def read_lines(file: str) -> list:
    with open(file, "r", encoding="utf-8") as file:
        return [line.strip() for line in file]


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
    for y, engine_line in enumerate(engine):
        for x, char in enumerate(engine_line):
            if char == "^":
                return x, y


def next_step(directions, x, y, direction):
    dx, dy = directions[direction]
    return x + dx, y + dy


def path(engine):
    direction = "U"
    starting_point = starting_point_position(engine)
    x, y = starting_point
    visited = set()
    count_visit = 0
    while not path_ends(engine, directions, x, y,
                        direction) and count_visit < 6001:  # need to provide bigger number that first part visited (evenmore times)# I try for 600001 and also get the same result
        visited.add(starting_point)
        if is_obstacle(engine, directions, x, y, direction):
            direction = change_direction(direction)
        elif count_visit == 6000:
            return 6000

        else:
            x, y = next_step(directions, x, y, direction)
            visited.add((x, y))
            count_visit += 1
    return len(visited)


# do not put an obstacle in front of an starting point df y - 1
def coordinate_where_dots(engine):
    starting_point = starting_point_position(engine)
    x0, y0 = starting_point

    set_of_dots = set()
    for y, engine_line in enumerate(engine):
        for x, char in enumerate(engine_line):
            if char == "." and char != '^':
                set_of_dots.add((x, y))
    # exclude in front of starting point
    set_of_dots.remove((x0, y0 - 1))
    return set_of_dots


def list_of_engines_with_additional_obstacles(engine):
    list_of_engine_with_obstacles = []
    for x0, y0 in coordinate_where_dots(engine):
        dots_engine = []
        for y, engine_line in enumerate(engine):
            new_line = ""
            for x, char in enumerate(engine_line):
                if x0 == x and y0 == y and char != "^":
                    new_line += "#"
                else:
                    new_line += char
            dots_engine.append(new_line)
        list_of_engine_with_obstacles.append(dots_engine)
    return list_of_engine_with_obstacles


def count_looped_engines(engine):
    count_looped = 0
    for engine_with_new_obstacle in list_of_engines_with_additional_obstacles(engine):
        if path(engine_with_new_obstacle) == 6000:
            count_looped += 1
    return count_looped


def count_dot_in_engine(engine):
    count_dot = 0
    for y, engine_line in enumerate(engine):
        for x, char in enumerate(engine_line):
            if char == ".":
                count_dot += 1
    return count_dot


print("First part: ", path(add_star(read_lines(l))))
print("Second part: ", count_looped_engines(add_star(read_lines(l))))


class TestFunctions(unittest.TestCase):
    def setUp(self):
        self.small_engine = add_star(read_lines(s))
        self.engine = add_star(read_lines(l))

    def test_path(self):
        self.assertEqual(path(self.small_engine), 41)
        self.assertEqual(path(self.engine), 4982)

    def test_count_looped_engines(self):
        self.assertEqual(count_looped_engines(self.small_engine), 6)

    def test_count_new_engines(self):
        # 16082 new engines with an additional obstacle for large engine
        self.assertEqual(count_dot_in_engine(self.small_engine) - 1,
                         (len(list_of_engines_with_additional_obstacles(self.small_engine))))
        self.assertEqual(count_dot_in_engine(self.engine) - 1,
                         (len(list_of_engines_with_additional_obstacles(self.engine))))

    def test_count_looped_engines_big_engine(self):
        # final solution
        self.assertEqual(count_looped_engines(self.engine), 1663)