---
lesson_name: How to Approach a New Problem
code_editor: False
code_execution: False
adding_file_allowed: False
section: Approaching New Problems
---

## Why This Matters &#x1F4A1;

In every section so far, you knew the pattern before you read the problem: a problem in *Sliding Window* is a sliding-window problem. In an interview, nobody tells you that. You get an unfamiliar problem and a blank editor.

This lesson gives you a fixed routine for that moment. It has six steps, and each step feeds the next:

1. **Restate** the problem in your own words.
2. **Try small examples** by hand.
3. **Write the brute force**, and work out its complexity.
4. **Find the bottleneck**: what work is the brute force repeating?
5. **Pick a pattern** that removes the bottleneck.
6. **List edge cases**, and check your solution against them.

We'll run the whole routine on one problem you haven't seen in this course.

## The Problem &#x1F9E9;

> Given a list of integers `nums` and an integer `k`, return the number of contiguous subarrays whose sum is exactly `k`. `nums` can contain negative numbers and zeros, and can have up to 100,000 elements.

## Step 1: Restate It &#x1F5E3;&#xFE0F;

Say what goes in, what comes out, and what the rules are, without copying the wording:

- **In:** a list of integers (can be negative or zero) and a target `k`.
- **Out:** a count, not the subarrays themselves.
- **Rules:** a subarray is a run of *adjacent* elements, `nums[i:j]` with `i < j`. Two subarrays with the same values at different positions count separately.

Then ask the questions the statement leaves open. Can the list be empty? (Then the answer is `0`.) Can `k` be `0` or negative? (Yes, nothing rules it out.) Writing these down now gives you half of step 6 for free.

Also read the size limit. It tells you the target complexity before you've written any code:

| Largest `n` | Fastest acceptable time |
| --- | --- |
| about 20 | `O(2ⁿ)` or `O(n!)`: try everything (*Backtracking*) |
| about 1,000 | `O(n²)` |
| about 100,000 | `O(n log n)` or `O(n)` |
| 1,000,000,000 or more | `O(log n)` or `O(1)`: *Binary Search* or math |

With 100,000 elements, an `O(n²)` solution does about 5 billion steps, which is far too slow. We need `O(n)` or `O(n log n)`.

## Step 2: Try Small Examples &#x270F;&#xFE0F;

Work a few inputs by hand before you think about code. Pick at least one ordinary case and one awkward case.

- `nums = [1, 2, 3]`, `k = 3`: `[1, 2]` and `[3]`, so the answer is `2`.
- `nums = [1, 1, 1]`, `k = 2`: `[1, 1]` starting at index 0 and `[1, 1]` starting at index 1, so `2`. Same values at different positions both count.
- `nums = [3, 4, -7, 1]`, `k = 1`: `[1]` and the whole list `[3, 4, -7, 1]`, so `2`. A negative number means a long subarray can sum to a small target.

Doing these by hand shows you what the answer *is* before you work on how to compute it. Keep them: they become your first tests.

## Step 3: Write the Brute Force &#x1F528;

Write the most direct solution you can, even if it's slow. It proves you understand the problem, and it's a correct answer to fall back on.

The most direct idea is to check every subarray. Fixing the start `i` and extending the end `j` one step at a time lets you keep a running total instead of calling `sum()` on each slice:

```python
def count_subarrays(nums, k):
    count = 0
    for i in range(len(nums)):
        total = 0
        for j in range(i, len(nums)):
            total += nums[j]
            if total == k:
                count += 1
    return count
```

There are `n²/2` pairs `(i, j)` and each takes `O(1)`, so this is `O(n²)` time and `O(1)` space. It's correct, but step 1 told us it's too slow for 100,000 elements.

(Calling `sum(nums[i:j + 1])` for every pair would be `O(n³)`. Even a brute force is worth a moment's thought about repeated work.)

## Step 4: Find the Bottleneck &#x1F50E;

Ask: **what work am I repeating?** Look at what the inner loop does for one fixed end `j`. It asks, for every earlier start `i`, "does `nums[i..j]` sum to `k`?" That's a search, and every new `j` repeats it from scratch.

Rewrite the question using prefix sums. Let `prefix[j]` be the sum of the first `j` elements. Then:

```text
sum(nums[i:j]) == prefix[j] - prefix[i]
```

So "does some subarray ending here sum to `k`?" becomes "how many earlier prefix sums equal `prefix[j] - k`?" The bottleneck is a *lookup of a value among everything seen so far*, done once per element.

## Step 5: Pick a Pattern &#x1F9ED;

Now match the bottleneck to a pattern you know. Some signals and the patterns they point to:

| Signal in the problem or the bottleneck | Pattern to try |
| --- | --- |
| "Have I seen this value (or its partner) before?" | Hash map or set (*Arrays & Hashing*) |
| Sorted input, or pairs that move towards each other | *Two Pointers* |
| Contiguous run of elements, all values non-negative | *Sliding Window* |
| "Next greater/smaller element", matching brackets | Monotonic stack (*Stack*) |
| Sorted input, or "the smallest value that works" | *Binary Search* |
| "Top k", "k-th largest", repeatedly take the smallest | Heap (*Heap / Priority Queue*) |
| "All combinations / permutations / subsets" | *Backtracking* |
| Grid or network, reachability, fewest steps | BFS / DFS (*Graphs*) |
| "Count the ways", "min/max cost", overlapping subproblems | *Dynamic Programming* |
| Ranges with start and end points | Sort by start (*Intervals*) |

Our bottleneck is the first row: "how many times have I seen the value `prefix - k`?" That's the *Complement lookup* from *Two Sum*, with a count instead of an index. Keep a dictionary from prefix sum to how many times it has appeared:

```python
def count_subarrays(nums, k):
    seen = {0: 1}  # the empty prefix, so subarrays starting at index 0 count
    prefix = 0
    count = 0
    for x in nums:
        prefix += x
        count += seen.get(prefix - k, 0)
        seen[prefix] = seen.get(prefix, 0) + 1
    return count
```

Trace it on `[3, 4, -7, 1]` with `k = 1`:

| `x` | `prefix` | looking for `prefix - k` | found | `count` |
| --- | --- | --- | --- | --- |
| 3 | 3 | 2 | 0 | 0 |
| 4 | 7 | 6 | 0 | 0 |
| -7 | 0 | -1 | 0 | 0 |
| 1 | 1 | 0 | 2 | 2 |

The last step finds the prefix sum `0` twice: once for the empty prefix (giving the whole list) and once after `-7` (giving `[1]`). That matches the answer from step 2.

**Why it's correct:** every subarray `nums[i:j]` corresponds to exactly one pair of prefix sums, `prefix[i]` and `prefix[j]`, with `i < j`. When the loop reaches `j`, `seen` holds every earlier prefix sum with its count, so it adds exactly the number of starts `i` that give a sum of `k`. Looking up before storing makes sure `i < j`.

**Complexity:** one pass with `O(1)` average dictionary operations, so `O(n)` time. The dictionary can hold up to `n + 1` prefix sums, so `O(n)` space.

**Watch out for the wrong pattern.** "Contiguous subarray" makes *Sliding Window* look like a match. But a window only works when growing it can only increase the sum, which needs non-negative values. On `[3, 4, -7, 1]` with `k = 1`, a window that shrinks whenever the sum goes over `k` never sees the whole list, so it finds `0` subarrays instead of `2`. When a pattern seems to fit, check its requirements against the constraints you wrote down in step 1.

## Step 6: List Edge Cases &#x1F9EA;

Go back to the questions from step 1 and add the usual suspects for this kind of input. Run each one through your solution, by hand or in code:

- **Empty list:** `[]` with `k = 0` gives `0`. The loop doesn't run.
- **One element:** `[5]` with `k = 5` gives `1`, found through the `{0: 1}` entry.
- **Negative numbers:** `[1, -1, 1]` with `k = 1` gives `3`: `[1]`, `[1]` and `[1, -1, 1]`.
- **Zeros and `k = 0`:** `[0, 0, 0]` gives `6`, one for every subarray. This is why `seen` stores counts, not `True`: each prefix sum `0` pairs with every earlier one.
- **Large input:** 100,000 elements. The `O(n)` solution handles it, and the brute force doesn't.

The `{0: 1}` starting entry is the kind of detail edge cases catch. Without it, `[5]` with `k = 5` returns `0`, because the subarray starting at index 0 has no earlier prefix to match.

## Tips & Gotchas &#x1F4CC;

- **Don't skip the brute force.** Even when you can't make it faster, a correct `O(n²)` solution beats an unfinished `O(n)` one, and its inner loop is usually where the bottleneck is.
- **Name the bottleneck as a question.** "For each element, I'm searching for X" points to a hash map. "I'm recomputing this sum" points to a running total or prefix sums. "I'm trying every split again" points to memoization.
- **Check the pattern's requirements.** Sliding window needs a monotonic condition, two pointers on pairs usually need sorted input, binary search needs a sorted or monotonic search space, and greedy needs a reason the local choice is safe.
- **Use the size limit.** It tells you the target complexity, which rules out patterns before you try them.
- **Test the examples you wrote by hand first.** They're small enough to check without a computer, so they catch mistakes in the idea, not just in the code.

Use this routine on every problem from now on, including ones you revisit from earlier sections: cover the section name, and start from step 1.
