---
lesson_name: Intervals Basics
code_editor: False
code_execution: False
adding_file_allowed: False
section: Intervals
---

## Why This Pattern Matters &#x1F4A1;

Interval problems give you ranges like `[start, end]` (meetings, bookings, segments). Nearly all of them start the same way: **sort by start**, then sweep from left to right while comparing each interval with the previous one.

## Spotting It &#x1F50D;

- Input looks like `[[1, 3], [2, 6], [8, 10]]`.
- "Merge overlapping", "insert", "remove the fewest to avoid overlap", "how many rooms".

## The One Check to Memorise &#x1F9E0;

Two intervals `[a_start, a_end]` and `[b_start, b_end]` overlap when:

```python
a_start <= b_end and b_start <= a_end
```

After sorting by start, you only need to compare the current start with the previous end: `curr_start <= prev_end`.

## Core Building Blocks &#x1F9F1;

### Merge

```python
def merge(intervals):
    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0]]
    for start, end in intervals[1:]:
        if start <= merged[-1][1]:                 # overlaps the last one
            merged[-1][1] = max(merged[-1][1], end)
        else:
            merged.append([start, end])
    return merged
```

Use `max` because the earlier interval might fully contain the new one.

### Count simultaneous intervals (meeting rooms)

Split each interval into a start event and an end event, sort each list, and sweep:

```python
def min_rooms(intervals):
    starts = sorted(s for s, _ in intervals)
    ends = sorted(e for _, e in intervals)
    rooms = best = e = 0
    for s in starts:
        while e < len(ends) and ends[e] <= s:
            rooms -= 1
            e += 1
        rooms += 1
        best = max(best, rooms)
    return best
```

A min-heap of end times works too.

## Tips & Gotchas &#x1F4CC;

- **Clarify whether touching counts** as overlapping. Do `[1, 2]` and `[2, 3]` overlap? It changes `<=` vs `<`.
- **Sort by end time** for "keep the most non-overlapping intervals". The interval that finishes first leaves the most room for the rest.
- **Insert Interval** in three phases: add everything ending before the new one, merge everything that overlaps it, then add the rest.
- **Don't mutate the input** if the caller might reuse it. Copy before sorting when in doubt.
- **Queries over intervals** (*Minimum Interval to Include Each Query*): sort both the intervals and the queries, then use a heap of active intervals.
