def search_max(sequence: list[int]) -> int:
    max = sequence[0]  # Assume first element is maximum
    for i in range(len(sequence)):
        if sequence[i] > max:
            max = sequence[i]
    return max


print(search_max([10, 11, 98, 8, 11, 10, 1, 254, 5]))
