import unittest

s = "small_input.txt"
l = "input.txt"

test = [".####",
        ".####",
        ".####",
        ".#.#.",
        ".#..."]


def rearrange_schematics(schematics):
    columns_to_rows = []
    for i in range(len(schematics)):
        new_column = ""
        for column in schematics:
            new_column += column[i]
        columns_to_rows.append(new_column)
    return columns_to_rows


def count_hashes(schematics):
    return [row.count("#") for row in schematics]


def read_lines(file_name: str) -> list:
    with open(file_name, "r", encoding="utf-8") as file:
        all_schematics = []
        next_schematics = []
        for line in file:
            if line == "\n":
                all_schematics.append(next_schematics)
                next_schematics = []
            else:
                next_schematics.append(line.strip())
        all_schematics.append(next_schematics)

        return all_schematics


def get_pin_heights_for_keys_and_locks(file_name):
    keys = []
    locks = []
    for schematics in read_lines(file_name):
        # in this case we have all hash = lock
        if schematics[0] == "#####":
            locks.append(count_hashes(rearrange_schematics(schematics[1:-1])))
        # for keys
        else:
            keys.append(count_hashes(rearrange_schematics(schematics[1:-1])))

    return keys, locks


def loop_all_locks_with_all_keys(file_name):
    counter = 0
    for keys in get_pin_heights_for_keys_and_locks(file_name)[0]:
        for locks in get_pin_heights_for_keys_and_locks(file_name)[1]:
            if keys != locks:
                # for each index check if sum less or equal 5
                accumulator = []
                for i in range(len(keys)):
                    if keys[i] + locks[i] <= 5:
                        accumulator.append(True)
                    else:
                        accumulator.append(False)
                if all(accumulator):
                    counter += 1
    return counter


print("Part 1 :", loop_all_locks_with_all_keys(l))


class TestFunctions(unittest.TestCase):
    def setUp(self):
        self.small_input: list[str] = read_lines(s)
        self.s = "small_input.txt"
        self.l = "input.txt"

    def test_semple_input(self):
        self.assertEqual(loop_all_locks_with_all_keys(self.s), 3)
        self.assertEqual(loop_all_locks_with_all_keys(self.l), 3320)