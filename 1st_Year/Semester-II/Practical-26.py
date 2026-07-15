original_string = "Hello My Name is Hello"


def reverse_str(strn: str) -> str:
    rev_str = ""
    for char in strn:
        rev_str = char + rev_str
    return rev_str


print(reverse_str(original_string))
