class DynamicArray:
    def __init__(self):
        self._capacity = 1
        self._size = 0
        self._data = [None] * self._capacity

    def __len__(self):
        return self._size

    def capacity(self):
        return self._capacity

    def get(self, index):
        if index < 0 or index >= self._size:
            raise IndexError("index out of range")
        return self._data[index]

    def append(self, value):
        if self._size == self._capacity:
            self._resize(2 * self._capacity)
        self._data[self._size] = value
        self._size += 1

    def insert_front(self, value):
        if self._size == self._capacity:
            self._resize(2 * self._capacity)
        for i in range(self._size, 0, -1):
            self._data[i] = self._data[i - 1]
        self._data[0] = value
        self._size += 1

    def _resize(self, new_capacity):
        new_data = [None] * new_capacity
        for i in range(self._size):
            new_data[i] = self._data[i]
        self._data = new_data
        self._capacity = new_capacity
