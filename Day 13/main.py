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


def sum_lowest_price_per_claw_machines(file_name):
    return sum(calculate_lowest_price(button_a[0], button_a[1], button_b[0], button_b[1], price[0], price[1]) for
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

    def test_sum_lowest_price(self):
        self.assertEqual(sum_lowest_price_per_claw_machines(self.s), 480)
        self.assertEqual(sum_lowest_price_per_claw_machines(self.l), 31897)