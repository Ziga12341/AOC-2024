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


def next_step(x, y, direction):
    dx, dy = directions[direction]
    return x + dx, y + dy


def get_neighbours(x, y):
    return [next_step(x, y, direction) for direction in directions]


def find_neighbors(file_name, start):
    grid = read_lines(file_name)
    x_start, y_start = start
    region_plants_char_on_start = grid[y_start][x_start]
    visited = []
    visited.append(start)
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
                visited.append(neighbour)
    return visited


# I get all regions in this function - all plants which each needs its own fence
def find_regions(file_name):
    already_in_regions = set()
    all_regions = []
    # loop over input
    for y, column in enumerate(read_lines(file_name)):
        for x, char in enumerate(column):
            # take each element and check if it is not already arranged to one region
            if (x, y) not in already_in_regions:
                # this one is candidate for establish new region
                # fom this point i need to take this element and with fload fill approach check neighbors
                neighbours_of_this_region = find_neighbors(file_name, (x, y))
                all_regions.append(neighbours_of_this_region)
                already_in_regions = already_in_regions.union(neighbours_of_this_region)
    return all_regions


# part 1
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


def total_price_of_fencing_all_regions(file_input):
    return sum(calculate_price_for_fence_per_region(region) for region in find_regions(file_input))


print("First part: ", total_price_of_fencing_all_regions(l))


# for part two... i have for each side own function to check a fence on north, south, east and west
def calculate_number_of_sides_horizontally_north(region: list):
    initial_region = set(region)
    # i will return hov many sides u have upper of plants in horizontal way
    fence_horizontally_north_counter = 0
    while region:
        plant = region.pop(0)
        x, y = plant
        # there is no plant north from this plant (no upper neighbor) add one fence
        # check initial region
        if not (x, y - 1) in initial_region:
            fence_horizontally_north_counter += 1
            # remove all neighbors from this plant from region
            for i in range(1, len(initial_region)):
                if (x + i, y) in region and (x + i, y - 1) not in initial_region:
                    region.remove((x + i, y))
                else:
                    break
                # check backwards too
            for j in range(1, len(initial_region)):
                # check backwards too
                if (x - j, y) in region and (x - j, y - 1) not in initial_region:
                    region.remove((x - j, y))
                else:
                    break

    return fence_horizontally_north_counter


def calculate_number_of_sides_horizontally_south(region: list):
    initial_region = set(region)
    # i will return hov many sides u have upper of plants in horizontal way
    fence_horizontally_south_counter = 0
    while region:
        plant = region.pop(0)
        x, y = plant
        # there is no plant south from this plant (no neighbor under) add one fence
        # check initial region
        if not (x, y + 1) in initial_region:
            fence_horizontally_south_counter += 1
            # remove all neighbors from this plant from a region in a horisontal scale
            for i in range(1, len(initial_region)):
                # i look only forward (check if correct)
                if (x + i, y) in region and (x + i, y + 1) not in initial_region:
                    region.remove((x + i, y))
                else:
                    break
                    # check backwards too
            for j in range(1, len(initial_region)):
                if (x - j, y) in region and (x - j, y + 1) not in initial_region:
                    region.remove((x - j, y))
                else:
                    break

    return fence_horizontally_south_counter


def calculate_number_of_sides_vertically_east(region: list):
    initial_region = set(region)
    # i will return hov many sides u have upper of plants in horizontal way
    fence_vertically_east_counter = 0
    while region:
        plant = region.pop(0)
        x, y = plant
        # there is no plant east from this plant (no neighbor right) add one fence
        # check initial region
        if not (x + 1, y) in initial_region:
            fence_vertically_east_counter += 1
            # remove all neighbors from this plant from a region in a vertical scale
            for i in range(1, len(initial_region)):
                # i look only forward (check if correct)
                if (x, y + i) in region and (x + 1, y + i) not in initial_region:
                    region.remove((x, y + i))
                else:
                    break
                    # check backwards too
            for j in range(1, len(initial_region)):
                # how to look backwards
                if (x, y - j) in region and (x + 1, y - j) not in initial_region:
                    region.remove((x, y - j))
                else:
                    break

    return fence_vertically_east_counter


def calculate_number_of_sides_vertically_west(region: list):
    # sides on left side - west
    initial_region = set(region)
    fence_vertically_west_counter = 0
    while region:
        plant = region.pop(0)
        x, y = plant
        # there is no plant west from this plant (no neighbor left) add one fence
        # check initial region
        if not (x - 1, y) in initial_region:
            fence_vertically_west_counter += 1
            # remove all neighbors from this plant from a region in a vertical scale
            for i in range(1, len(initial_region)):
                if (x, y + i) in region and (x - 1, y + i) not in initial_region:
                    region.remove((x, y + i))
                else:
                    break
                    # check backwards too
            for j in range(1, len(initial_region)):
                # check backwards too
                if (x, y - j) in region and (x - 1, y - j) not in initial_region:
                    region.remove((x, y - j))
                else:
                    break

    return fence_vertically_west_counter


# merge all sites... problem with function that empty me a region - is this side effect?
def number_of_sides(region: list):
    initial_region = (region)
    # sum all sides and multiply by area
    north = calculate_number_of_sides_horizontally_north(list(initial_region))
    south = calculate_number_of_sides_horizontally_south(list(initial_region))
    east = calculate_number_of_sides_vertically_east(list(initial_region))
    west = calculate_number_of_sides_vertically_west(list(initial_region))
    return east + north + south + west


def price_for_fence_with_discount_number_of_sides(region: list):
    return number_of_sides(region) * len(region)


def total_price_of_fencing_all_regions_with_discount(file_input):
    return sum(price_for_fence_with_discount_number_of_sides(region) for region in find_regions(file_input))


print("Second part: ", total_price_of_fencing_all_regions_with_discount(l))


# 838198 too high
# 821582 too high
# 820975 too high
# 815788


class TestFunctions(unittest.TestCase):
    def setUp(self):
        self.small_input: list[str] = read_lines(s)
        self.s = "small_input.txt"
        self.l = "input.txt"

    def test_sum(self):
        self.assertEqual(total_price_of_fencing_all_regions(self.s), 1930)
        self.assertEqual(total_price_of_fencing_all_regions(self.l), 1377008)

    def test_number_of_sides(self):
        self.assertEqual(number_of_sides(

            [(0, 0), (1, 0), (0, 1), (2, 0), (1, 1), (3, 0), (2, 1), (3, 1), (2, 2), (3, 2), (2, 3), (4, 2)]), 10)
        self.assertEqual(number_of_sides([(4, 0), (5, 0), (4, 1), (5, 1)]), 4)
        self.assertEqual(number_of_sides(
            [(6, 0), (7, 0), (6, 1), (7, 1), (6, 2), (8, 1), (5, 2), (5, 3), (4, 3), (3, 3), (4, 4), (4, 5), (5, 5),
             (5, 6)]), 22)
        self.assertEqual(
            number_of_sides([(8, 0), (9, 0), (9, 1), (9, 2), (8, 2), (9, 3), (7, 2), (8, 3), (7, 3), (8, 4)]), 12)
        self.assertEqual(number_of_sides(
            [(0, 2), (1, 2), (0, 3), (1, 3), (0, 4), (1, 4), (0, 5), (2, 4), (1, 5), (0, 6), (3, 4), (1, 6), (3, 5)]),
            10)
        self.assertEqual(
            number_of_sides([(6, 3), (6, 4), (5, 4), (6, 5), (7, 5), (6, 6), (7, 6), (6, 7), (7, 7), (6, 8), (6, 9)]),
            12)
        self.assertEqual(number_of_sides([(7, 4)]), 4)
        self.assertEqual(number_of_sides(
            [(9, 4), (9, 5), (8, 5), (9, 6), (8, 6), (9, 7), (8, 7), (9, 8), (8, 8), (9, 9), (7, 8), (8, 9), (7, 9)]),
            8)
        self.assertEqual(number_of_sides(
            [(2, 5), (2, 6), (3, 6), (2, 7), (4, 6), (3, 7), (1, 7), (2, 8), (4, 7), (3, 8), (1, 8), (5, 7), (3, 9),
             (5, 8)]), 16)
        self.assertEqual(number_of_sides([(0, 7), (0, 8), (0, 9), (1, 9), (2, 9)]), 6)
        self.assertEqual(number_of_sides([(4, 8), (4, 9), (5, 9)]), 6)

    def test_discount(self):
        self.assertEqual(total_price_of_fencing_all_regions_with_discount(self.s), 1206)
        self.assertEqual(total_price_of_fencing_all_regions_with_discount("small_input_2.txt"), 236)
        self.assertEqual(total_price_of_fencing_all_regions_with_discount("small_input_3.txt"), 368)
        self.assertEqual(total_price_of_fencing_all_regions_with_discount("small_input_4.txt"), 36)
        self.assertEqual(total_price_of_fencing_all_regions_with_discount("small_input_5.txt"), 946)
        self.assertEqual(total_price_of_fencing_all_regions_with_discount("small_input_6.txt"), 164)
        self.assertEqual(total_price_of_fencing_all_regions_with_discount("small_input_7.txt"), 436)
        self.assertEqual(total_price_of_fencing_all_regions_with_discount("small_input_8.txt"), 80)
        self.assertEqual(total_price_of_fencing_all_regions_with_discount("small_input_9.txt"), 236)
        self.assertEqual(total_price_of_fencing_all_regions_with_discount("small_input_10.txt"), 368)
        self.assertEqual(total_price_of_fencing_all_regions_with_discount("small_input_11.txt"), 1206)
        self.assertEqual(total_price_of_fencing_all_regions_with_discount("small_input_13.txt"), 250)
        self.assertEqual(total_price_of_fencing_all_regions_with_discount("small_input_12.txt"), 1992)
        self.assertEqual(total_price_of_fencing_all_regions_with_discount(self.l), 815788)