import unittest

s = "small_input.txt"
l = "input.txt"


def get_disk_map(file_path: str) -> str:
    with open(file_path, "r", encoding="utf-8") as file_path:
        return [line.strip() for line in file_path][0]


small_input: str = get_disk_map(s)
large_input: str = get_disk_map(l)
print(small_input[::2])


def get_reversed_number(file_path):
    return [(i, int(element)) for i, element in enumerate(get_disk_map(file_path)[::2])][::-1]


print(get_reversed_number(s))


def id_assigment_2(file_path: str):
    disk_map = get_disk_map(file_path)
    starting_number = 0
    rearranged_int = []
    for i, number in enumerate(disk_map):
        if i % 2 == 0:
            # hom many ids need to add
            rearranged_int.extend([starting_number] * int(number))
            starting_number += 1
        else:
            # free spaces info
            rearranged_int.extend(int(number) * [-1])

    return rearranged_int


print(id_assigment_2("small_input.txt"))


# move one element
# 00...111...2...333.44.5555.6666.777.888899 - > 0099811188827773336446555566..............
def replace_dot_with_last_element(file_path: str):
    arranged_disk_map: list[int] = id_assigment_2(file_path)
    new_arranged_disk_map = []
    right_index = len(arranged_disk_map) - 1
    for i, number in enumerate(arranged_disk_map):
        if i <= right_index:
            if number == -1:
                first_reversed_digit = arranged_disk_map[right_index]
                while first_reversed_digit == -1:
                    right_index -= 1
                    first_reversed_digit = arranged_disk_map[right_index]

                new_arranged_disk_map.append(first_reversed_digit)
                right_index -= 1
            else:
                new_arranged_disk_map.append(number)
    return new_arranged_disk_map


print(replace_dot_with_last_element(s))


def get_dot_index(arranged_disk):
    dot_indexes = []
    segment_of_dots = []
    for i, element in enumerate(arranged_disk):
        if element == -1:
            segment_of_dots.append(i)
        elif segment_of_dots:
            dot_indexes.append(segment_of_dots)
            segment_of_dots = []
    return dot_indexes


print(get_dot_index(
    [0, 0, -1, -1, -1, 1, 1, 1, -1, -1, -1, 2, -1, -1, -1, 3, 3, 3, -1, 4, 4, -1, 5, 5, 5, 5, -1, 6, 6, 6, 6, -1, 7, 7,
     7, -1, 8, 8, 8, 8, 9, 9]
))


def arrange_disk_move_whole_file(file_path):
    # follow_index = float('inf')
    follow_index = 2**1000
    initial_assigment = id_assigment_2(file_path)
    numbers_to_replace = get_reversed_number(file_path)
    while numbers_to_replace:
        get_indexes = get_dot_index(initial_assigment[:follow_index])
        number, times = numbers_to_replace.pop(0)
        for one_group_of_dots in get_indexes:
            if len(one_group_of_dots) >= times:
                follow_index = initial_assigment.index(number)
                index_to_replace_with_number = one_group_of_dots[:times]
                for dot_index in index_to_replace_with_number:
                    initial_assigment[dot_index] = number
                    # l[:3] + [9 if num == 5 else num for num in l[3:]]
                initial_assigment = initial_assigment[:index_to_replace_with_number[-1] + 1] + [-1 if nummber_in_initial_assigment == number else nummber_in_initial_assigment for nummber_in_initial_assigment in initial_assigment[index_to_replace_with_number[-1] + 1:]]
                break

    return initial_assigment
print(arrange_disk_move_whole_file(s))

def filesystem_checksum(file_path):
    sum_number_plus_index = 0
    arranged_disk_map = replace_dot_with_last_element(file_path)
    for i, number in enumerate(arranged_disk_map):
        if number != -1:
            sum_number_plus_index += i * int(number)
    return sum_number_plus_index
def filesystem_checksum_part_2(file_path):
    sum_number_plus_index = 0
    arranged_disk_map = arrange_disk_move_whole_file(file_path)
    for i, number in enumerate(arranged_disk_map):
        if number != -1:
            sum_number_plus_index += i * int(number)
    return sum_number_plus_index


print("First_part: ", filesystem_checksum(l))
print("Second_part: ", filesystem_checksum_part_2(l))
# part 2 6423378639280 too high



class TestFunctions(unittest.TestCase):
    def setUp(self):
        self.s = "small_input.txt"
        self.l = "input.txt"

    def test_id_assigment_2(self):
        self.assertEqual(id_assigment_2(self.s),
                         [0, 0, -1, -1, -1, 1, 1, 1, -1, -1, -1, 2, -1, -1, -1, 3, 3, 3, -1, 4, 4, -1, 5, 5, 5, 5, -1,
                          6, 6, 6, 6, -1, 7, 7, 7, -1, 8, 8, 8, 8, 9, 9])

    def test_arrange_disk_map(self):
        self.assertEqual(replace_dot_with_last_element(self.s),
                         [0, 0, 9, 9, 8, 1, 1, 1, 8, 8, 8, 2, 7, 7, 7, 3, 3, 3, 6, 4, 4, 6, 5, 5, 5, 5, 6, 6])

    def test_arrange_disc_move_whole_files(self):
        self.assertEqual(arrange_disk_move_whole_file(self.s),
                         [0, 0, 9, 9, 2, 1, 1, 1, 7, 7, 7, -1, 4, 4, -1, 3, 3, 3, -1, -1, -1, -1, 5, 5, 5, 5, -1, 6, 6,
                          6, 6, -1, -1, -1, -1, -1, 8, 8, 8, 8, -1, -1])

    def test_filesystem_checksum(self):
        self.assertEqual(filesystem_checksum(self.s), 1928)