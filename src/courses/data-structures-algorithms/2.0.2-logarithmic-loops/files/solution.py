def count_digits(n):
    digits = 1
    while n >= 10:
        n //= 10
        digits += 1
    return digits


def largest_power_of_two(n):
    power = 1
    while power * 2 <= n:
        power *= 2
    return power


def halvings_per_index(n):
    total = 0
    for i in range(n):
        j = n
        while j > 1:
            j //= 2
            total += 1
    return total


def count_distinct(nums):
    nums = sorted(nums)
    count = 0
    for i in range(len(nums)):
        if i == 0 or nums[i] != nums[i - 1]:
            count += 1
    return count


def search_all(nums, queries):
    # nums is sorted
    found = 0
    for q in queries:
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if nums[mid] == q:
                found += 1
                break
            if nums[mid] < q:
                lo = mid + 1
            else:
                hi = mid - 1
    return found


def halving_work(n):
    steps = 0
    size = n
    while size > 0:
        for _ in range(size):
            steps += 1
        size //= 2
    return steps


def count_digits_complexity():
    return "O(log n)"


def largest_power_of_two_complexity():
    return "O(log n)"


def halvings_per_index_complexity():
    return "O(n log n)"


def count_distinct_complexity():
    return "O(n log n)"


def search_all_complexity():
    return "O(m log n)"


def halving_work_complexity():
    return "O(n)"
