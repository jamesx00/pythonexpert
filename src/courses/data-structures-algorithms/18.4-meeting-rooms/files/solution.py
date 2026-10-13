def can_attend_all_meetings(intervals):
    ordered = sorted(intervals, key=lambda iv: iv[0])
    for i in range(1, len(ordered)):
        if ordered[i][0] < ordered[i - 1][1]:
            return False
    return True
