---
lesson_name: Rich test results and lesson metadata
code_editor: True
code_execution: True
adding_file_allowed: False
difficulty: easy
target_complexity:
  time: O(n)
  space: O(n)
hints:
  - What would you need to remember about the numbers you've already seen, to know whether the current number completes a pair?
  - For each number `x`, the only partner that works is `target - x`. A `set` answers "have I seen it?" in `O(1)`. Review the *Arrays & Hashing Basics* lesson for the complement-lookup template.
  - "Template: keep a `seen` set. For each `x`, return `True` if `target - x` is in `seen`, otherwise add `x`. Return `False` after the loop."
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

#### Lesson metadata

Exercise lessons can set these optional front matter fields. Lessons without them render exactly as before.

```yaml
difficulty: easy            # easy | medium | hard. Shown in the lesson header and the sidebar.
target_complexity:
  time: O(n)                # required if target_complexity is set
  space: O(n)               # optional
hints:                      # revealed one at a time, placed before the Solution reveal
  - A guiding question, not the answer.
  - The key insight. Point back to the relevant basics lesson or warm-up.
  - The template.
checkpoint: true            # end-of-section problem with no hints; labelled in the header
rich_test_results: true     # the test file reports rich results (see below)
```

- **Hints** are Markdown. Quote a hint that starts with a backtick or contains `: ` so the YAML stays valid. The full solution is the existing Solution reveal, so hints stop at the template. In Mixed Practice problems, the first hint names the pattern.
- **Checkpoint** problems have no `hints` (the content checker enforces this).

#### Solution walkthroughs

Write every walkthrough in this order: brute force and its complexity → the bottleneck ("what work am I repeating?") → the optimal idea → why it's correct → final complexity, briefly justified → common mistakes.

#### Reference solutions

Put the reference solution in `files/solution.<ext>` next to the starter, using the same extension as the lesson's main file (`solution.py`, `solution.sql`). It isn't listed in `file_groups`, so it's never shipped to the browser. Run `npm run check-content` to verify every lesson: the reference must pass every test, the starter must fail at least one, and the test IDs the test file reports must match the `test-N` list items.

#### Rich test results

The test file prints one JSON object mapping test ID → result. A result can be a boolean (the original format) or an object:

```json
{
    "1": {"passed": true},
    "2": {"passed": false, "got": "[0, 1]", "expected": "[1, 2]"},
    "3": {"passed": false, "error": "IndexError: list index out of range", "expected": "3"},
    "4": {"passed": false, "timed_out": true}
}
```

- `got` and `expected` are shown as-is, so send Python reprs (`repr(value)`). Long values are truncated in the feedback.
- `error` is the exception type and message.
- `timed_out` marks a performance test that went over its time budget.

Set `rich_test_results: true` on lessons that use this format. Then, if the execution service kills the whole run, every test the file didn't report is shown as too slow.

Expected values are literal data in the test file, not computed by a reference implementation, so test files contain no solution code. This lesson's `tests.py` has a reusable `check()` helper (open hidden files in the editor settings to see it).

#### Performance tests

A performance test is a normal test ID whose input is generated deterministically (a fixed formula or seed) and run under a time budget enforced inside the test file: `check(..., time_budget=1.0)` interrupts the call with `SIGALRM` once the budget runs out and reports `timed_out`, so the other tests still report their results. Say the input size in the test description. Set the budget well above an efficient solution's runtime and well below a brute-force solution's runtime, measured on the execution service, and record both timings in a comment next to the budget.

---

### Exercise

Write a function `has_pair_with_sum(nums, target)` that returns `True` if two different elements of `nums` add up to `target`, and `False` otherwise.

### Tests

<ul>
<li id="test-1"><code>has_pair_with_sum([1, 4, 6, 2], 8)</code> should return <code>True</code></li>
<li id="test-2"><code>has_pair_with_sum([1, 2, 3], 7)</code> should return <code>False</code></li>
<li id="test-3"><code>has_pair_with_sum([5, 5], 10)</code> should return <code>True</code></li>
<li id="test-4"><code>has_pair_with_sum([5], 10)</code> should return <code>False</code></li>
<li id="test-5"><code>has_pair_with_sum([], 0)</code> should return <code>False</code></li>
<li id="test-6">Performance: 100,000 elements with no matching pair, within 1 second</li>
</ul>

<details class="border border-red-500 px-4 cursor-pointer">
<summary class="select-none">Solution</summary>

```python
def has_pair_with_sum(nums, target):
    seen = set()
    for x in nums:
        if target - x in seen:
            return True
        seen.add(x)
    return False
```

**Brute force:** check every pair with two nested loops, `O(n²)` time.

**Bottleneck:** for each `x`, the inner loop searches the whole list for `target - x`.

**Optimal idea:** remember the numbers seen so far in a set and look up `target - x` in `O(1)`.

**Why it's correct:** any pair `(a, b)` with `a` before `b` is found when the loop reaches `b`, because `a` is already in `seen`. Checking before adding stops an element from pairing with itself.

**Complexity:** `O(n)` time (one pass, `O(1)` set operations), `O(n)` space for the set.

**Common mistakes:** adding `x` to `seen` before checking, which makes `[5]` with target `10` return `True`.

</details>
