import heapq


def k_closest(points, k):
    heap = []  # max-heap of the k closest so far: (-distance, x, y)
    for x, y in points:
        heapq.heappush(heap, (-(x * x + y * y), x, y))
        if len(heap) > k:
            heapq.heappop(heap)  # drop the farthest
    return [[x, y] for _, x, y in heap]
