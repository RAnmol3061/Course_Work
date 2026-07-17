exp_list = [1, 15, 20, 23, 24, 25]  # It must be sorted for binary search to work


def lin_search(sequence: list[int], key: int) -> int:
    for i in range(len(sequence)):
        if sequence[i] == key:
            return 1
    return -1


def bin_search(sequence: list[int], key: int) -> int:
    low = 0
    high = len(sequence) - 1

    while low <= high:
        mid = (low + high) // 2

        if sequence[mid] == key:
            return 1
        elif sequence[mid] > key:
            high = mid - 1
        else:
            low = mid + 1
    return -1


print(lin_search(exp_list, 23))
print(lin_search(exp_list, 7))
print(bin_search(exp_list, 25))
print(bin_search(exp_list, 100))
