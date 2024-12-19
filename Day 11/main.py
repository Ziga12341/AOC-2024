import unittest
from functools import lru_cache
from collections import defaultdict

s = "small_input.txt"
l = "input.txt"


def read_lines(file_path: str) -> list[int]:
    with open(file_path, "r", encoding="utf-8") as file_path:
        return [int(stone) for stone in file_path.readline().split(" ")]


small_input: list[int] = read_lines(s)
large_input: list[int] = read_lines(l)


# 512072, 1, 20, 24, 28676032

# @lru_cache(maxsize=None)
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


@lru_cache(maxsize=None)
def blink_stone(stone):
    list_after_blink = []
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


def blink_n_times(first_arrangement, n):
    list_after_blink = first_arrangement
    if n == 0:
        return len(list_after_blink)
    else:
        for stone in list_after_blink:
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
            return blink_n_times(first_arrangement, n-1)


# 1
# def count_stones(first_arrangement, n):
#     return blink_n_times(first_arrangement, n)
sumaza = 0
for element in small_input:
    sumaza += (blink_n_times([element], 6))

print(sumaza)
print("First part: ", blink_n_times(large_input, 6))

#
# class TestFunctions(unittest.TestCase):
#     def setUp(self):
#         self.small_input: list[int] = read_lines(s)
#         self.s = "small_input.txt"
#
#     def test_blink(self):
#         self.assertEqual(blink(small_input), [253000, 1, 7])
#         self.assertEqual(blink([253, 0, 2024, 14168]), [512072, 1, 20, 24, 28676032])
#         self.assertEqual(blink([512072, 1, 20, 24, 28676032]), [512, 72, 2024, 2, 0, 2, 4, 2867, 6032])
#
#     def test_count_stones(self):
#         self.assertEqual(next_blink(self.s), [253000, 1, 7])
#
#     def test_blink_n_times(self):
#         self.assertEqual(count_stones(self.small_input, 6), 22)
#         self.assertEqual(count_stones(self.small_input, 25), 55312)