import unittest

s = "small_input.txt"
l = "input.txt"


def get_disk_map(file_path: str) -> str:
    with open(file_path, "r", encoding="utf-8") as file_path:
        return [line.strip() for line in file_path][0]


small_input: str = get_disk_map(s)
large_input: str = get_disk_map(l)


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


def filesystem_checksum(file_path):
    sum_number_plus_index = 0
    arranged_disk_map = replace_dot_with_last_element(file_path)
    for i, number in enumerate(arranged_disk_map):
        sum_number_plus_index += i * int(number)
    return sum_number_plus_index


print("First_part: ", filesystem_checksum(l))


# # 91088873473 too low

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

    def test_filesystem_checksum(self):
        self.assertEqual(filesystem_checksum(self.s), 1928)