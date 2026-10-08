import string
from collections import deque

def ladder_length(start_word, end_word, word_list):
    words = set(word_list)
    if end_word not in words:
        return 0
    if start_word == end_word:
        return 1

    q = deque([(start_word, 1)])
    visited = {start_word}
    while q:
        word, length = q.popleft()
        if word == end_word:
            return length
        for i in range(len(word)):
            for ch in string.ascii_lowercase:
                candidate = word[:i] + ch + word[i + 1:]
                if candidate in words and candidate not in visited:
                    visited.add(candidate)
                    q.append((candidate, length + 1))
    return 0
