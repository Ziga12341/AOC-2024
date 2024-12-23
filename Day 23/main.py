import unittest
from collections import defaultdict
from typing import Tuple, Any

s = "small_input.txt"
l = "input.txt"


def list_of_connected_computers(file: str) -> list:
    with open(file, "r", encoding="utf-8") as file:
        return [line.strip().split("-") for line in file]


print(list_of_connected_computers(s))


def create_connected_dicts(file: str) -> tuple[defaultdict[Any, list], defaultdict[Any, list]]:
    with open(file, "r", encoding="utf-8") as file:
        connected_computers = defaultdict(list)
        reversed_connected_computers = defaultdict(list)
        for line in file:
            line = line.strip().split("-")
            first, second = line

            connected_computers[first].append(second)
            reversed_connected_computers[second].append(first)
            if second=='de':
                print('||||||||||||||, second ', reversed_connected_computers)
        return connected_computers, reversed_connected_computers


small_input: tuple[defaultdict[Any, list], defaultdict[Any, list]] = create_connected_dicts(s)
# large_input: tuple[defaultdict[Any, list], defaultdict[Any, list]] = create_connected_dicts(l)


def sets_of_networks(file_name):
    networks_by_3_comp = set()
    connected_computers, reversed_connected_computers = create_connected_dicts(file_name)
    for first, second in list_of_connected_computers(file_name):
        third_computer_in_network = (set(connected_computers[first] + reversed_connected_computers[first]) & set(connected_computers[second] + reversed_connected_computers[second])) | (set(connected_computers[second] + reversed_connected_computers[second]) & set(connected_computers[first] + reversed_connected_computers[first]))
        if third_computer_in_network:
            if "ka" in third_computer_in_network:
                print("iiiiiiiiiiiii")
            third = third_computer_in_network.pop()
            if third == 'ka':
                print('kaaaaaa')
            network = tuple(sorted([first, second, third]))
            networks_by_3_comp.add(network)
    return networks_by_3_comp

print(sets_of_networks(s))
print(len(sets_of_networks(s)))

print(small_input)

first_tuple = small_input[0]
second_tuple = small_input[1]
print(first_tuple)
print(second_tuple)
print(first_tuple.keys())

print("de=ka", second_tuple['de'])

f_dict = {
    'kh': ['tc', 'ub', 'ta'],
    'qp': ['kh', 'ub'],
    'de': ['cg', 'co', 'ta'],
    'ka': ['co', 'de'],
    'yn': ['aq', 'cg'],
    'cg': ['tb'],
    'vc': ['aq'],
    'tb': ['ka', 'wq', 'vc'],
    'wh': ['tc', 'td', 'yn', 'qp'],
    'ta': ['co', 'ka'],
    'tc': ['td'],
    'td': ['qp', 'yn'],
    'aq': ['cg'],
    'wq': ['ub', 'aq', 'vc'],
    'ub': ['vc'],
    'co': ['tc']
}
s_dict = {
    'tc': ['kh', 'wh', 'co'],
    'kh': ['qp'],
    'cg': ['de', 'yn', 'aq'],
    'co': ['ka', 'ta', 'de'],
    'aq': ['yn', 'vc', 'wq'],
    'ub': ['qp', 'kh', 'wq'],
    'tb': ['cg'],
    'ka': ['tb', 'ta'],
    'td': ['tc', 'wh'],
    'wq': ['tb'],
    'qp': ['td', 'wh'],
    'vc': ['ub', 'wq', 'tb'],
    'ta': ['de', 'kh'],
    'yn': ['wh', 'td'],
    'de': ['ka']
}

print(f_dict['qp'])
print(f_dict['kh'])
print(f_dict['ub'])
print(f_dict['td'])
print(f_dict['wh'])
print("----")
print(s_dict['qp'])
print(s_dict['kh'])
print(s_dict['ub'])

print('-------------')
print(s_dict['kh'] + f_dict['kh'])
print(s_dict['qp'] + f_dict['qp'])
print("=======")
print(set(s_dict['kh'] + f_dict['kh']) & set(s_dict['qp'] + f_dict['qp']))


class TestFunctions(unittest.TestCase):
    def setUp(self):
        self.small_input: list[str] = create_connected_dicts(s)