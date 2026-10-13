def has_duplicate_list(nums):
    seen = []
    for x in nums:
        if x in seen:
            return True
        seen.append(x)
    return False


def has_duplicate_set(nums):
    seen = set()
    for x in nums:
        if x in seen:
            return True
        seen.add(x)
    return False


def reversed_copy(nums):
    result = []
    for x in nums:
        result.insert(0, x)
    return result


def drain_list(nums):
    queue = list(nums)
    total = 0
    while queue:
        total += queue.pop(0)
    return total


from collections import deque


def drain_deque(nums):
    queue = deque(nums)
    total = 0
    while queue:
        total += queue.popleft()
    return total


def prefix_sums(nums):
    result = []
    for i in range(len(nums)):
        result.append(sum(nums[:i + 1]))
    return result


def has_duplicate_list_complexity():
    return "O(?)"


def has_duplicate_set_complexity():
    return "O(?)"


def reversed_copy_complexity():
    return "O(?)"


def drain_list_complexity():
    return "O(?)"


def drain_deque_complexity():
    return "O(?)"


def prefix_sums_complexity():
    return "O(?)"
