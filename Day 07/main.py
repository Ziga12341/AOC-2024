import unittest

s = "small_input.txt"
l = "input.txt"


def read_lines(file_path: str) -> list:
    with open(file_path, "r", encoding="utf-8") as file:
        return [line.strip() for line in file]


def parse_operations_to_int(file_path):
    # can change to set:
    equations = []
    for equation in read_lines(file_path):
        test_value, numbers = equation.split(":")
        numbers = [int(number) for number in numbers.split(" ")[1:]]
        equations.append((int(test_value), numbers))

    return equations


###
def all_possible_operators(n, concentration_rule=False):
    if concentration_rule:
        signs = ['+', '*', '||']
    else:
        signs = ['+', '*']
    combinations = [[]]

    for _ in range(n):
        new_combinations = []
        for combination in combinations:
            for sign in signs:
                new_combination = combination + [sign]
                new_combinations.append(new_combination)
        combinations = new_combinations

    return combinations
###


def is_operation_possibly_true(equation: tuple[int, list[int]], enable_concatenation_rule=False):
    test_value, numbers = equation
    operations = all_possible_operators(len(numbers) - 1, concentration_rule=enable_concatenation_rule)
    first_number = numbers[0]
    equation_true = []
    for operation in operations:
        operation_accumulator_number = first_number
        for i in range(len(numbers) - 1):
            number_in_numbers = numbers[i + 1]
            symbol = operation[i - 1]
            if symbol == "+":
                operation_accumulator_number += number_in_numbers
            elif symbol == "*":
                operation_accumulator_number *= number_in_numbers
            elif enable_concatenation_rule and symbol == "||":
                operation_accumulator_number = int(str(operation_accumulator_number) + str(number_in_numbers))
        if operation_accumulator_number == test_value:
            equation_true.append(True)
    return any(equation_true)


def sum_valid_equations(file_path, with_concatenation_rule=False):
    sum_values_form_equation = 0
    for equation in parse_operations_to_int(file_path):
        if is_operation_possibly_true(equation, enable_concatenation_rule=with_concatenation_rule):
            sum_values_form_equation += equation[0]
    return sum_values_form_equation


print("Part one: ", sum_valid_equations(l))
print("Part two: ", sum_valid_equations(l, with_concatenation_rule=True))


class TestFunctions(unittest.TestCase):
    def setUp(self):
        self.small_input: list[str] = read_lines(s)
        self.s = "small_input.txt"
        self.l = "input.txt"

    def test_is_operation_possibly_true(self):
        self.assertTrue(is_operation_possibly_true((190, [10, 19])))
        self.assertTrue(is_operation_possibly_true((292, [11, 6, 16, 20])))
        self.assertTrue(is_operation_possibly_true((3267, [81, 40, 27])))

    def test_is_operation_possibly_false(self):
        self.assertFalse(is_operation_possibly_true((83, [17, 5])))
        self.assertFalse(is_operation_possibly_true((156, [15, 6])))
        self.assertFalse(is_operation_possibly_true((7290, [6, 8, 6, 15])))

    def test_operation_with_concatenation_rule_true(self):
        self.assertTrue(is_operation_possibly_true((7290, [6, 8, 6, 15]), enable_concatenation_rule=True))

    def test_part_one(self):
        self.assertEqual(sum_valid_equations(self.s), 3749)
        self.assertEqual(sum_valid_equations(self.l), 5030892084481)

    def test_part_two(self):
        self.assertEqual(sum_valid_equations(self.s, with_concatenation_rule=True), 11387)
        self.assertEqual(sum_valid_equations(self.l, with_concatenation_rule=True), 91377448644679)