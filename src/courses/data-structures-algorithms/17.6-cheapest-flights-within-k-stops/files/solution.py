def find_cheapest_price(n, flights, src, dst, k):
    prices = [float("inf")] * n
    prices[src] = 0

    for _ in range(k + 1):
        updated = prices[:]
        for u, v, w in flights:
            if prices[u] != float("inf") and prices[u] + w < updated[v]:
                updated[v] = prices[u] + w
        prices = updated

    return prices[dst] if prices[dst] != float("inf") else -1
