import unittest

s = "small_input.txt"
l = "input.txt"


def read_lines(file: str) -> list:
    with open(file, "r", encoding="utf-8") as file:
        return [int(line.strip()) for line in file]


small_input: list[str] = read_lines(s)
large_input: list[str] = read_lines(l)


def prune(secret_number: int) -> int:
    return secret_number % 16777216


def mix(initial_secret_number: int, result: int) -> int:
    return initial_secret_number ^ result


def first_step(secret_number: int) -> int:
    result = secret_number * 64
    mixing = mix(secret_number, result)
    return prune(mixing)


def second_step(secret_number: int) -> int:
    result = secret_number // 32
    mixing = mix(secret_number, result)
    return prune(mixing)


def third_step(secret_number: int) -> int:
    result = secret_number * 2048
    mixing = mix(secret_number, result)
    return prune(mixing)


def get_next_secret_number(secret_number: int) -> int:
    result_of_first_step = first_step(secret_number)
    result_of_second_step = second_step(result_of_first_step)
    return third_step(result_of_second_step)


def loop_next_numbers_n_times(initial_number: int, n: int):
    current_loop = 1
    while current_loop <= n:
        initial_number = get_next_secret_number(initial_number)
        current_loop += 1
    return initial_number


def sum_2000th_secret_number(file_name: str) -> int:
    counter = 0
    for number in read_lines(file_name):
        counter += loop_next_numbers_n_times(number, 2000)
    return counter


from collections import defaultdict


def get_changes_in_prices(file_name: str):
    main_dict = defaultdict(list)
    for initial_number in read_lines(file_name):
        tuple_changes_by_4 = defaultdict(int)
        current_loop = 1
        previous_value = int(str(initial_number)[-1])
        four_changes_with_price = []
        while current_loop <= 2000:
            if len(four_changes_with_price) == 4:
                if not tuple_changes_by_4[tuple(four_changes_with_price)] or tuple_changes_by_4[
                    tuple(four_changes_with_price)] < previous_value:
                    tuple_changes_by_4[tuple(four_changes_with_price)] = previous_value
                four_changes_with_price = four_changes_with_price[1:]
            else:
                initial_number = get_next_secret_number(initial_number)
                initial_last_number = int(str(initial_number)[-1])
                change_in_price = initial_last_number - previous_value
                four_changes_with_price.append(change_in_price)
                previous_value = initial_last_number
                current_loop += 1
        for tuple_with_four_changes_with_price, current_value in tuple_changes_by_4.items():
            main_dict[tuple_with_four_changes_with_price].append(current_value)
    # Compute sums and store them in a dictionary
    sum_dict = {}
    for key in main_dict:
        total = 0
        for num in main_dict[key]:
            total += num
        sum_dict[key] = total

    # Sort the sum_dict by values in descending order
    sorted_by_sum_desc = {}
    for key in sorted(sum_dict, key=sum_dict.get, reverse=True):
        sorted_by_sum_desc[key] = sum_dict[key]

    return sorted_by_sum_desc


# print("Part one: ", sum_2000th_secret_number(l))
# print("Part two: ",get_changes_in_prices("small_input_part_2.txt"))
# print("Part two: ",get_changes_in_prices(l))
# part two 2431 too high
# part two 2259 too low
# 2430 too high


# check for this one! = (2, -1, -1, 2)
def get_particular(sequence, file_name):
    main_list = []
    for initial_number in read_lines(file_name):
        tuple_changes_by_4 = []
        current_loop = 1
        previous_value = int(str(initial_number)[-1])
        four_changes_with_price = []
        while current_loop <= 2000:
            initial_number = get_next_secret_number(initial_number)
            initial_last_number = int(str(initial_number)[-1])
            change_in_price = initial_last_number - previous_value
            four_changes_with_price.append(change_in_price)
            if len(four_changes_with_price) > 4:
                four_changes_with_price.pop(0)  # Remove the oldest change
            if len(four_changes_with_price) == 4 and tuple(four_changes_with_price) == sequence:
                tuple_changes_by_4.append(previous_value)
            previous_value = initial_last_number
            current_loop += 1
        if tuple_changes_by_4:
            main_list.append(max(tuple_changes_by_4))
    return sum(main_list)


# print(get_particular((2, -1, -1, 2), l))  # the annswer for this one: 1610


# print(get_changes_in_prices("small_input_part_2.txt")) # correct: first is (-2, 1, -1, 3): [7, 7, 9]

# i can try to loop over all sequences

def generate_all_sequences():
    sequences = set()
    for a in range(-9, 10):
        for b in range(-9, 10):
            for c in range(-9, 10):
                for d in range(-9, 10):
                    sequences.add((a, b, c, d))
    return sequences

def collect_all(file_name):
    all_of_sequences = []
    for sequence in generate_all_sequences():
        all_of_sequences.append((get_particular(sequence, file_name), sequence))

    return sorted(all_of_sequences)

print(collect_all("small_input_part_2.txt"))
# print(collect_all(l))
class TestFunctions(unittest.TestCase):
    def setUp(self):
        self.small_input: list[str] = read_lines(s)
        self.s = "small_input.txt"
        self.l = "input.txt"

    def test_sum_2000(self):
        self.assertEqual(sum_2000th_secret_number(self.s), 37327623)
        self.assertEqual(sum_2000th_secret_number(self.l), 19877757850)