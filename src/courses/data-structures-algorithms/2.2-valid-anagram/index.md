---
lesson_name: Valid Anagram
code_editor: True
code_execution: True
adding_file_allowed: False
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
</ul>
