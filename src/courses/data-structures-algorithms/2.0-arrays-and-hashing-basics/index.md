---
lesson_name: Arrays & Hashing Basics
code_editor: False
code_execution: False
adding_file_allowed: False
section: Arrays & Hashing
---

## Why This Pattern Matters &#x1F4A1;

Most interview problems start with an array or a string. The naive answer usually compares every pair of elements, which costs `O(n²)`. A hash map (`dict`) or hash set (`set`) lets you answer "have I seen this before?" in `O(1)` on average, which often brings the whole solution down to a single `O(n)` pass.

The core trade-off: **spend extra memory to save time.**

## Spotting It &#x1F50D;

Reach for a hash map or set when the problem asks you to:

- Detect **duplicates** or check **membership** ("does X exist?").
- **Count** how often things appear (anagrams, top-k frequent, majority element).
- Find a **pair** that satisfies a condition (two sum: "have I seen `target - x`?").
- **Group** items that share a key (group anagrams by sorted letters).

## Core Building Blocks &#x1F9F1;

### Seen-set

```python
def has_duplicate(nums):
    seen = set()
    for x in nums:
        if x in seen:
            return True
        seen.add(x)
    return False
```

### Complement lookup (value → index)

```python
def two_sum(nums, target):
    index_of = {}
    for i, x in enumerate(nums):
        if target - x in index_of:
            return [index_of[target - x], i]
        index_of[x] = i  # store AFTER checking, so x can't pair with itself
```

### Counting

```python
from collections import Counter, defaultdict

counts = Counter("banana")        # {'a': 3, 'n': 2, 'b': 1}

freq = {}
for ch in "banana":
    freq[ch] = freq.get(ch, 0) + 1  # the manual version
```

### Grouping by a key

```python
groups = defaultdict(list)
for word in words:
    groups[tuple(sorted(word))].append(word)  # key must be hashable
```

### Prefix sums

Precompute running totals so any range sum is one subtraction:

```python
prefix = [0]
for x in nums:
    prefix.append(prefix[-1] + x)
# sum(nums[i:j]) == prefix[j] - prefix[i]
```

## Tips & Gotchas &#x1F4CC;

- **Dict keys must be hashable.** Lists can't be keys; convert to a `tuple` (or a string) first.
- **A 26-slot count array** (`[0] * 26`, index `ord(c) - ord('a')`) is a fast, hashable-once-tupled signature for lowercase-letter problems.
- **Check before you insert** in complement lookups, or an element may match itself.
- **Sorting is the alternative.** If extra memory isn't allowed, sorting first (`O(n log n)`) often makes duplicates adjacent.
- **Bucket sort trick:** when values are bounded by `n` (e.g., frequencies), an array of buckets indexed by count gives `O(n)` instead of sorting.
- `set(nums)` gives you `O(1)` membership for questions like "is `x - 1` present?" — the key idea behind *Longest Consecutive Sequence*.
- `Counter(a) == Counter(b)` is a one-line anagram check.

## Complexity Cheat Sheet &#x23F1;&#xFE0F;

| Operation | `list` | `set` / `dict` |
| --- | --- | --- |
| `x in ...` | `O(n)` | `O(1)` average |
| append / add | `O(1)` | `O(1)` average |
| index lookup | `O(1)` | `O(1)` by key |

Ready? The next lessons put these building blocks to work.
