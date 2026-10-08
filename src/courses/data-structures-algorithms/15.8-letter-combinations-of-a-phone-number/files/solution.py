def letter_combinations(digits):
    if not digits:
        return []
    digit_map = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz",
    }
    result = []

    def backtrack(index, path):
        if index == len(digits):
            result.append("".join(path))
            return
        for letter in digit_map[digits[index]]:
            path.append(letter)
            backtrack(index + 1, path)
            path.pop()

    backtrack(0, [])
    return result
