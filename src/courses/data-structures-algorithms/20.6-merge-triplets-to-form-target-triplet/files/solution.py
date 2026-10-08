def merge_triplets(triplets, target):
    best = [0, 0, 0]
    for t in triplets:
        if t[0] <= target[0] and t[1] <= target[1] and t[2] <= target[2]:
            best = [max(best[i], t[i]) for i in range(3)]
    return best == target
