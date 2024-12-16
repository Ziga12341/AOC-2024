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


# 125
@lru_cache(maxsize=None)
def blink_stone(stone: int):
    set_after_blink = set()
    if stone == 0:
        set_after_blink.add(1)
    else:
        len_stone = len(str(stone))
        if len_stone % 2 == 0 and stone != 0:
            first = str(stone)[:len_stone // 2]
            second = str(stone)[len_stone // 2:]
            first_int = int(first)
            second_int = int(second)
            if set(first) == {0}:
                set_after_blink.add(0)
            else:
                set_after_blink.add(first_int)
            if set(second) == {0}:
                set_after_blink.add(0)
            else:
                set_after_blink.add(second_int)
        else:
            set_after_blink.add(stone * 2024)

    return set_after_blink


# 512072, 1, 20, 24, 28676032
def blink(list_of_arrangement):
    set_after_blink = set()
    for stone in list_of_arrangement:
        if stone == 0:
            set_after_blink.add(1)
        else:
            len_stone = len(str(stone))
            if len_stone % 2 == 0 and stone != 0:
                first = str(stone)[:len_stone // 2]
                second = str(stone)[len_stone // 2:]
                first_int = int(first)
                second_int = int(second)
                if set(first) == {0}:
                    set_after_blink.add(0)
                else:
                    set_after_blink.add(first_int)
                if set(second) == {0}:
                    set_after_blink.add(0)
                else:
                    set_after_blink.add(second_int)
            else:
                set_after_blink.add(stone * 2024)

    return set_after_blink


print(blink([125]))


# i may need to remember on which step i (result of blink) split something and and save only small list... than on the last tstep iterarte only
# i may have dict with each blink for each iteration of blink in one n ... blink one stone input result and in which n it happend
# remember in which number of blik did you get some result... save in dict or save number in set
def next_blink(list_of_stones):
    next_blink_list = []
    arrangement = [blink_stone(stone) for stone in list_of_stones]
    for new_stone in arrangement:
        next_blink_list.extend(new_stone)
    return next_blink_list


def next_blink_set(set_of_stones):
    next_blink_set_stones= set()
    arrangement = {blink_stone(stone) for stone in set_of_stones}
    for new_stone in arrangement:
        next_blink_set_stones.add(new_stone)
    return next_blink_set_stones

# print(next_blink_set({125, 17}))
def blink_n_times(first_arrangement, n):
    next_arrangement = first_arrangement
    if n == 0:
        return next_arrangement
    else:
        next_arrangement = (blink_n_times(next_blink(next_arrangement), n - 1))
        return next_arrangement


@lru_cache(maxsize=None)
def blink_stone_n_times(first_number, n):
    first_set = first_number
    dict_of_stones_in_set_by_n = defaultdict(set)
    dict_of_stones_in_set_by_n[n].add(first_set)
    for i in range(len(dict_of_stones_in_set_by_n[n])):
        first_blink = blink_stone(dict_of_stones_in_set_by_n[n][i])
        if n == 0:
            return dict_of_stones_in_set_by_n[n]
        else:
            for blink in first_blink:
                dict_of_stones_in_set_by_n[n].add(blink_stone_n_times(blink, n - 1))
            return dict_of_stones_in_set_by_n[n]

print(blink_stone_n_times(17,6))

# ------------ #
@lru_cache(maxsize=None)
def blink_sets_stones(first_frozenset, n):
    # Convert the frozenset back to a mutable set for internal use
    first_set = first_frozenset
    dict_of_stones_in_set_by_n = defaultdict(set)
    dict_of_stones_in_set_by_n[n] = first_set
    if n == 0:
        return dict_of_stones_in_set_by_n
    else:
        for stone in list(dict_of_stones_in_set_by_n[n]):
            dict_of_stones_in_set_by_n[n].add(blink_sets_stones(blink_stone(stone), n-1))
        return dict_of_stones_in_set_by_n

# Use frozenset when calling the function
# print(blink_sets_stones(first_frozenset=frozenset({125, 17}), n=6))

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
        self.assertEqual(blink(small_input), {253000, 1, 7})
        self.assertEqual(blink([253, 0, 2024, 14168]), {512072, 1, 20, 24, 28676032})
        self.assertEqual(blink([512072, 1, 20, 24, 28676032]), {512, 72, 2024, 2, 0, 2, 4, 2867, 6032})

    def test_count_stones(self):
        self.assertEqual(next_blink(read_lines(self.s)), [253000, 1, 7])

    def test_blink_n_times(self):
        self.assertEqual(count_stones(self.small_input, 6), 22)
        self.assertEqual(count_stones(self.small_input, 25), 55312)