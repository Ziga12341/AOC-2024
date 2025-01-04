import unittest

s = "small_input.txt"
l = "input.txt"


def read_lines(file: str) -> list:
    with open(file, "r", encoding="utf-8") as file:
        robots_current_positions_and_velocities = []
        for line in file:
            line = line.strip().split(" ")

            position = line[0]
            position = position.split("=")[1].split(",")
            position_x = int(position[0])
            position_y = int(position[1])
            position = (position_x, position_y)

            velocities = line[1]
            velocities = velocities.split("=")[1].split(",")
            velocities_x = int(velocities[0])
            velocities_y = int(velocities[1])
            velocities = (velocities_x, velocities_y)
            robots_current_positions_and_velocities.append((position, velocities))

        return robots_current_positions_and_velocities


small_input: list[str] = read_lines(s)
large_input: list[str] = read_lines(l)


def calculate_robots_location_after_n_seconds(robot_initial, seconds, grid_x, grid_y):
    position = robot_initial[0]
    velocity = robot_initial[1]

    move_to_x = velocity[0] * seconds
    move_to_y = velocity[1] * seconds

    # if move to negative calculate decided % with negative divider

    if move_to_x < 0:
        move_x_just_once_per_grid = move_to_x % -grid_x
    else:
        move_x_just_once_per_grid = move_to_x % grid_x

    if move_to_y < 0:
        move_y_just_once_per_grid = move_to_y % -grid_y
    else:
        move_y_just_once_per_grid = move_to_y % grid_y

    new_position_x = move_x_just_once_per_grid + position[0]
    new_position_y = move_y_just_once_per_grid + position[1]

    # IF NEGATIVE OR ONE CICLE AWAY CALCULATE RIGHT POSITION
    if new_position_x < 0:
        new_position_x = new_position_x + grid_x

    if new_position_y < 0:
        new_position_y = new_position_y + grid_y

    if new_position_y >= grid_y:
        new_position_y = new_position_y - grid_y

    if new_position_x >= grid_x:
        new_position_x = new_position_x - grid_x
    return new_position_x, new_position_y


def calculate_number_of_robots_in_quadrant(file_name, seconds, grid_x, grid_y):
    # get all robots location after n seconds and provided grid size
    new_locations = [calculate_robots_location_after_n_seconds(robot_initial, seconds, grid_x, grid_y) for robot_initial
                     in read_lines(file_name)]
    up_left_quadrant = []
    up_right_quadrant = []
    down_left_quadrant = []
    down_right_quadrant = []

    # do not take middle horizontal and vertical lines
    for x, y in new_locations:
        if x < (grid_x - 1) / 2 and y < (grid_y - 1) / 2:
            up_left_quadrant.append((x, y))
        elif x > (grid_x - 1) / 2 and y < (grid_y - 1) / 2:
            up_right_quadrant.append((x, y))
        elif x < (grid_x - 1) / 2 and y > (grid_y - 1) / 2:
            down_left_quadrant.append((x, y))
        elif x > (grid_x - 1) / 2 and y > (grid_y - 1) / 2:
            down_right_quadrant.append((x, y))

    return len(up_left_quadrant) * len(up_right_quadrant) * len(down_right_quadrant) * len(down_left_quadrant)


print("Part 1: ", calculate_number_of_robots_in_quadrant(l, 100, 101, 103))


# too low 207070080
# right answer 226179492

# tree shape... what coordinates are in three shape. start on the middle... and add each column two at edges

def xmas_tree(wide, tall):
    tree_coordinates = set()
    upper_limit = wide // 2
    lower_limit = wide // 2
    for y in range(tall - 1):
        upper_limit += 1
        lower_limit += -1

        for x in range(wide):
            if x < upper_limit and x > lower_limit:
                tree_coordinates.add((x, y))

    tree_coordinates.add((wide // 2, tall - 1))
    return tree_coordinates


def all_robots_in_tree(grid_wide, grid_tall, file_name):
    max_iteration = 1000000
    seconds = 1
    xmas_tree_locations = xmas_tree(grid_wide, grid_tall)
    # get new robots arrangements every secon
    while seconds < max_iteration:
        current_robots_location = {
            calculate_robots_location_after_n_seconds(robot_initial, seconds, grid_wide, grid_tall) for robot_initial
            in read_lines(file_name)}
        # check if more than 85% of robots in xmas tree
        if len(current_robots_location & xmas_tree_locations) >= len(current_robots_location) * 0.850:
            return seconds
        else:
            seconds += 1


print("Part 2: ", all_robots_in_tree(101, 103, l))


class TestFunctions(unittest.TestCase):
    def setUp(self):
        self.small_input: list[str] = read_lines(s)
        self.s = "small_input.txt"
        self.l = "input.txt"

    def test_move_after_time(self):
        self.assertEqual(calculate_robots_location_after_n_seconds(((2, 4), (2, -3)), 5, 11, 7), (1, 3))
        self.assertEqual(calculate_robots_location_after_n_seconds(((6, 3), (-1, -3)), 100, 11, 7), (5, 4))
        self.assertEqual(calculate_robots_location_after_n_seconds(((10, 3), (-1, 2)), 100, 11, 7), (9, 0))
        self.assertEqual(calculate_robots_location_after_n_seconds(((0, 4), (3, -3)), 100, 11, 7),
                         (3, 5))
        self.assertEqual(calculate_robots_location_after_n_seconds(((2, 0), (2, -1)), 100, 11, 7),
                         (4, 5))
        self.assertEqual(calculate_robots_location_after_n_seconds(((9, 3), (2, 3)), 100, 11, 7), (0, 2))

    def test_quadrants_multiplications(self):
        self.assertEqual(calculate_number_of_robots_in_quadrant(self.s, 100, 11, 7), 12)
        self.assertEqual(calculate_number_of_robots_in_quadrant(self.l, 100, 101, 103), 226179492)

    def test_robots_in_tree(self):
        self.assertEqual(all_robots_in_tree(101, 103, self.l), 7502)