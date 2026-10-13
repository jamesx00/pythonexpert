def total(nums):
    result = 0
    for x in nums:
        result += x
    return result


def has_duplicate(nums):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] == nums[j]:
                return True
    return False


def min_and_max(nums):
    smallest = nums[0]
    for x in nums:
        smallest = min(smallest, x)
    largest = nums[0]
    for x in nums:
        largest = max(largest, x)
    return smallest, largest


def count_common(a, b):
    count = 0
    for x in a:
        for y in b:
            if x == y:
                count += 1
    return count


def first_ten_sum(nums):
    result = 0
    for i in range(min(10, len(nums))):
        result += nums[i]
    return result


def count_zero_triples(nums):
    count = 0
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            for k in range(j + 1, len(nums)):
                if nums[i] + nums[j] + nums[k] == 0:
                    count += 1
    return count


def total_complexity():
    return "O(?)"


def has_duplicate_complexity():
    return "O(?)"


def min_and_max_complexity():
    return "O(?)"


def count_common_complexity():
    return "O(?)"


def first_ten_sum_complexity():
    return "O(?)"


def count_zero_triples_complexity():
    return "O(?)"
