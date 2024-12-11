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
# print(large_input)

# 12345 -> "0..111....22222"
def id_assigment(file_path: str):
    disk_map = get_disk_map(file_path)
    starting_number = 0
    rearranged_string = ""
    list_of_numbers = []
    for i, number in enumerate(disk_map):
        if i % 2 == 0:
            # hom many ids need to add
            rearranged_string += str(starting_number) * int(number)
            add_how_many_numbers = [starting_number] * int(number)
            list_of_numbers.extend(add_how_many_numbers)
            starting_number += 1
        else:
            # free spaces info
            rearranged_string += int(number) * "."

    return rearranged_string, list_of_numbers



# move one element
# 00...111...2...333.44.5555.6666.777.888899 - > 0099811188827773336446555566..............
def replace_dot_with_last_element(file_path: str):
    arranged_disk_map = id_assigment(file_path)[0]
    reversed_digits = "".join(str(number) for number in reversed(id_assigment(file_path)[1]))
    numbers_in_disk_map = len([number for number in arranged_disk_map if number.isdigit()])
    new_arranged_disk_map = ""
    for i, number in enumerate(arranged_disk_map):
        if i < numbers_in_disk_map:
            if not number.isdigit() and reversed_digits:
                new_arranged_disk_map += reversed_digits[0]
                reversed_digits = reversed_digits[1:]
            else:
                new_arranged_disk_map += number
    return new_arranged_disk_map


def filesystem_checksum(file_path):
    sum_number_plus_index = 0
    arranged_disk_map = replace_dot_with_last_element(file_path)
    for i, number in enumerate(arranged_disk_map):
        if number != ".":
            sum_number_plus_index += i * int(number)
    return sum_number_plus_index

arranged_disk_map = replace_dot_with_last_element(s)
print("arranged_disk_map: ", arranged_disk_map)
# print("id arrangement l: ", id_assigment(l))
# print("large arranged file: ", replace_dot_with_last_element(id_assigment(l)))
# print("First_part: ", filesystem_checksum(l))
print("First_part: ", filesystem_checksum("test_input_jernej_1.txt"))
print("First_part: ", filesystem_checksum("test_input_jernej_1.txt"))
# # 91088873473 too low

class TestFunctions(unittest.TestCase):
    def setUp(self):
        self.s = "small_input.txt"
        self.l = "input.txt"
        self.test_input = "test_input.txt"
        self.test_input_2 = "test_input_2.txt"
        self.test_input_3 = "test_input_3.txt"
        self.test_input_4 = "test_input_4.txt"

        self.test_input_jernej_1 = "test_input_jernej_1.txt"
        self.test_input_jernej_2 = "test_input_jernej_2.txt"
        self.test_input_jernej_3 = "test_input_jernej_3.txt"
        self.test_input_jernej_4 = "test_input_jernej_4.txt"
        self.test_input_jernej_5 = "test_input_jernej_5.txt"

    def test_id_assigment(self):
        self.assertEqual(id_assigment(self.s)[0], "00...111...2...333.44.5555.6666.777.888899")
        self.assertEqual(id_assigment(self.test_input)[0], "0.11..2")  # 11221
        self.assertEqual(id_assigment(self.test_input_2)[0], "0..111....22222")  # 12345
        self.assertEqual(id_assigment(self.test_input_3)[0], "000000000111111111222222222")  # 90909
        self.assertEqual(id_assigment(self.test_input_4)[0], "." * 18 + "2")  # 09091
        # self.assertEqual(id_assigment(self.test_input_jernej_3)[0], "00000....11111112222222.........333333......44.......555555555.......666666........77777777")
        self.assertEqual(id_assigment(self.test_input_jernej_5)[0], "00...111...2...333.44.5555.6666.777.888899.1010.111111.12121212")
        self.assertEqual(id_assigment(self.test_input_jernej_4)[0], "00000....11111112222222.........333333......44.......555555555.......666666........77777777")
        self.assertEqual(id_assigment(self.test_input_jernej_1)[0], "00000....11111112222222.........333333......44.......555555555.......666666........77777777....88......999999999..10101010101010")

    def test_arrange_disk_map(self):
        self.assertEqual(replace_dot_with_last_element(self.s), "0099811188827773336446555566")
        self.assertEqual(replace_dot_with_last_element(self.s).index("4"), 19)
        # self.assertEqual(replace_dot_with_last_element(self.l).index("1"), 12)
        self.assertEqual(replace_dot_with_last_element(self.test_input_jernej_1), "")

    def test_filesystem_checksum(self):
        self.assertEqual(filesystem_checksum(self.s), 1928)
        # self.assertEqual(filesystem_checksum(self.test_input_jernej_2), 1233027)
        # self.assertEqual(filesystem_checksum(self.test_input_jernej_3), 21974)
        self.assertEqual(filesystem_checksum(self.test_input_jernej_4), 5268) # do not fail
        self.assertEqual(filesystem_checksum(self.test_input_jernej_1), 13152) # fail