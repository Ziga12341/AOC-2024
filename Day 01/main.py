from collections import Counter

s = "small_input.txt"
l = "input.txt"


def read_lines(file: str) -> tuple:
    with (open(file, "r", encoding="utf-8") as file):
        left_ids = []
        right_ids = []
        for line in file:
            left, right = line.strip().split("   ")
            left_ids.append(left)
            right_ids.append(right)
        return left_ids, right_ids


small_input: tuple[str] = read_lines(s)
large_input: tuple[str] = read_lines(l)


def sum_sorted_ids(file: str) -> int:
    sum = 0
    left_ids, right_ids = read_lines(file)
    sorted_left_ids = sorted(left_ids)
    sorted_right_ids = sorted(right_ids)
    for i in range(len(sorted_left_ids)):
        sum += abs(int(sorted_left_ids[i]) - int(sorted_right_ids[i]))
    return sum


print("first part: ", sum_sorted_ids(l))


def similarity_score(file: str) -> int:
    sum = 0
    sorted_left_ids, sorted_right_ids = read_lines(file)
    appears_in_right = (Counter(sorted_right_ids))
    for sorted_left_id in sorted_left_ids:
        sum += int(sorted_left_id) * appears_in_right[sorted_left_id]
    return sum


print('second part: ', similarity_score(l))