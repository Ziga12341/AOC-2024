import unittest
from functools import lru_cache

s = "small_input.txt"
l = "input.txt"


def read_lines(file_path: str) -> list[int]:
    with open(file_path, "r", encoding="utf-8") as file_path:
        return [int(stone) for stone in file_path.readline().split(" ")]


small_input: list[int] = read_lines(s)
large_input: list[int] = read_lines(l)


# 512072, 1, 20, 24, 28676032

def blink(list_of_arrangement):
    list_after_blink = []
    for stone in list_of_arrangement:
        if stone == 0:
            list_after_blink.append(1)
        else:
            len_stone = len(str(stone))
            if len_stone % 2 == 0 and stone != 0:
                first = str(stone)[:len_stone // 2]
                second = str(stone)[len_stone // 2:]
                first_int = int(first)
                second_int = int(second)
                if set(first) == {0}:
                    list_after_blink.append(0)
                else:
                    list_after_blink.append(first_int)
                if set(second) == {0}:
                    list_after_blink.append(0)
                else:
                    list_after_blink.append(second_int)
            else:
                list_after_blink.append(stone * 2024)

    return list_after_blink


def next_blink(file_path):
    arrangement = read_lines(file_path)
    return blink(arrangement)


# !only this function in needed for solving puzzle!

@lru_cache(maxsize=None)
def blink_stone(stone: int, n: int) -> int:
    len_arrangements = 0
    if n == 0:
        return 1
    else:
        # next_arrangement = []
        if stone == 0:
            len_arrangements += blink_stone(1, n - 1)
        else:
            len_stone = len(str(stone))
            if len_stone % 2 == 0 and stone != 0:
                first = str(stone)[:len_stone // 2]
                second = str(stone)[len_stone // 2:]
                first_int = int(first)
                second_int = int(second)
                if set(first) == {'0'}:
                    len_arrangements += blink_stone(0, n - 1)

                else:
                    len_arrangements += blink_stone(first_int, n - 1)
                if set(second) == {'0'}:
                    len_arrangements += blink_stone(0, n - 1)
                else:

                    len_arrangements += blink_stone(second_int, n - 1)

            else:
                len_arrangements += blink_stone(stone * 2024, n - 1)
    return len_arrangements


def count_stones_when_blinking(file_name, blink_times):
    counter = 0
    for stone in read_lines(file_name):
        counter += blink_stone(stone, blink_times)
    return counter


print("First part: ", count_stones_when_blinking(l, 25))
print("Second part: ", count_stones_when_blinking(l, 75))


class TestFunctions(unittest.TestCase):
    def setUp(self):
        self.s = "small_input.txt"
        self.l = "input.txt"

    def test_blink(self):
        self.assertEqual(blink(small_input), [253000, 1, 7])
        self.assertEqual(blink([253, 0, 2024, 14168]), [512072, 1, 20, 24, 28676032])
        self.assertEqual(blink([512072, 1, 20, 24, 28676032]), [512, 72, 2024, 2, 0, 2, 4, 2867, 6032])

    def test_count_stones(self):
        self.assertEqual(next_blink(self.s), [253000, 1, 7])

    def test_blink_n_times(self):
        self.assertEqual(count_stones_when_blinking(self.s, 6), 22)
        self.assertEqual(count_stones_when_blinking(self.s, 25), 55312)
        self.assertEqual(count_stones_when_blinking(self.l, 25), 212655)
        self.assertEqual(count_stones_when_blinking(self.l, 75), 253582809724830)