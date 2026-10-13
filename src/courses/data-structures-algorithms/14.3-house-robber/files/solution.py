def rob(houses):
    prev, curr = 0, 0
    for h in houses:
        prev, curr = curr, max(curr, prev + h)
    return curr
