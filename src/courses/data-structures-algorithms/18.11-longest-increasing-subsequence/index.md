---
lesson_name: Longest Increasing Subsequence
code_editor: True
code_execution: True
adding_file_allowed: False
difficulty: medium
target_complexity:
  time: O(n log n)
  space: O(n)
hints:
  - "For each length `L`, which increasing subsequence of length `L` is the most useful one to keep for later: the one ending in a large number or a small one?"
  - "The `O(n^2)` DP from *Common 1-D Shapes* in *1-D Dynamic Programming Basics* (`dp[i] = 1 + max(dp[j])` for `j < i` with `nums[j] < nums[i]`) is a good start but too slow here. Instead keep `tails`, where `tails[L - 1]` is the smallest possible last number of an increasing subsequence of length `L`. It stays sorted, so binary search where each number goes."
  - "Template: `tails = []`. For each `n`: `i = bisect.bisect_left(tails, n)`. If `i == len(tails)`, append `n`, otherwise set `tails[i] = n`. Return `len(tails)`."
rich_test_results: true
file_groups:
  - common: false
    files:
      - file_name: main.py
        file_type: python
        id: 1
        is_closable: false
        is_edit_focus: true
        is_editable: true
        is_hidden: false
        is_main: true
        is_test_file: false
        source: main.py
      - file_name: tests.py
        file_type: python
        id: 2
        is_closable: false
        is_edit_focus: false
        is_editable: false
        is_hidden: true
        is_main: false
        is_test_file: true
        source: tests.py
    id: 1
    name: Python
---

### Longest Increasing Subsequence

Write a function `length_of_lis(nums)` that takes a list of integers and returns the length of the longest strictly increasing subsequence, meaning a sequence of elements picked from `nums` in their original relative order (not necessarily adjacent) where each element is strictly greater than the one before it.

For example, given `nums = [0, 3, 1, 6, 2, 2, 7]`, one longest increasing subsequence is `0, 1, 2, 7`, giving a length of `4`.

The performance test has 20,000 numbers, so aim for `O(n log n)` time.

---

### Tests

<ul>
<li id="test-1"><code>length_of_lis([0, 3, 1, 6, 2, 2, 7])</code> should return <code>4</code></li>
<li id="test-2"><code>length_of_lis([7, 7, 7, 7])</code> should return <code>1</code></li>
<li id="test-3"><code>length_of_lis([4, 10, 4, 3, 8, 9])</code> should return <code>3</code></li>
<li id="test-4"><code>length_of_lis([5])</code> should return <code>1</code></li>
<li id="test-5"><code>length_of_lis([1, 2, 3, 4, 5])</code> should return <code>5</code></li>
<li id="test-6"><code>length_of_lis([5, 4, 3, 2, 1])</code> should return <code>1</code></li>
<li id="test-7"><code>length_of_lis([9, 1, 4, 2, 3, 3, 7])</code> should return <code>4</code></li>
<li id="test-8">Performance: 20,000 numbers, within 1 second</li>
</ul>

<details class="border border-red-500 px-4 cursor-pointer">
<summary class="select-none">Solution</summary>

```python
import bisect

def length_of_lis(nums):
    tails = []
    for n in nums:
        i = bisect.bisect_left(tails, n)
        if i == len(tails):
            tails.append(n)
        else:
            tails[i] = n
    return len(tails)
```

**Brute force:** trying every subsequence is `O(2^n)`. The classic DP is better: `dp[i]` is the length of the longest increasing subsequence ending at `i`, found by looking at every earlier `j` with `nums[j] < nums[i]`. That's `O(n^2)`: 200 million steps for 20,000 numbers, too slow here.

**Bottleneck:** for each new number, the `O(n^2)` DP scans all earlier positions. Many of them are useless: of two subsequences with the same length, the one with the smaller last number is always at least as good to extend.

**Optimal idea:** keep `tails`, where `tails[L - 1]` is the smallest last number of any increasing subsequence of length `L` seen so far. For a new number `n`, find the first tail `>= n` with `bisect_left`. If there is none, `n` extends the longest subsequence, so append it. Otherwise `n` makes a better (smaller) ending for that length, so replace it.

**Why it's correct:** `tails` is always strictly increasing: a subsequence of length `L + 1` contains one of length `L` with a smaller last number. The first tail `>= n` sits at length `L`, which means the tail before it, at length `L - 1`, is `< n`, so `n` can extend that subsequence to length `L` with a smaller ending than before. Only the length of `tails` is the answer: `tails` itself is usually not a real subsequence.

**Complexity:** `O(n log n)` time: one binary search per number. `O(n)` space for `tails`.

**Common mistakes:** using `bisect_right`, which lets equal numbers extend each other, so `[7, 7, 7, 7]` gives `4` instead of `1`. Returning `tails` as if it were the subsequence. Only ever appending: replacing a tail with a smaller number is what leaves room for longer subsequences later.

</details>
