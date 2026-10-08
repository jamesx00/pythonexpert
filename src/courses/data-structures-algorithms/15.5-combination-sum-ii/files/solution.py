def combination_sum2(candidates, target):
    candidates = sorted(candidates)
    result = []

    def backtrack(start, remaining, path):
        if remaining == 0:
            result.append(list(path))
            return
        if remaining < 0:
            return
        for i in range(start, len(candidates)):
            if i > start and candidates[i] == candidates[i - 1]:
                continue
            path.append(candidates[i])
            backtrack(i + 1, remaining - candidates[i], path)
            path.pop()

    backtrack(0, target, [])
    return result
