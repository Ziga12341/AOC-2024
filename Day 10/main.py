import unittest

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


def possible_trails_only_first_position(engine):
    trail_last_position = set()
    for y, engine_line in enumerate(engine):
        for x, char in enumerate(engine_line):
            if char == "0":
                trail_last_position.add((x, y))
    return trail_last_position


def next_step(directions, x, y, direction):
    dx, dy = directions[direction]
    return x + dx, y + dy


def next_step_valid_position(engine, directions, x, y, direction, current_trail_height: str):
    x0, y0 = next_step(directions, x, y, direction)
    if engine[y0][x0] == current_trail_height:
        return x0, y0


print(possible_trails_only_first_position(add_star(small_input)))
print(next_step_valid_position(add_star(small_input), directions, 2, 1, "L", "8"))
print(next_step_valid_position(add_star(small_input), directions, 5, 1, "D", "1"))
print("---")


def stop_position(engine, directions, x, y, direction):
    dx, dy = directions[direction]
    return engine[y + dy][x + dx] == "9"


def valid_next_step_positions(engine, directions, x, y, current_trail_height: str):
    valid_positions = []
    for direction in directions:
        next_position = next_step_valid_position(engine, directions, x, y, direction, current_trail_height)
        if next_position:
            x0, y0 = next_position
            if engine[y0][x0] == str(int(current_trail_height)):
                valid_positions.append(next_position)
    return valid_positions


print(valid_next_step_positions(add_star(small_input), directions, 2, 1, "8"))  # why just one position?
print(valid_next_step_positions(add_star(small_input), directions, 2, 1, "0"))  # why just one position?


# do not work yet
def is_valid_path(engine, directions, starting_point):
    x, y = starting_point  # starts on 0
    next_position = [starting_point]
    start_on = "9876543210"
    list_of_valid_positions = valid_next_step_positions(engine, directions, x, y, start_on)
    # stop condition
    if len(list_of_valid_positions) == 1:
        x, y = list_of_valid_positions[0]
        next_position.extend((x, y))
    if len(list_of_valid_positions) > 1:
        print(
            f"three is not one valid position, valid positions: {len(valid_next_step_positions(engine, directions, x, y, start_on))}")
    else:
        print(f"no valid")
        return False
    return len(next_position) == 9


def count_valid_paths(engine, directions):
    starting_points = possible_trails_only_first_position(engine)
    return sum(is_valid_path(engine, directions, starting_point) for starting_point in starting_points)


print("Part 1: ", count_valid_paths(add_star(small_input), directions))


class TestFunctions(unittest.TestCase):
    def setUp(self):
        self.small_input: list[str] = read_lines(s)

    def test_count_valid_paths(self):
        self.assertEqual(count_valid_paths(add_star(self.small_input), directions), 36)