---
lesson_name: Kth Smallest Element in a BST
code_editor: True
code_execution: True
adding_file_allowed: False
difficulty: medium
target_complexity:
  time: O(h + k)
  space: O(h)
hints:
  - "In which order does an in-order walk visit a BST's values? When can you stop?"
  - "Use an in-order walk (the *Preorder, Inorder & Postorder* warm-up) and count nodes as you visit them. Stop at the `k`-th one instead of walking the whole tree."
  - "Template: `stack, node = [], root`. Loop: push `node` and go left until `None`; `node = stack.pop()`; `k -= 1`; if `k == 0`, return `node.val`; `node = node.right`."
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

### Kth Smallest Element in a BST

Write a function `kth_smallest(root, k)` that returns the `k`-th smallest value stored in a binary search tree, where `k` is `1`-based (`k=1` means the smallest value in the tree).

For example, in the BST built from `[5, 3, 8, 2, 4, 7, 9]`, the values in sorted order are `2, 3, 4, 5, 7, 8, 9`, so `kth_smallest(root, 3)` should return `4`.

---

### Tests

<ul>
<li id="test-1"><code>kth_smallest(build_tree([5, 3, 8, 2, 4, 7, 9]), 3)</code> should return <code>4</code></li>
<li id="test-2"><code>kth_smallest(build_tree([5, 3, 8, 2, 4, 7, 9]), 1)</code> should return <code>2</code></li>
<li id="test-3"><code>kth_smallest(build_tree([5, 3, 8, 2, 4, 7, 9]), 7)</code> should return <code>9</code></li>
<li id="test-4"><code>kth_smallest(build_tree([3, 1, 4, None, 2]), 1)</code> should return <code>1</code></li>
<li id="test-5"><code>kth_smallest(build_tree([3, 1, 4, None, 2]), 4)</code> should return <code>4</code></li>
<li id="test-6"><code>kth_smallest(build_tree([1]), 1)</code> should return <code>1</code></li>
<li id="test-7">Performance: 2,000 queries with <code>k</code> up to 50 on a 131,071-node BST, within 1 second</li>
</ul>

<details class="border border-red-500 px-4 cursor-pointer">
<summary class="select-none">Solution</summary>

```python
def kth_smallest(root, k):
    stack = []
    node = root
    while True:
        while node:
            stack.append(node)
            node = node.left
        node = stack.pop()
        k -= 1
        if k == 0:
            return node.val
        node = node.right
```

**Brute force:** collect every value with an in-order walk and return `order[k - 1]`. It's correct, but it always visits all `n` nodes and stores them, even when `k` is `1`.

**Bottleneck:** everything after the `k`-th value is visited for nothing.

**Optimal idea:** do the in-order walk with an explicit stack so you can stop the moment you pop the `k`-th node.

**Why it's correct:** an in-order walk of a BST visits values in increasing order. The stack version visits nodes in the same order: it goes as far left as possible, visits the node, then does the same for its right subtree. So the `k`-th node popped holds the `k`-th smallest value.

**Complexity:** `O(h + k)` time: `O(h)` to reach the smallest node, then about one step per node visited. `O(h)` extra space for the stack.

**Common mistakes:** treating `k` as 0-based. Building the full sorted list every time, which passes small tests but not the performance test. A recursive version can stop early too, but it needs a way to tell every caller to stop once the answer is found.

</details>
