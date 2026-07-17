import random

random.seed(100)
exp_list = [random.randint(1, 100) for _ in range(10)]


def loop_sum(sequence: list) -> int:
    sum = 0

    for no in sequence:
        sum += no
    return sum


print(loop_sum(exp_list))
