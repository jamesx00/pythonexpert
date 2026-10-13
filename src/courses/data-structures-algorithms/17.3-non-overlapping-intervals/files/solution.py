def erase_overlap_intervals(intervals):
    if not intervals:
        return 0
    ordered = sorted(intervals, key=lambda iv: iv[1])
    removed = 0
    prev_end = ordered[0][1]
    for start, end in ordered[1:]:
        if start < prev_end:
            removed += 1
        else:
            prev_end = end
    return removed
