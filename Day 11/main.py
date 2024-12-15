import unittest
from functools import lru_cache

s = "small_input.txt"
l = "input.txt"


def read_lines(file_path: str) -> list[int]:
    with open(file_path, "r", encoding="utf-8") as file_path:
        return [int(stone) for stone in file_path.readline().split(" ")]


small_input: list[int] = read_lines(s)
large_input: list[int] = read_lines(l)


# 125
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


print(blink([125]))


# i may need to remember on which step i (result of blink) split something and and save only small list... than on the last tstep iterarte only

def next_blink(list_of_stones):
    next_blink_list = []
    arrangement = [blink_stone(stone) for stone in list_of_stones]
    for new_stone in arrangement:
        next_blink_list.extend(new_stone)
    return next_blink_list


def blink_n_times(first_arrangement, n):
    next_arrangement = first_arrangement
    if n == 0:
        return next_arrangement
    else:
        next_arrangement = (blink_n_times(next_blink(next_arrangement), n - 1))
        return next_arrangement


@lru_cache(maxsize=None)
def blink_stone_n_times(first_number, n):
    next_arrangement = [first_number]
    for i in range(len(next_arrangement)):
        first_blink = blink_stone(next_arrangement[i])
        if n == 0:
            return next_arrangement
        else:
            for blink in first_blink:
                next_arrangement.append(blink_stone_n_times(blink, n - 1))
            return next_arrangement


# ------------ #

def blink_first_stone_n_times(stone, n):
    next_arrangement = stone
    if n == 0:
        return next_arrangement
    else:
        current_arrangement = []
        for stone in next_arrangement:
            current_arrangement.extend(blink_stone_n_times(blink_stone(stone), n - 1))
        next_arrangement = current_arrangement
        return next_arrangement


def count_stones(first_arrangement, n):
    return len(blink_n_times(first_arrangement, n))


def count_stones_second_part(first_arrangement, n):
    return len(blink_stone_n_times(first_arrangement, n))


# print("blink", blink_stone_n_times(17, 6))


# print("blink first stone", blink_first_stone_n_times([125], 5))

print("First part: ", count_stones(large_input, 25))


# print("Second part: ", count_stones_second_part(large_input, 25))
# print("Second part: ", count_stones_second_part(large_input, 40))


class TestFunctions(unittest.TestCase):
    def setUp(self):
        self.small_input: list[int] = read_lines(s)
        self.s = "small_input.txt"

    def test_blink(self):
        self.assertEqual(blink(small_input), [253000, 1, 7])
        self.assertEqual(blink([253, 0, 2024, 14168]), [512072, 1, 20, 24, 28676032])
        self.assertEqual(blink([512072, 1, 20, 24, 28676032]), [512, 72, 2024, 2, 0, 2, 4, 2867, 6032])

    def test_count_stones(self):
        self.assertEqual(next_blink(read_lines(self.s)), [253000, 1, 7])

    def test_blink_n_times(self):
        self.assertEqual(count_stones(self.small_input, 6), 22)
        self.assertEqual(count_stones(self.small_input, 25), 55312)