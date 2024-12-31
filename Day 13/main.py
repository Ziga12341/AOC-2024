import unittest

s = "small_input.txt"
l = "input.txt"


def read_lines(file: str) -> list:
    with open(file, "r", encoding="utf-8") as file:
        return [line.strip() for line in file]


small_input: list[str] = read_lines(s)
large_input: list[str] = read_lines(l)

print(small_input)


def calculate_lowest_price(xa, ya, xb, yb, xp, yp):
    collect_prices = []
    for press_a in range(1, 101):
        for press_b in range(1, 101):

            # sum button a and b (times each button pressed) and compare with price
            if (xp, yp) == ((press_a * xa + press_b * xb), (press_a * ya + press_b * yb)):
                # press a cost 3 tokens, sum presses
                collect_prices.append(press_a * 3 + press_b)
    return min(collect_prices) if collect_prices else 0


print(calculate_lowest_price(94, 34, 22, 67, 8400, 5400))


class TestFunctions(unittest.TestCase):
    def setUp(self):
        self.small_input: list[str] = read_lines(s)

    def test_lowest_price(self):
        self.assertEqual(calculate_lowest_price(94, 34, 22, 67, 8400, 5400), 280)
        self.assertEqual(calculate_lowest_price(17, 86, 84, 37, 7870, 6450), 200)
        self.assertEqual(calculate_lowest_price(7, 8, 8, 7, 7870, 6450), 0)