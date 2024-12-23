import unittest
from collections import defaultdict
from typing import Tuple, Any

s = "small_input.txt"
l = "input.txt"


def list_of_connected_computers(file: str) -> list:
    with open(file, "r", encoding="utf-8") as file:
        return [line.strip().split("-") for line in file]


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


def sets_of_networks(file_name):
    networks_by_3_comp = set()
    all_in_network = set()
    connected_computers, reversed_connected_computers = create_connected_dicts(file_name)
    for first, second in list_of_connected_computers(file_name):
        third_computer_in_network = (set(connected_computers[first] + reversed_connected_computers[first]) & set(
            connected_computers[second] + reversed_connected_computers[second]))

        if third_computer_in_network:
            for i in range(len(third_computer_in_network)):
                third = third_computer_in_network.pop()
                network = tuple(sorted([first, second, third]))
                networks_by_3_comp.add(network)
    return networks_by_3_comp


print(sets_of_networks(s))


def one_computer_start_with_t(file_name):
    counter = 0
    for network in sets_of_networks(file_name):
        first, second, third = network
        if first[0] == 't' or second[0] == 't' or third[0] == 't':
            counter += 1
    return counter


print("Part 1:", one_computer_start_with_t(l))


class TestFunctions(unittest.TestCase):
    def setUp(self):
        self.s = "small_input.txt"
        self.l = "input.txt"

    def test_creating_networks(self):
        self.assertEqual(len(sets_of_networks(self.s)), 12)
        self.assertEqual(sets_of_networks(self.s),
                         {('td', 'wh', 'yn'), ('tb', 'vc', 'wq'), ('aq', 'vc', 'wq'), ('kh', 'qp', 'ub'),
                          ('aq', 'cg', 'yn'), ('tc', 'td', 'wh'), ('co', 'ka', 'ta'), ('co', 'de', 'ka'),
                          ('qp', 'td', 'wh'), ('de', 'ka', 'ta'), ('co', 'de', 'ta'), ('ub', 'vc', 'wq')}
                         )

    def test_count_t(self):
        self.assertEqual(one_computer_start_with_t(self.s), 7)
        self.assertEqual(one_computer_start_with_t(self.l), 1368)