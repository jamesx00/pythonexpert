---
lesson_name: Word Ladder
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

### Word Ladder

You are given a `start_word`, an `end_word`, and a `word_list` of allowed words, all the same length. Write a function `ladder_length(start_word, end_word, word_list)` that returns the number of words in the shortest transformation sequence from `start_word` to `end_word`, changing exactly one letter at a time, where every intermediate word (including `end_word`) must appear in `word_list`. `start_word` itself does not need to be in the list. If no such sequence exists, return `0`.

For example, with `start_word = "hit"`, `end_word = "cog"`, and `word_list = ["hot", "dot", "dog", "lot", "log", "cog"]`, one shortest path is `hit -> hot -> dot -> dog -> cog`, which has `5` words, so the function should return `5`.

---

### Tests

<ul>
<li id="test-1"><code>ladder_length("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"])</code> should return <code>5</code></li>
<li id="test-2"><code>ladder_length("hit", "cog", ["hot", "dot", "dog", "lot", "log"])</code> should return <code>0</code></li>
<li id="test-3"><code>ladder_length("a", "c", ["a", "b", "c"])</code> should return <code>2</code></li>
<li id="test-4"><code>ladder_length("hot", "dog", ["hot", "dog"])</code> should return <code>0</code></li>
<li id="test-5"><code>ladder_length("hot", "dog", ["hot", "dot", "dog"])</code> should return <code>3</code></li>
<li id="test-6"><code>ladder_length("cat", "cat", ["cat"])</code> should return <code>1</code></li>
<li id="test-7"><code>ladder_length("same", "cost", [])</code> should return <code>0</code></li>
</ul>

<details class="border border-red-500 px-4 cursor-pointer">
<summary class="select-none">Solution</summary>

```python
import string
from collections import deque

def ladder_length(start_word, end_word, word_list):
    words = set(word_list)
    if end_word not in words:
        return 0
    if start_word == end_word:
        return 1

    q = deque([(start_word, 1)])
    visited = {start_word}
    while q:
        word, length = q.popleft()
        if word == end_word:
            return length
        for i in range(len(word)):
            for ch in string.ascii_lowercase:
                candidate = word[:i] + ch + word[i + 1:]
                if candidate in words and candidate not in visited:
                    visited.add(candidate)
                    q.append((candidate, length + 1))
    return 0
```

</details>
