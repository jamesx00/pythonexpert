import heapq

def k_smallest(nums, k):
    heap = list(nums)
    heapq.heapify(heap)
    return [heapq.heappop(heap) for _ in range(k)]
