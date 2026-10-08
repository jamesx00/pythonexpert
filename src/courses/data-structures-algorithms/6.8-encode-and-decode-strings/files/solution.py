def encode(words):
    return "".join(f"{len(w)}#{w}" for w in words)


def decode(encoded):
    words = []
    i = 0
    while i < len(encoded):
        j = i
        while encoded[j] != "#":
            j += 1
        length = int(encoded[i:j])
        start = j + 1
        words.append(encoded[start:start + length])
        i = start + length
    return words
