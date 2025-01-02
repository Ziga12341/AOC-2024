import unittest

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


def read_lines(file_name: str) -> list:
    with open(file_name, "r", encoding="utf-8") as file:
        return [line.strip() for line in file]


small_input: list[str] = read_lines(s)
large_input: list[str] = read_lines(l)
print(small_input)


def next_step(x, y, direction):
    dx, dy = directions[direction]
    return x + dx, y + dy


def get_neighbours(x, y):
    return [next_step(x, y, direction) for direction in directions]


def find_neighbors(file_name, start):
    grid = read_lines(file_name)
    x_start, y_start = start
    region_plants_char_on_start = grid[y_start][x_start]
    visited = set()
    visited.add(start)
    queue = []
    queue.append(start)
    while queue:
        x, y = queue.pop(0)

        # Get neighbors and process them
        for neighbour in get_neighbours(x, y):
            x0, y0 = neighbour
            # new candidate the same region as on start
            if neighbour not in visited and 0 <= x0 < len(grid[0]) and 0 <= y0 < len(grid) and grid[y0][
                x0] == region_plants_char_on_start:
                queue.append(neighbour)
                visited.add(neighbour)
    return visited


print(find_neighbors(s, (0, 0)))


# I get all regions in this function
def find_regions(file_name):
    already_in_regions = set()
    all_regions = []
    # loop over input
    for y, column in enumerate(read_lines(file_name)):
        for x, char in enumerate(column):
            # take each element and check if it is not already arranged to one region
            if (x, y) not in already_in_regions:
                # this one is candidate for establish new region
                # fom this point i need to take this element and with bfs approach check neighbors
                neighbours_of_this_region = find_neighbors(file_name, (x, y))
                all_regions.append(neighbours_of_this_region)
                already_in_regions = already_in_regions.union(neighbours_of_this_region)
    return all_regions


def calculate_price_for_fence_per_region(region):
    calculate_perimeter = 0
    for plant in region:
        x, y = plant
        # for each plant calculate how many neighbors are in set of region and subtract from 4
        # if 3 neighbors ( 4 - 3 )add one to the perimeter
        # max is 3 min is 0... if all neighbours in region add 0 to perimeter
        calculate_perimeter += 4 - (len(set(get_neighbours(x, y)) & set(region)))

    # price is area * perimeter of region ... len of region is area
    return calculate_perimeter * len(region)


print(find_regions(s))
print(len(find_regions(s)))


def total_price_of_fencing_all_regions(file_input):
    return sum(calculate_price_for_fence_per_region(region) for region in find_regions(file_input))


print("First part: ", total_price_of_fencing_all_regions(l))


class TestFunctions(unittest.TestCase):
    def setUp(self):
        self.small_input: list[str] = read_lines(s)
        self.s = "small_input.txt"
        self.l = "input.txt"

    def test_sum(self):
        self.assertEqual(total_price_of_fencing_all_regions(self.s), 1930)
        self.assertEqual(total_price_of_fencing_all_regions(self.l), 1377008)