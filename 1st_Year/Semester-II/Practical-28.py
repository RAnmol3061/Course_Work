with open("lorem_ipsum.txt") as src:
    hist = {}
    cont = src.read()
    words = cont.split()

    for word in words:
        hist[word] = hist.get(word, 0) + 1

print(hist)
