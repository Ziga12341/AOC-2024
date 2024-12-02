import unittest

s = "small_input.txt"
l = "input.txt"


def read_lines(file: str) -> list[list[str]]:
    with open(file, "r", encoding="utf-8") as file:
        return [line.strip().split(' ') for line in file]


small_input: list[list[str]] = read_lines(s)
large_input: list[list[str]] = read_lines(l)


def is_safe_report_decreasing(report: list[int]) -> bool:
    # is report safe increasing
    # The levels are either all increasing or all decreasing.
    # Any two adjacent levels differ by at least one and at most three.
    all_true = []
    for level_in_string in range(1, len(report)):
        level = int(level_in_string)
        current_number = report[level - 1]
        next_number = report[level]
        if (next_number < current_number) and (
                current_number - next_number == 1 or current_number - next_number == 2 or current_number - next_number == 3):
            all_true.append(True)
        else:
            all_true.append(False)
    return all(all_true)


def is_safe_report_decreasing_with_tolerance(report: list[int]) -> bool:
    # each time remove one number from a report. brute force method
    any_true = []
    for i in range(len(report)):
        one_number_less_report = report[:i] + report[i + 1:]
        if is_safe_report_decreasing(one_number_less_report):
            any_true.append(True)
        else:
            any_true.append(False)

    return any(any_true)


def is_safe_report_increasing(report: list[int]) -> bool:
    # is report safe increasing
    # The levels are either all increasing or all decreasing.
    # Any two adjacent levels differ by at least one and at most three.
    all_true = []
    for level_in_string in range(1, len(report)):
        level = int(level_in_string)
        current_number = report[level - 1]
        next_number = report[level]
        if (next_number > current_number) and (
                next_number - current_number == 1 or next_number - current_number == 2 or next_number - current_number == 3):
            all_true.append(True)
        else:
            all_true.append(False)
    return all(all_true)


def is_safe_report_increasing_with_tolerance(report: list[int]) -> bool:
    # each time remove one number from a report. brute force method
    any_true = []
    for i in range(len(report)):
        one_number_less_report = report[:i] + report[i + 1:]
        if is_safe_report_increasing(one_number_less_report):
            any_true.append(True)
        else:
            any_true.append(False)

    return any(any_true)


def is_save_report(report: list[int]) -> bool:
    first_number = report[0]
    last_number = report[-1]
    if first_number > last_number:
        return is_safe_report_decreasing(report)

    elif last_number > first_number:
        return is_safe_report_increasing(report)


def is_save_report_with_tolerance(report: list[int]) -> bool:
    # if values increase in list than implement is safe report increasing

    first_number = report[0]
    last_number = report[-1]
    if first_number > last_number:
        return is_safe_report_decreasing_with_tolerance(report)
    elif last_number > first_number:
        return is_safe_report_increasing_with_tolerance(report)


def sum_safe_reports_with_tolerance(file) -> int:
    sum_safe_report_with_tolerance = 0
    for report in read_lines(file):
        report = [int(level) for level in report]
        # print(report)
        if is_save_report_with_tolerance(report):
            sum_safe_report_with_tolerance += 1

    return sum_safe_report_with_tolerance


def sum_safe_reports(file) -> int:
    sum_safe_report = 0
    for report in read_lines(file):
        report = [int(level) for level in report]
        # print(report)
        if is_save_report(report):
            sum_safe_report += 1

    return sum_safe_report


print("Part one:", sum_safe_reports(l))
print("Part two:", sum_safe_reports_with_tolerance(l))


class TestFunctions(unittest.TestCase):
    def setUp(self):
        self.small_input: list[list[str]] = read_lines(s)

    def test_sum_safe_reports(self):
        self.assertEqual(sum_safe_reports(s), 2)

    def test_is_safe_report_decreasing(self):
        self.assertTrue(is_safe_report_decreasing([7, 6, 4, 2, 1]))
        self.assertFalse(is_safe_report_decreasing([1, 3, 6, 7, 9]))

    def test_is_safe_report_increasing(self):
        self.assertFalse(is_safe_report_increasing([7, 6, 4, 2, 1]))
        self.assertTrue(is_safe_report_increasing([1, 3, 6, 7, 9]))

    def test_if_safe_report(self):
        self.assertTrue(is_save_report([7, 6, 4, 2, 1]))
        self.assertTrue(is_save_report([1, 3, 6, 7, 9]))

    def test_safe_report_with_tolerance(self):
        self.assertEqual(sum_safe_reports_with_tolerance(s), 4)

    def test_safe_report_increasing_with_tolerance(self):
        self.assertTrue(is_safe_report_increasing_with_tolerance([1, 3, 6, 7, 9]))
        self.assertTrue(is_safe_report_increasing_with_tolerance([1, 3, 2, 4, 5]))
        self.assertTrue(is_safe_report_increasing_with_tolerance([1, 2, 5, 5, 7, 8]))
        self.assertTrue(is_safe_report_increasing_with_tolerance([48, 46, 47, 49, 51, 54, 56]))
        self.assertTrue(is_safe_report_increasing_with_tolerance([1, 1, 2, 3, 4, 5]))
        self.assertTrue(is_safe_report_increasing_with_tolerance([5, 1, 2, 3, 4, 5]))
        self.assertTrue(is_safe_report_increasing_with_tolerance([7, 10, 8, 10, 11]))
        self.assertTrue(is_safe_report_increasing_with_tolerance([1, 2, 3, 4, 3]))
        self.assertTrue(is_safe_report_increasing_with_tolerance([7, 10, 8, 10, 11]))
        self.assertTrue(is_safe_report_increasing_with_tolerance([8, 9, 10, 11]))
        self.assertFalse(is_safe_report_increasing_with_tolerance([1, 2, 7, 8, 9]))

    def test_safe_report_decreasing_with_tolerance(self):
        self.assertTrue(is_safe_report_decreasing_with_tolerance([7, 6, 4, 2, 1]))
        self.assertTrue(is_safe_report_decreasing_with_tolerance([8, 6, 4, 4, 1]))
        self.assertTrue(is_safe_report_decreasing_with_tolerance([66, 64, 64, 62, 60]))
        self.assertTrue(is_safe_report_decreasing_with_tolerance([29, 28, 27, 25, 26, 25, 22, 20]))
        self.assertTrue(is_safe_report_decreasing_with_tolerance([9, 8, 7, 6, 7]))
        self.assertTrue(is_safe_report_decreasing_with_tolerance([29, 28, 27, 25, 26, 25, 22, 20]))
        self.assertFalse(is_safe_report_decreasing_with_tolerance([9, 7, 6, 2, 1]))