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
        return connected_computers, reversed_connected_computers


small_input: tuple[defaultdict[Any, list], defaultdict[Any, list]] = create_connected_dicts(s)


# large_input: tuple[defaultdict[Any, list], defaultdict[Any, list]] = create_connected_dicts(l)


def sets_of_networks(file_name):
    networks_by_3_comp = set()
    connected_computers, reversed_connected_computers = create_connected_dicts(file_name)
    for first, second in list_of_connected_computers(file_name):
        third_computer_in_network = (set(connected_computers[first] + reversed_connected_computers[first]) & set(
            connected_computers[second] + reversed_connected_computers[second])) | (set(
            connected_computers[second] + reversed_connected_computers[second]) & set(
            connected_computers[first] + reversed_connected_computers[first]))
        if third_computer_in_network:
            for i in range(len(third_computer_in_network)):
                third = third_computer_in_network.pop()
                network = tuple(sorted([first, second, third]))
                networks_by_3_comp.add(network)
    return networks_by_3_comp


print(sets_of_networks(s))


class TestFunctions(unittest.TestCase):
    def setUp(self):
        self.s = "small_input.txt"

    def test_creating_networks(self):
        self.assertEqual(len(sets_of_networks(self.s)), 12)
        self.assertEqual(sets_of_networks(self.s),
                         {('td', 'wh', 'yn'), ('tb', 'vc', 'wq'), ('aq', 'vc', 'wq'), ('kh', 'qp', 'ub'),
                          ('aq', 'cg', 'yn'), ('tc', 'td', 'wh'), ('co', 'ka', 'ta'), ('co', 'de', 'ka'),
                          ('qp', 'td', 'wh'), ('de', 'ka', 'ta'), ('co', 'de', 'ta'), ('ub', 'vc', 'wq')}
                         )