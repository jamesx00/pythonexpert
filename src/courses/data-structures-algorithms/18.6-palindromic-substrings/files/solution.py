def count_palindromic_substrings(s):
    n = len(s)
    count = 0

    def expand(l, r):
        c = 0
        while l >= 0 and r < n and s[l] == s[r]:
            c += 1
            l -= 1
            r += 1
        return c

    for i in range(n):
        count += expand(i, i)
        count += expand(i, i + 1)
    return count
