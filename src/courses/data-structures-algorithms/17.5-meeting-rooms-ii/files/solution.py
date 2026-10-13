def min_meeting_rooms(intervals):
    if not intervals:
        return 0
    starts = sorted(iv[0] for iv in intervals)
    ends = sorted(iv[1] for iv in intervals)
    s_ptr = 0
    e_ptr = 0
    rooms = 0
    max_rooms = 0
    n = len(intervals)
    while s_ptr < n:
        if starts[s_ptr] < ends[e_ptr]:
            rooms += 1
            s_ptr += 1
            max_rooms = max(max_rooms, rooms)
        else:
            rooms -= 1
            e_ptr += 1
    return max_rooms
