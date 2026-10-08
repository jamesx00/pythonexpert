from collections import Counter


def is_anagram(word_one, word_two):
    if len(word_one) != len(word_two):
        return False
    return Counter(word_one) == Counter(word_two)
