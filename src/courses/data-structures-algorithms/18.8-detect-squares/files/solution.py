from collections import defaultdict


class DetectSquares:
    def __init__(self):
        self.counts = defaultdict(int)
        self.points = defaultdict(set)

    def add(self, point):
        x, y = point
        self.counts[(x, y)] += 1
        self.points[x].add(y)

    def count(self, point):
        x, y = point
        total = 0
        for y2 in list(self.points[x]):
            if y2 == y:
                continue
            d = y2 - y
            for x2 in (x + d, x - d):
                total += self.counts[(x, y2)] * self.counts[(x2, y)] * self.counts[(x2, y2)]
        return total
