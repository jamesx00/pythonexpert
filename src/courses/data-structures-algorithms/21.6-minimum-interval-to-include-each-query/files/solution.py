import heapq

def min_interval_for_queries(intervals, queries):
    ordered = sorted(intervals, key=lambda iv: iv[0])
    answer = [-1] * len(queries)
    order = sorted(range(len(queries)), key=lambda i: queries[i])

    heap = []
    idx = 0
    for qi in order:
        q = queries[qi]
        while idx < len(ordered) and ordered[idx][0] <= q:
            start, end = ordered[idx]
            heapq.heappush(heap, (end - start + 1, end))
            idx += 1
        while heap and heap[0][1] < q:
            heapq.heappop(heap)
        if heap:
            answer[qi] = heap[0][0]

    return answer
