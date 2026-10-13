class MinHeap:
    def __init__(self):
        self._heap = []

    def __len__(self):
        return len(self._heap)

    def peek(self):
        return self._heap[0]

    def push(self, value):
        self._heap.append(value)
        self._sift_up(len(self._heap) - 1)

    def pop(self):
        heap = self._heap
        if not heap:
            raise IndexError("pop from an empty heap")
        heap[0], heap[-1] = heap[-1], heap[0]
        smallest = heap.pop()
        if heap:
            self._sift_down(0)
        return smallest

    def _sift_up(self, i):
        heap = self._heap
        while i > 0:
            parent = (i - 1) // 2
            if heap[i] >= heap[parent]:
                break
            heap[i], heap[parent] = heap[parent], heap[i]
            i = parent

    def _sift_down(self, i):
        heap = self._heap
        n = len(heap)
        while True:
            left, right = 2 * i + 1, 2 * i + 2
            smallest = i
            if left < n and heap[left] < heap[smallest]:
                smallest = left
            if right < n and heap[right] < heap[smallest]:
                smallest = right
            if smallest == i:
                return
            heap[i], heap[smallest] = heap[smallest], heap[i]
            i = smallest
