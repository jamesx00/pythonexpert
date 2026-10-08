import heapq


def k_closest(points, k):
    heap = [(x ** 2 + y ** 2, x, y) for x, y in points]
    heapq.heapify(heap)
    closest = heapq.nsmallest(k, heap)
    return [[x, y] for d, x, y in closest]
