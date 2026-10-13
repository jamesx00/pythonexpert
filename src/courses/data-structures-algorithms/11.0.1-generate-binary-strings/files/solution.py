def binary_strings(n):
    result = []
    path = []

    def backtrack():
        if len(path) == n:
            result.append("".join(path))
            return
        for ch in "01":
            path.append(ch)
            backtrack()
            path.pop()

    backtrack()
    return result
