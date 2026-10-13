---
lesson_name: Valid Anagram
code_editor: True
code_execution: True
adding_file_allowed: False
difficulty: easy
target_complexity:
  time: O(n)
  space: O(1)
hints:
  - "Two words are anagrams if they use the same letters the same number of times. What could you compute for each word, and then compare?"
  - "Count the letters in each word with a dictionary (the *Counting* block in *Arrays & Hashing Basics*). The words are anagrams exactly when the two counts are equal."
  - "Template: if the lengths differ, return `False`. Otherwise build both letter counts and return whether they're equal (`collections.Counter` does the counting for you)."
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

### Valid Anagram

Write a function `is_anagram(word_one, word_two)` that takes two lowercase strings and returns `True` if `word_two` is an anagram of `word_one` (uses exactly the same letters, the same number of times, in any order), or `False` otherwise.

For example, `is_anagram("stone", "tones")` should return `True` since both strings share the exact same five letters, just in a different order. Two strings that aren't the same length, like `"stone"` and `"toness"`, can never be anagrams of each other.

---

### Tests

<ul>
<li id="test-1"><code>is_anagram("stone", "tones")</code> should return <code>True</code></li>
<li id="test-2"><code>is_anagram("stone", "toness")</code> should return <code>False</code></li>
<li id="test-3"><code>is_anagram("rat", "tar")</code> should return <code>True</code></li>
<li id="test-4"><code>is_anagram("rat", "car")</code> should return <code>False</code></li>
<li id="test-5"><code>is_anagram("", "")</code> should return <code>True</code></li>
<li id="test-6"><code>is_anagram("aabbcc", "abcabc")</code> should return <code>True</code></li>
<li id="test-7"><code>is_anagram("aab", "abb")</code> should return <code>False</code></li>
<li id="test-8">Performance: two 100,000-letter anagrams, within 1 second</li>
</ul>

<details class="border border-red-500 px-4 cursor-pointer">
<summary class="select-none">Solution</summary>

```python
from collections import Counter


def is_anagram(word_one, word_two):
    if len(word_one) != len(word_two):
        return False
    return Counter(word_one) == Counter(word_two)
```

**Brute force:** for each letter of `word_one`, find it in a list of `word_two`'s letters and remove it. Each `remove` scans the list, so this is `O(n²)`.

**Bottleneck:** searching for one letter at a time. You only need to know *how many* of each letter there are, not where they are.

**Optimal idea:** count each word's letters in a dictionary and compare the two counts.

**Why it's correct:** two words are anagrams exactly when every letter appears the same number of times in both, which is exactly when the two counts are equal.

**Complexity:** `O(n)` time to count both words. `O(1)` extra space, because there are at most 26 lowercase letters. Sorting both words (`sorted(word_one) == sorted(word_two)`) is also correct, and is a fine answer in an interview, but it's `O(n log n)`.

**Common mistakes:** comparing `set(word_one) == set(word_two)`, which ignores counts, so `"aab"` and `"abb"` look like anagrams.

</details>
