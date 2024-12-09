import unittest

s = "small_input.txt"
l = "input.txt"


# 2333133121414131402

def get_disk_map(file_path: str) -> str:
    with open(file_path, "r", encoding="utf-8") as file_path:
        return [line.strip() for line in file_path][0]


small_input: str = get_disk_map(s)
large_input: str = get_disk_map(l)
print(small_input)


# 12345 -> "0..111....22222"
def id_assigment(file_path: str) -> str:
    disk_map = get_disk_map(file_path)
    starting_number = 0
    rearranged_string = ""
    for i, number in enumerate(disk_map):
        if i % 2 == 0:
            # hom many ids need to add
            rearranged_string += str(starting_number) * int(number)
            starting_number += 1
        else:
            # free spaces info
            rearranged_string += int(number) * "."

    return rearranged_string


# move one element
# 00...111...2...333.44.5555.6666.777.888899 - > 0099811188827773336446555566..............
def replace_dot_with_last_element(arranged_disk_map: str):
    reversed_digits = [number for number in reversed(arranged_disk_map) if number.isdigit()]
    numbers_in_disk_map = len([number for number in arranged_disk_map if number.isdigit()])
    new_arranged_disk_map = ""
    for i, number in enumerate(arranged_disk_map):
        if i < numbers_in_disk_map:
            if not number.isdigit() and reversed_digits:
                new_arranged_disk_map += reversed_digits.pop(0)
            else:
                new_arranged_disk_map += number
    return new_arranged_disk_map


def filesystem_checksum(file_path):
    sum_number_plus_index = 0
    arranged_disk_map = replace_dot_with_last_element(id_assigment(file_path))
    for i, number in enumerate(arranged_disk_map):
        if number != ".":
            sum_number_plus_index += i * int(number)
    print((i,number))
    return sum_number_plus_index

arranged_disk_map = replace_dot_with_last_element(id_assigment(s))
print("arranged_disk_map: ", arranged_disk_map)
# print("id addigment l: ", id_assigment(l))
# print("large arranged file: ", replace_dot_with_last_element(id_assigment(l)))
# print("First_part: ", filesystem_checksum(l))
# # 91088873473 too low

class TestFunctions(unittest.TestCase):
    def setUp(self):
        self.s = "small_input.txt"
        self.l = "input.txt"
        self.test_input = "test_input.txt"
        self.test_input_2 = "test_input_2.txt"
        self.test_input_3 = "test_input_3.txt"
        self.test_input_4 = "test_input_4.txt"

    def test_id_assigment(self):
        self.assertEqual(id_assigment(self.s), "00...111...2...333.44.5555.6666.777.888899")
        self.assertEqual(id_assigment(self.test_input), "0.11..2")  # 11221
        self.assertEqual(id_assigment(self.test_input_2), "0..111....22222")  # 12345
        self.assertEqual(id_assigment(self.test_input_3), "000000000111111111222222222")  # 90909
        self.assertEqual(id_assigment(self.test_input_4), "." * 18 + "2")  # 09091

    def test_arrange_disk_map(self):
        self.assertEqual(replace_dot_with_last_element(id_assigment(self.s)), "0099811188827773336446555566")
        self.assertEqual(replace_dot_with_last_element(id_assigment(self.s)).index("4"), 19)
        self.assertEqual(replace_dot_with_last_element(id_assigment(self.l)).index("1"), 12)
        self.assertEqual(replace_dot_with_last_element("000000000111111111222222222"), "000000000111111111222222222")

    def test_filesystem_checksum(self):
        self.assertEqual(filesystem_checksum(self.s), 1928)