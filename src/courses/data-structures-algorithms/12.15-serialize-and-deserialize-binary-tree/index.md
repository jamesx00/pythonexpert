---
lesson_name: Serialize and Deserialize Binary Tree
code_editor: True
code_execution: True
adding_file_allowed: False
difficulty: hard
target_complexity:
  time: O(n)
  space: O(n)
hints:
  - "A preorder list of values alone can't tell `[1, 2]` from `[1, None, 2]`. What extra information makes it unambiguous?"
  - "Use a preorder walk (*Recursive DFS* in *Trees Basics*) that writes a marker like `#` for every missing child. Rebuild with the same walk, reading values from an iterator."
  - "Template: `serialize`: `dfs(node)` appends `'#'` for `None`, else `str(node.val)` then recurses left and right; join with `,`. `deserialize`: `values = iter(data.split(','))`; `build()` reads one value, returns `None` for `'#'`, otherwise makes a node and builds its left then right child."
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

### Serialize and Deserialize Binary Tree

Implement two functions that are inverses of each other: `serialize(root)` should turn a binary tree into a single string, and `deserialize(data)` should take that string and rebuild the exact same tree structure (same shape, same values), returning its root.

You get to design the string format yourself — a common approach is a preorder walk that writes a placeholder (like `"#"`) for missing children, separated by commas, e.g. `"1,2,#,#,3,4,#,#,5,#,#"` for the tree built from `[1, 2, 3, None, None, 4, 5]`. As long as `deserialize(serialize(root))` always reproduces `root`'s exact structure, any format works.

---

### Tests

<ul>
<li id="test-1">for a tree built from <code>[1, 2, 3, None, None, 4, 5]</code>, <code>deserialize(serialize(root))</code> should rebuild to <code>[1, 2, 3, None, None, 4, 5]</code></li>
<li id="test-2">for a tree built from <code>[]</code>, <code>deserialize(serialize(root))</code> should rebuild to <code>[]</code></li>
<li id="test-3">for a tree built from <code>[1]</code>, <code>deserialize(serialize(root))</code> should rebuild to <code>[1]</code></li>
<li id="test-4">for a tree built from <code>[1, 2]</code>, <code>deserialize(serialize(root))</code> should rebuild to <code>[1, 2]</code></li>
<li id="test-5">for a tree built from <code>[5, 4, 7, 3, None, 2, None, -1, None, 9]</code>, <code>deserialize(serialize(root))</code> should rebuild to <code>[5, 4, 7, 3, None, 2, None, -1, None, 9]</code></li>
<li id="test-6">for a tree built from <code>[1, None, 2, None, 3, None, 4]</code>, <code>deserialize(serialize(root))</code> should rebuild to <code>[1, None, 2, None, 3, None, 4]</code></li>
</ul>

<details class="border border-red-500 px-4 cursor-pointer">
<summary class="select-none">Solution</summary>

```python
def serialize(root):
    values = []

    def dfs(node):
        if node is None:
            values.append('#')
            return
        values.append(str(node.val))
        dfs(node.left)
        dfs(node.right)

    dfs(root)
    return ','.join(values)


def deserialize(data):
    values = iter(data.split(','))

    def build():
        val = next(values)
        if val == '#':
            return None
        node = TreeNode(int(val))
        node.left = build()
        node.right = build()
        return node

    return build()
```

**Brute force:** store the level-order list with `None` for every missing child of a full tree of the same height. It works, but for a chain of `n` nodes the full tree has about `2^n` slots.

**Bottleneck:** storing positions for children that don't exist.

**Optimal idea:** write a marker only for the missing children of nodes that exist. A preorder walk with `#` markers gives `2n + 1` tokens, and the same walk can read them back.

**Why it's correct:** in the string, each subtree is either a single `#` or a value followed by its left subtree's string and then its right subtree's string. `build` reads exactly one subtree per call, in that same order, so it consumes exactly the tokens `serialize` wrote for that subtree and rebuilds the same shape and values.

**Complexity:** `O(n)` time for both functions. `O(n)` space for the string, plus `O(h)` for the call stack.

**Common mistakes:** leaving out the `#` markers, which loses the shape. Joining values without a separator, so `12` can't be told apart from `1` and `2`. Forgetting `int(...)` when rebuilding, which gives string values. Restarting the token list in every `build` call instead of sharing one iterator.

</details>
