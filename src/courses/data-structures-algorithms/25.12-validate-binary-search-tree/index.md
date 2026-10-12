---
lesson_name: Validate Binary Search Tree
code_editor: True
code_execution: True
adding_file_allowed: False
difficulty: medium
target_complexity:
  time: O(n)
  space: O(h)
hints:
  - "Pattern: *Trees*."
  - "Checking each node against its parent isn't enough. Which values is a node deep in the right subtree of `5` allowed to have?"
  - "Use *Passing info down* from *Trees Basics*: pass an allowed range `(low, high)` down. Going left lowers `high` to the node's value; going right raises `low` to it."
  - "Template: `valid(node, low, high)`: `True` for `None`; `False` unless `low < node.val < high`; then `valid(node.left, low, node.val) and valid(node.right, node.val, high)`. Start with minus and plus infinity."
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

### Validate Binary Search Tree

Write a function `is_valid_bst(root)` that returns `True` if the tree obeys the binary search tree property everywhere — every node's value must be strictly greater than all values in its left subtree and strictly less than all values in its right subtree — and `False` otherwise.

For example, `build_tree([5, 3, 8, 1, 4, 7, 9])` is a valid BST. But `build_tree([5, 4, 6, None, None, 3, 7])` is not, even though every node is in the right order with its own children: the node `3` is the left child of `6`, which is fine for `6`, but it sits in `5`'s right subtree and is smaller than `5`.

---

### Tests

<ul>
<li id="test-1"><code>is_valid_bst(build_tree([5, 3, 8, 1, 4, 7, 9]))</code> should return <code>True</code></li>
<li id="test-2"><code>is_valid_bst(build_tree([5, 1, 4, None, None, 3, 6]))</code> should return <code>False</code></li>
<li id="test-3"><code>is_valid_bst(build_tree([2, 1, 3]))</code> should return <code>True</code></li>
<li id="test-4"><code>is_valid_bst(build_tree([1, 1]))</code> should return <code>False</code></li>
<li id="test-5"><code>is_valid_bst(build_tree([]))</code> should return <code>True</code></li>
<li id="test-6"><code>is_valid_bst(build_tree([10, 5, 15, None, None, 6, 20]))</code> should return <code>False</code></li>
<li id="test-7">Performance: a 66,335-node BST (an 800-node chain above a 65,535-node perfect BST), within 1 second</li>
</ul>

<details class="border border-red-500 px-4 cursor-pointer">
<summary class="select-none">Solution</summary>

```python
def is_valid_bst(root):
    def valid(node, low, high):
        if node is None:
            return True
        if not (low < node.val < high):
            return False
        return valid(node.left, low, node.val) and valid(node.right, node.val, high)

    return valid(root, float('-inf'), float('inf'))
```

**Brute force:** at every node, collect all the values in its left and right subtrees and check they're smaller and larger. Each node walks its whole subtree, so a deep tree takes `O(n^2)` time.

**Bottleneck:** a node only needs the largest value on its left and the smallest on its right, and those are compared again for every ancestor.

**Optimal idea:** turn it around. Instead of each node looking down, each node gets the range it must fit in from above. Going left, the parent's value becomes the new upper bound; going right, it becomes the new lower bound.

**Why it's correct:** every ancestor puts a bound on a node: it must be smaller than the ancestors it is left of and larger than those it is right of. The range passed down is the tightest of these bounds, so checking `low < node.val < high` at every node checks every ancestor pair at once.

**Complexity:** `O(n)` time, each node is checked once. `O(h)` extra space for the call stack.

**Common mistakes:** comparing a node only with its own children, which accepts `[5, 4, 6, None, None, 3, 7]`. Using `<=`, which allows duplicates: `[1, 1]` must be `False`. Using `0` or some large number as the starting bounds instead of infinity. An in-order walk that checks the values strictly increase is another correct `O(n)` solution.

</details>
