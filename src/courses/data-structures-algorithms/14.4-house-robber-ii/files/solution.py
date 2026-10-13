def _rob_line(houses):
    prev, curr = 0, 0
    for h in houses:
        prev, curr = curr, max(curr, prev + h)
    return curr

def rob_circular(houses):
    if len(houses) == 1:
        return houses[0]
    return max(_rob_line(houses[1:]), _rob_line(houses[:-1]))
