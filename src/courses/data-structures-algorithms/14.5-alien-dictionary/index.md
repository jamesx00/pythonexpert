---
lesson_name: Alien Dictionary
code_editor: True
code_execution: True
adding_file_allowed: False
difficulty: hard
target_complexity:
  time: O(C)
  space: O(n)
hints:
  - "Compare two words next to each other in the list. What does the first position where they differ tell you, and what does everything after it tell you?"
  - "From *Spotting It* in *Advanced Graphs Basics*: ordering rules from comparisons mean a graph plus a topological sort. Each pair of neighbouring words gives at most one edge, from the first differing letter of the first word to that of the second. A valid order exists only if the graph has no cycle."
  - "Template: put every letter in `graph` with `indegree` 0. For each `w1, w2` pair, add `w1[i] -> w2[i]` at the first `i` where they differ. If there's none and `len(w1) > len(w2)`, return `\"\"`. Then run Kahn's algorithm: queue the letters with indegree 0, pop, append, decrement neighbours. If the result is shorter than the number of letters, return `\"\"`."
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

### Alien Dictionary

An alien language uses the same alphabet as English, but the letters may be ordered differently. Write a function `alien_order(words)` that takes a list of words which is already sorted according to that unknown alien ordering, and returns one valid ordering of the alphabet's letters (as a string containing each letter that appears in `words` exactly once) that is consistent with how the words were sorted. If no valid ordering exists — the given sequence of words could not have come from any consistent letter ordering — return an empty string `""`.

For example, given `words = ["ac", "ab", "zc", "zb"]`, comparing consecutive words tells us `c` must come before `b`, and `a` must come before `z`, so one valid alien alphabet order is `"acbz"` (any order consistent with those constraints is acceptable), and `alien_order(words)` should return that ordering. If instead the input were `["ab", "aa"]`, no ordering could make `"ab"` sort before `"aa"`, so `alien_order(words)` should return `""`.

---

### Tests

<ul>
<li id="test-1"><code>alien_order(["z", "x"])</code> should return <code>"zx"</code>, the only ordering consistent with <code>z</code> coming before <code>x</code></li>
<li id="test-2"><code>alien_order(["z", "x", "z"])</code> should return <code>""</code>, since the words imply both <code>z</code> before <code>x</code> and <code>x</code> before <code>z</code></li>
<li id="test-3"><code>alien_order(["abc", "ab"])</code> should return <code>""</code>, since a longer word cannot come before its own prefix</li>
<li id="test-4"><code>alien_order(["ac", "ab", "zc", "zb"])</code> should return a valid ordering of <code>{a, b, c, z}</code> that keeps <code>c</code> before <code>b</code> and <code>a</code> before <code>z</code></li>
<li id="test-5"><code>alien_order(["wrt", "wrf", "er", "ett", "rftt"])</code> should return <code>"wertf"</code>, the only ordering consistent with the given word order</li>
<li id="test-6"><code>alien_order(["abc", "abd", "abe"])</code> should return a valid ordering of <code>{a, b, c, d, e}</code> that keeps <code>c</code> before <code>d</code> and <code>d</code> before <code>e</code></li>
<li id="test-7"><code>alien_order(["ba", "bc", "ac", "cab"])</code> should return <code>"bac"</code></li>
<li id="test-8"><code>alien_order(["a", "b", "ca", "cb", "a"])</code> should return <code>""</code>, since <code>c</code> comes both after and before <code>a</code></li>
<li id="test-9">Performance: the 26 letters as one-letter words from <code>"z"</code> down to <code>"a"</code>, within 1 second</li>
</ul>

<details class="border border-red-500 px-4 cursor-pointer">
<summary class="select-none">Solution</summary>

```python
from collections import deque


def alien_order(words):
    letters = set()
    for w in words:
        letters.update(w)

    graph = {c: [] for c in letters}
    indegree = {c: 0 for c in letters}

    for w1, w2 in zip(words, words[1:]):
        min_len = min(len(w1), len(w2))
        found = False
        for i in range(min_len):
            if w1[i] != w2[i]:
                graph[w1[i]].append(w2[i])
                indegree[w2[i]] += 1
                found = True
                break
        if not found and len(w1) > len(w2):
            return ""

    q = deque([c for c in letters if indegree[c] == 0])
    order = []

    while q:
        c = q.popleft()
        order.append(c)
        for nxt in graph[c]:
            indegree[nxt] -= 1
            if indegree[nxt] == 0:
                q.append(nxt)

    if len(order) != len(letters):
        return ""

    return "".join(order)
```

Here `n` is the number of words and `C` the total number of letters in them. The alphabet has at most 26 letters.

**Brute force:** try every ordering of the letters and check whether it sorts the words. With `k` different letters that's `k!` orderings, which never finishes for 26 letters, as in the performance test.

**Bottleneck:** most orderings break a rule you could read straight off the words.

**Optimal idea:** read the rules off directly. In a sorted list, two neighbouring words agree up to their first different letter, and that letter decides the order, so it gives one edge `w1[i] -> w2[i]`. Letters after it say nothing. Then a topological sort (Kahn's algorithm) puts the letters in an order that respects every edge.

**Why it's correct:** a list is sorted exactly when each word is in order with the next one, so the edges from neighbouring pairs are all the rules there are. A topological order respects all of them, so it sorts the words. If there's a cycle, such as `z -> x -> z` in test 2, no order can respect it, and Kahn's algorithm leaves the letters on the cycle unpicked, so `order` comes out short. A longer word before its own prefix, like `"abc"` before `"ab"`, can't be fixed by any order, so it needs its own check.

**Complexity:** `O(C)` time: comparing neighbours reads each letter at most twice, and the graph has at most 26 letters and `n - 1` edges. `O(n)` extra space for the edges, plus the 26 letters.

**Common mistakes:** comparing every pair of letters in the two words instead of stopping at the first difference. Missing the prefix case and returning an order for `["abc", "ab"]`. Leaving out letters that never appear in an edge, such as `a` and `b` in test 6. Counting a repeated edge once in `graph` but twice in `indegree`.

</details>
