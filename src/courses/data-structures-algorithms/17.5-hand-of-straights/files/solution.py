from collections import Counter

def is_n_straight_hand(hand, group_size):
    if len(hand) % group_size != 0:
        return False
    count = Counter(hand)
    for k in sorted(count.keys()):
        needed = count[k]
        if needed == 0:
            continue
        for j in range(k, k + group_size):
            if count[j] < needed:
                return False
            count[j] -= needed
    return True
