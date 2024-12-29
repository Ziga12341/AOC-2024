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
            return blink_n_times(first_arrangement, n - 1)


@lru_cache(maxsize=None)
def blink_n_times(first_arrangement, n):
    len_arrangements = 0
    if n == 0:
        return len(first_arrangement)
    else:
        next_arrangement = []
        for stone in first_arrangement:
            if stone == 0:
                next_arrangement.append(1)
            else:
                len_stone = len(str(stone))
                if len_stone % 2 == 0 and stone != 0:
                    first = str(stone)[:len_stone // 2]
                    second = str(stone)[len_stone // 2:]
                    first_int = int(first)
                    second_int = int(second)
                    if set(first) == {'0'}:
                        next_arrangement.append(0)
                    else:
                        next_arrangement.append(first_int)
                    if set(second) == {'0'}:
                        next_arrangement.append(0)
                    else:
                        next_arrangement.append(second_int)
                else:
                    next_arrangement.append(stone * 2024)
        return blink_n_times(tuple(next_arrangement), n - 1)


# @lru_cache(maxsize=None)
# def blink_stone(stone: int, n: int) -> int:
#     len_arrangements = 0
#     len_stone = len(str(stone))
#
#     # stop condition
#     if n == 0:
#         return len_arrangements
#
#     if stone == 0:
#         stone = 1
#         len_arrangements += 1
#     elif not len_stone % 2 == 0 and stone != 0:
#         stone = stone * 2024
#         len_arrangements += 1
#
#     else:
#         two_stones = []
#         if len_stone % 2 == 0 and stone != 0:
#             first = str(stone)[:len_stone // 2]
#             second = str(stone)[len_stone // 2:]
#             first_int = int(first)
#             second_int = int(second)
#             if set(first) == {'0'}:
#                 two_stones.append(0)
#             else:
#                 two_stones.append(first_int)
#             if set(second) == {'0'}:
#                 two_stones.append(0)
#             else:
#                 two_stones.append(second_int)
#         for stone in two_stones:
#             len_arrangements += 1
#             (blink_stone(stone, n - 1))
#
#     return len_arrangements


@lru_cache(maxsize=None)
def blink_stone(stone: int, n: int) -> int:
    len_arrangements = 0
    if n == 0:
        return 1
    else:
        # next_arrangement = []
        if stone == 0:
            len_arrangements += 1
            blink_stone(1, n - 1)
            # next_arrangement.append(1)
        else:
            len_stone = len(str(stone))
            if len_stone % 2 == 0 and stone != 0:
                first = str(stone)[:len_stone // 2]
                second = str(stone)[len_stone // 2:]
                first_int = int(first)
                second_int = int(second)
                if set(first) == {'0'}:
                    # next_arrangement.append(0)
                    len_arrangements += 1
                    blink_stone(0, n - 1)

                else:
                    len_arrangements += 1
                    blink_stone(first_int, n - 1)

                    # next_arrangement.append(first_int)
                if set(second) == {'0'}:
                    len_arrangements += 1
                    blink_stone(0, n - 1)

                    # next_arrangement.append(0)
                else:
                    len_arrangements += 1
                    blink_stone(second_int, n - 1)

                    # next_arrangement.append(second_int)
            else:
                # next_arrangement.append(stone * 2024)
                len_arrangements += 1
                blink_stone(stone * 2024, n - 1)
    print(len_arrangements)


from functools import lru_cache


@lru_cache(maxsize=None)
def blink_stone(stone: int, n: int) -> int:
    total_arrangements = 0

    if n == 0:
        return 1

    if stone == 0:
        total_arrangements += blink_stone(1, n - 1)
    else:
        len_stone = len(str(stone))
        if len_stone % 2 == 0 and stone != 0:
            first = str(stone)[:len_stone // 2]
            second = str(stone)[len_stone // 2:]
            first_int = int(first)
            second_int = int(second)

            if set(first) == {'0'}:
                total_arrangements += blink_stone(0, n - 1)
            else:
                total_arrangements += blink_stone(first_int, n - 1)

            if set(second) == {'0'}:
                total_arrangements += blink_stone(0, n - 1)
            else:
                total_arrangements += blink_stone(second_int, n - 1)
        else:
            total_arrangements += blink_stone(stone * 2024, n - 1)
    return total_arrangements


def count_stones_when_blinking(file_name, blink_times):
    counter = 0
    for stone in read_lines(file_name):
        counter += blink_stone(stone, blink_times)
    return counter

print("First part: ", count_stones_when_blinking(l, 25))
print("Second part: ", count_stones_when_blinking(l, 75))


# print("blink n", blink_n_times(tuple(small_input), 6))
# print("blink n", blink_n_times(tuple([17]), 6))
# print("blink n", blink_n_times(tuple(large_input), 25))


# 1
# def count_stones(first_arrangement, n):
#     return blink_n_times(first_arrangement, n)

# for stone in large_input:
#     print("First part: ", blink_n_times(stone, 6))

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