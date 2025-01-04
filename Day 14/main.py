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
print(small_input)


def calculate_robots_location_after_n_seconds(robot_initial, seconds, grid_x, grid_y):
    position = robot_initial[0]
    velocity = robot_initial[1]

    move_to_x = velocity[0] * seconds
    move_to_y = velocity[1] * seconds

    if move_to_x < 0:
        move_x_just_once_per_grid = (abs(move_to_x) % grid_x)
        move_x_just_once_per_grid = - move_x_just_once_per_grid
    else:
        move_x_just_once_per_grid = move_to_x % grid_x

    if move_to_y < 0:
        move_y_just_once_per_grid = (abs(move_to_y) % grid_y)
        move_y_just_once_per_grid = - move_y_just_once_per_grid
    else:
        move_y_just_once_per_grid = move_to_y % grid_y

    new_position_x = move_x_just_once_per_grid + position[0]
    new_position_y = move_y_just_once_per_grid + position[1]

    if new_position_x > grid_x:
        new_position_x = new_position_x - grid_x
    elif new_position_x < 0:
        new_position_x = new_position_x + grid_x

    elif new_position_y > grid_y:
        new_position_y = new_position_y - grid_y
    elif new_position_y < 0:
        new_position_y = new_position_y + grid_y

    return new_position_x, new_position_y


# print(calculate_robots_location_after_n_seconds(((2, 4), (2, -3)), 5, 11, 7))
print(calculate_robots_location_after_n_seconds(((6, 3), (-1, -3)), 100, 11, 7))

# (9, 7) wrong?
print([calculate_robots_location_after_n_seconds(robot_initial, 100, 11, 7) for robot_initial in read_lines(s)])
def calculate_number_of_robots_in_quadrant(file_name, seconds, grid_x, grid_y):
    new_locations = [calculate_robots_location_after_n_seconds(robot_initial, seconds, grid_x, grid_y) for robot_initial in read_lines(file_name)]
    up_left_quadrant = []
    up_right_quadrant = []
    down_left_quadrant = []
    down_right_quadrant = []

    for x,y in new_locations:
        if x < (grid_x - 1) / 2 and y < (grid_y - 1) / 2:
            up_left_quadrant.append((x,y))
        elif x > (grid_x - 1) / 2 and y < (grid_y - 1) / 2:
            up_right_quadrant.append((x,y))
        elif x < (grid_x - 1) / 2 and y > (grid_y - 1) / 2:
            down_left_quadrant.append((x,y))
        elif x > (grid_x - 1) / 2 and y > (grid_y - 1) / 2:
            down_right_quadrant.append((x,y))
        else:
            print("middle", (x,y))
    return len(up_left_quadrant) * len(up_right_quadrant) * len(down_right_quadrant) * len(down_left_quadrant)


print(calculate_number_of_robots_in_quadrant(s, 100, 11, 7))

class TestFunctions(unittest.TestCase):
    def setUp(self):
        self.small_input: list[str] = read_lines(s)
        self.s = "small_input.txt"

    def test_move_after_time(self):
        self.assertEqual(calculate_robots_location_after_n_seconds(((2, 4), (2, -3)), 5, 11, 7), (1, 3))
        self.assertEqual(calculate_robots_location_after_n_seconds(((0, 4), (3, -3)), 100, 11, 7),
                         (3, 5))  # not 100 percent sure

    def test_quadrants_multiplications(self):
        self.assertEqual(calculate_number_of_robots_in_quadrant(self.s, 100, 11,7), 12)