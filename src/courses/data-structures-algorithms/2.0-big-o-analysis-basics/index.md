---
lesson_name: Big-O Analysis Basics
code_editor: False
code_execution: False
adding_file_allowed: False
section: Big-O Analysis
---

## Why This Matters &#x1F4A1;

Two solutions can both return the right answer and still be wildly different: one finishes instantly on a million elements, the other runs for hours. **Big-O notation** is how we describe that difference without timing anything. It tells you how the work a function does **grows** as its input grows.

Every problem in this course states a target complexity, such as `O(n)` time and `O(1)` space. This section teaches you to work out the complexity of your own code, so you know whether you've hit the target before you press Run.

## The Core Idea &#x1F50D;

Count the basic steps (comparisons, additions, dictionary lookups) as a function of the input size `n`, then keep only the fastest-growing term and drop constant factors:

- `3n + 7` steps → `O(n)`
- `n²/2 + 5n` steps → `O(n²)`
- `20` steps, no matter the input → `O(1)`

Constants are dropped because Big-O describes the *shape* of growth. Doubling `n` doubles an `O(n)` function's work and quadruples an `O(n²)` function's work, whatever the constants are.

## Reading Complexity From Code &#x1F9F1;

### Sequential blocks add, the biggest wins

```python
def f(nums):
    total = sum(nums)      # O(n)
    nums.sort()            # O(n log n)
    return total, nums[0]  # O(1)
# O(n) + O(n log n) + O(1) = O(n log n)
```

### Nested loops multiply

```python
def has_pair_with_sum(nums, target):
    for i in range(len(nums)):              # n times
        for j in range(i + 1, len(nums)):   # up to n times each
            if nums[i] + nums[j] == target:
                return True
    return False
# O(n²)
```

### Halving the input each step gives a log

```python
def count_halvings(n):
    steps = 0
    while n > 1:
        n //= 2
        steps += 1
    return steps
# O(log n): n can only be halved about log₂(n) times
```

### Hidden loops count too

Many one-liners are loops in disguise. Know their cost:

| Operation | Cost |
| --- | --- |
| `x in some_list` | `O(n)` |
| `x in some_set` / `x in some_dict` | `O(1)` average |
| `some_list.append(x)` | `O(1)` amortized |
| `some_list.insert(0, x)` / `some_list.pop(0)` | `O(n)` |
| `some_list[a:b]` (slice) | `O(b - a)` |
| `sorted(xs)` / `xs.sort()` | `O(n log n)` |
| `s1 + s2` (strings) | `O(len(s1) + len(s2))` |

A loop that does `x in some_list` on every iteration is `O(n²)`, even though it looks like a single loop.

## Amortized Cost &#x2696;&#xFE0F;

A Python `list` stores its items in a fixed-size block of memory. When the block is full, `append` allocates a bigger block (roughly 1.125× to 2× the size) and copies every item across. That copy is `O(n)`.

So why is `append` called `O(1)`? Because the copies get rarer as the list grows. If the capacity doubles each time, then appending `n` items triggers copies of size 1, 2, 4, …, up to `n`. Those add up to less than `2n`, so the total work for `n` appends is `O(n)`, which is `O(1)` **per append on average**. That's what *amortized* means: an occasional expensive step, paid for by many cheap ones.

You'll build a resizing array yourself in the *Build-It-Yourself Data Structures* section.

## Space Complexity &#x1F4BE;

Space complexity counts the **extra** memory your function uses beyond its input:

- A few variables → `O(1)`
- A `set` or `dict` that can hold every element → `O(n)`
- A recursive function that goes `d` calls deep → `O(d)` for the call stack

## Common Complexities, Fastest to Slowest &#x23F1;&#xFE0F;

| Big-O | Name | Example | Rough limit for ~1 second |
| --- | --- | --- | --- |
| `O(1)` | constant | dict lookup | any `n` |
| `O(log n)` | logarithmic | binary search | any `n` |
| `O(n)` | linear | one pass over a list | ~10⁷ |
| `O(n log n)` | linearithmic | sorting | ~10⁶ |
| `O(n²)` | quadratic | all pairs | ~3,000 |
| `O(2ⁿ)` | exponential | all subsets | ~20 |
| `O(n!)` | factorial | all orderings | ~10 |

The last column is a rule of thumb for Python: if a problem allows `n = 100,000`, an `O(n²)` solution is too slow and you need `O(n log n)` or better.

## Tips & Gotchas &#x1F4CC;

- **Name your variables.** If a function takes a list of `n` words of length up to `k`, sorting each word is `O(n · k log k)`, not `O(n log n)`.
- **Best, average and worst case can differ.** Dict lookups are `O(1)` on average but `O(n)` in the worst case. Quicksort is `O(n log n)` on average but `O(n²)` in the worst case. When people say "the complexity" they usually mean the worst case, unless they say "average" or "amortized".
- **Don't forget the call stack** when working out the space used by recursive code.
