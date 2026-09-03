---
lesson_name: Encode and Decode Strings
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

### Encode and Decode Strings

Write two functions, `encode(words)` and `decode(encoded)`, that work together to pack a list of strings into a single string and unpack it again. `encode(words)` takes a list of strings (which may contain any characters, including digits, spaces, and punctuation) and returns one combined string. `decode(encoded)` takes a string produced by `encode` and returns the original list of strings, in the same order.

The two functions must round-trip correctly for any list of strings, including strings that themselves contain numbers or the characters you might otherwise be tempted to use as a separator. For example, `encode(["4:cats", "dogs"])` must decode back to exactly `["4:cats", "dogs"]`, not something that gets confused by the colon or the digit `4` inside the first word.

---

### Tests

<ul>
<li id="test-1"><code>decode(encode(["cat", "dog"]))</code> should return <code>["cat", "dog"]</code></li>
<li id="test-2"><code>decode(encode([]))</code> should return <code>[]</code></li>
<li id="test-3"><code>decode(encode([""]))</code> should return <code>[""]</code></li>
<li id="test-4"><code>decode(encode(["4:cats", "dogs"]))</code> should return <code>["4:cats", "dogs"]</code></li>
<li id="test-5"><code>decode(encode(["a", "", "bb", ""]))</code> should return <code>["a", "", "bb", ""]</code></li>
<li id="test-6"><code>decode(encode(["hello world", "foo#bar"]))</code> should return <code>["hello world", "foo#bar"]</code></li>
</ul>

<details class="border border-red-500 px-4 cursor-pointer">
<summary class="select-none">Solution</summary>

```python
def encode(words):
    return "".join(f"{len(w)}#{w}" for w in words)


def decode(encoded):
    words = []
    i = 0
    while i < len(encoded):
        j = i
        while encoded[j] != "#":
            j += 1
        length = int(encoded[i:j])
        start = j + 1
        words.append(encoded[start:start + length])
        i = start + length
    return words
```

</details>
