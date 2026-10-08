class DynamicArray:
    def __init__(self):
        self._capacity = 1
        self._size = 0
        # A fixed-size block of memory: always exactly self._capacity slots.
        # Don't call append or insert on it; build a bigger block instead.
        self._data = [None] * self._capacity

    def __len__(self):
        return self._size

    def capacity(self):
        return self._capacity

    def get(self, index):
        return None

    def append(self, value):
        pass

    def insert_front(self, value):
        pass
