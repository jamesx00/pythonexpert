def count_paths(rows, cols, memo=None):
    if memo is None:
        memo = {}
    if rows == 1 or cols == 1:
        return 1
    if (rows, cols) not in memo:
        memo[(rows, cols)] = count_paths(rows - 1, cols, memo) + count_paths(rows, cols - 1, memo)
    return memo[(rows, cols)]
