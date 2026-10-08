def is_anagram(word_one, word_two):
    if len(word_one) != len(word_two):
        return False
    return sorted(word_one) == sorted(word_two)
