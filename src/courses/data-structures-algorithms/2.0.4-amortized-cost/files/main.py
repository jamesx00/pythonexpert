def build_list(n):
    result = []
    for i in range(n):
        result.append(i)
    return result


class DoublingArray:
    def __init__(self):
        self.capacity = 1
        self.size = 0
        self.data = [None]

    def append(self, value):
        if self.size == self.capacity:
            self.capacity *= 2
            new_data = [None] * self.capacity
            for i in range(self.size):
                new_data[i] = self.data[i]
            self.data = new_data
        self.data[self.size] = value
        self.size += 1


def append_one(array, value):
    # The worst-case cost of ONE call, on an array holding n items.
    array.append(value)


def append_amortized(array, value):
    # The AMORTIZED cost of one call, over a long run of appends
    # to the same DoublingArray.
    array.append(value)


class GrowByTenArray:
    def __init__(self):
        self.capacity = 10
        self.size = 0
        self.data = [None] * 10

    def append(self, value):
        if self.size == self.capacity:
            self.capacity += 10
            new_data = [None] * self.capacity
            for i in range(self.size):
                new_data[i] = self.data[i]
            self.data = new_data
        self.data[self.size] = value
        self.size += 1


def fill_grow_by_ten(n):
    array = GrowByTenArray()
    for i in range(n):
        array.append(i)
    return array


def next_greater(nums):
    result = [-1] * len(nums)
    stack = []  # indexes still waiting for a bigger number
    for i in range(len(nums)):
        while stack and nums[stack[-1]] < nums[i]:
            result[stack.pop()] = nums[i]
        stack.append(i)
    return result


def build_list_complexity():
    return "O(?)"


def append_one_complexity():
    return "O(?)"


def append_amortized_complexity():
    return "O(?)"


def fill_grow_by_ten_complexity():
    return "O(?)"


def next_greater_complexity():
    return "O(?)"
