import sys


def count_words() -> dict[str, int]:
    arguments = sys.argv
    if len(arguments) > 1:
        hist = {}
        with open(arguments[1]) as src:
            cont = src.read()
            words = cont.split()
            for word in words:
                hist[word] = hist.get(word, 0) + 1

        return hist
    else:
        print("Please enter filename as argument")
        return {}  # type:ignore


print(f"Frequncy: {count_words()}")
