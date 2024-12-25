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


print(rearrange_schematics(test))


def count_hashes(schematics):
    return [row.count("#") for row in schematics]


print(count_hashes(rearrange_schematics(test)))


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


small_input: list[str] = read_lines(s)
large_input: list[str] = read_lines(l)
print(small_input)


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

print(get_pin_heights_for_keys_and_locks(s))

class TestFunctions(unittest.TestCase):
    def setUp(self):
        self.small_input: list[str] = read_lines(s)