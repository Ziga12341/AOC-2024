import unittest
from typing import List, Tuple

s = "small_input.txt"
l = "input.txt"


def read_lines(file_name: str) -> list[tuple[tuple[int, int], ...]]:
    with open(file_name, "r", encoding="utf-8") as file_name:
        claw_machines = []
        accumulator = []
        for line in file_name:

            # in case of new line
            if line == "\n":
                claw_machines.append(tuple(accumulator))
                accumulator = []
            else:
                x_and_y_only = line.strip().split(": ")[1]
                x, y = x_and_y_only.split(",")
                x = int(x[2:])
                y = int(y[3:])
                accumulator.append((x, y))
        claw_machines.append(tuple(accumulator))
        return claw_machines


small_input: list[tuple[tuple[int, int], ...]] = read_lines(s)
large_input: list[tuple[tuple[int, int], ...]] = read_lines(l)


def calculate_lowest_price(xa, ya, xb, yb, xp, yp):
    collect_prices = []
    for press_a in range(1, 101):
        for press_b in range(1, 101):

            # sum button a and b (times each button pressed) and compare with price
            if (xp, yp) == ((press_a * xa + press_b * xb), (press_a * ya + press_b * yb)):
                # press a cost 3 tokens, sum presses
                collect_prices.append(press_a * 3 + press_b)
    return min(collect_prices) if collect_prices else 0


def calculate_lowest_price_part_2(xa, ya, xb, yb, xp, yp):
    # calculation for x
    # xp = xp + 10000000000000
    # yp = yp + 10000000000000
    get_all_price_x_times_press_a = set()
    for n in reversed(range(xp // xa)):
        if (xp - n * xa) % xb == 0:
            if (yp - n * ya) % yb == 0:
                return (n * 3) + (xp - n * xa) // xb
            else:
                return 0
    #
    # # calculation for y
    # get_all_price_y_times_press_a = set()
    # for m in range(yp // ya):
    #     if (yp - m * ya) % yb == 0:
    #         get_all_price_y_times_press_a.add(m)
    #
    # # biggest element that is in for both x and y price times_press_a
    #
    # times_press_a_in_x_and_y = get_all_price_y_times_press_a & get_all_price_x_times_press_a
    # # handle classes where we do not have any match
    # if times_press_a_in_x_and_y:
    #     biggest_button_a_for_x_and_y = max(times_press_a_in_x_and_y)
    # else:
    #     return 0
    # # calculate press b
    # press_b = (xp - biggest_button_a_for_x_and_y * xa) // xb
    #
    # return biggest_button_a_for_x_and_y * 3 + press_b


print(calculate_lowest_price_part_2(94, 34, 22, 67, 8400, 5400))


def sum_lowest_price_per_claw_machines(file_name):
    return sum(calculate_lowest_price(button_a[0], button_a[1], button_b[0], button_b[1], price[0], price[1]) for
               button_a, button_b, price in read_lines(file_name))


def sum_lowest_price_per_claw_machines_second_part(file_name):
    return sum(calculate_lowest_price_part_2(button_a[0], button_a[1], button_b[0], button_b[1], price[0], price[1]) for
               button_a, button_b, price in read_lines(file_name))


print("First part: ", sum_lowest_price_per_claw_machines(l))


class TestFunctions(unittest.TestCase):
    def setUp(self):
        self.small_input: list[str] = read_lines(s)
        self.s = "small_input.txt"
        self.l = "input.txt"

    def test_lowest_price(self):
        self.assertEqual(calculate_lowest_price(94, 34, 22, 67, 8400, 5400), 280)
        self.assertEqual(calculate_lowest_price(17, 86, 84, 37, 7870, 6450), 200)
        self.assertEqual(calculate_lowest_price(7, 8, 8, 7, 7870, 6450), 0)
        self.assertEqual(calculate_lowest_price_part_2(94, 34, 22, 67, 8400, 5400), 280)
        self.assertEqual(calculate_lowest_price_part_2(17, 86, 84, 37, 7870, 6450), 200)

    def test_sum_lowest_price(self):
        self.assertEqual(sum_lowest_price_per_claw_machines(self.s), 480)
        self.assertEqual(sum_lowest_price_per_claw_machines(self.l), 31897)