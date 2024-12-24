import unittest
from collections import defaultdict
from typing import Tuple, Type, List, Any, Set

s = "small_input.txt"
l = "input.txt"


def read_lines(file: str) -> tuple[defaultdict[Any, int], list[tuple[Any, Any, Any, Any]], set[Any]]:
    with open(file, "r", encoding="utf-8") as file:
        gate_map = defaultdict(int)
        gates_and_wires = []
        all_results = set()
        new_line = False
        for line in file:
            if line == "\n":
                new_line = True
            if not new_line:
                # parse first part
                line = line.strip().split(": ")
                gate_id_unique, value = line
                value = int(value)
                gate_map[gate_id_unique] = value
                all_results.add(gate_id_unique)
            else:
                if line != "\n":
                    # parse the second part with rules
                    line = line.strip().split(" -> ")
                    rest, result = line
                    rest = rest.strip().split(" ")
                    first, operator, second = rest
                    gates_and_wires.append((first, operator, second, result))
                    all_results.add(result)
        return gate_map, gates_and_wires, all_results


small_input = read_lines(s)
large_input = read_lines(l)

print(small_input)


def get_number_for_wire(file_name):
    gate_map, gates_and_wires, all_result = read_lines(file_name)
    while gate_map.keys() != all_result:
        for first, operator, second, result in gates_and_wires:
            if first not in gate_map.keys() or second not in gate_map.keys():
                break
            else:

                if operator == "AND":
                    if gate_map[first] == 1 and gate_map[second] == 1:
                        gate_map[result] = 1
                    else:
                        gate_map[result] = 0

                if operator == "OR":
                    if gate_map[first] == 0 and gate_map[second] == 0:
                        gate_map[result] = 0
                    else:
                        gate_map[result] = 1

                if operator == "XOR":
                    if (gate_map[first] == 0 and gate_map[second] == 0) or (
                            gate_map[first] == 1 and gate_map[second] == 1):
                        gate_map[result] = 0
                    else:
                        gate_map[result] = 1
    return gate_map


def get_number_for_wire(file_name):
    gate_map, gates_and_wires, all_result = read_lines(file_name)
    changed = True
    while changed and gate_map.keys() != all_result:
        changed = False
        for first, operator, second, result in gates_and_wires:
            if result in gate_map:
                continue
            if first not in gate_map or second not in gate_map:
                continue

            changed = True
            if operator == "AND":
                gate_map[result] = 1 if gate_map[first] == 1 and gate_map[second] == 1 else 0
            elif operator == "OR":
                gate_map[result] = 0 if gate_map[first] == 0 and gate_map[second] == 0 else 1
            elif operator == "XOR":
                gate_map[result] = 1 if gate_map[first] != gate_map[second] else 0

    return gate_map
def get_z_values_from_wires(file_name):
    values = []
    # sort_wires = [item for item in reversed(sorted(get_number_for_wire(file_name)))]
    for wire, value in reversed(sorted(get_number_for_wire(file_name).items())):
        if wire[0] == "z":
            values.append(value)

    return values



print(get_number_for_wire(l))
print(get_z_values_from_wires(l))
# Convert binary list to decimal
binary_string = ''.join(map(str, get_z_values_from_wires(l)))
decimal_number = int(binary_string, 2)
print(decimal_number)

class TestFunctions(unittest.TestCase):
    def setUp(self):
        self.small_input: list[str] = read_lines(s)