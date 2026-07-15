# Find the lenght of a list
exp_list = [10, 20, 30]

# Using Built-In len()
print(
    len(exp_list)
)  # Time Complexity: O(1), Reason: There is a size variable in the header of every list in python. Magic of OOPs


# Using User-Defined Fucntion
def get_length(sequence: list[int]) -> int:
    c = 0
    for i in sequence:
        c += 1
    return c  # Time Complexity: O(N)


print(get_length(exp_list))
