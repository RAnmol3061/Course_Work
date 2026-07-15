exp_list = [10, 23, 45, 15]


def find_max_min(sequence: list[int]) -> tuple:
    max = sequence[0]  # Assume first element is max
    min = sequence[0]  # Assume first element is min

    for i in range(len(sequence)):
        if max < sequence[i]:
            max = sequence[i]
        if min > sequence[i]:
            min = sequence[i]

    return max, min


max, min = find_max_min(exp_list)
print(f"Maximum Element = {max}, Minimum Element = {min}")
