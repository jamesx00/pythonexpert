---
lesson_name: Lowest Common Ancestor of a BST
code_editor: True
code_execution: True
adding_file_allowed: False
difficulty: medium
target_complexity:
  time: O(h)
  space: O(1)
hints:
  - "Compare `p.val` and `q.val` with the current node. If both are smaller, where must their lowest common ancestor be?"
  - "Use the BST ordering with *Passing info down* from *Trees Basics*: walk down from the root, going left while both values are smaller and right while both are larger. The first node where they split (or where one of them sits) is the answer."
  - "Template: `node = root`. While `node`: if both are smaller, `node = node.left`; elif both are larger, `node = node.right`; else return `node`."
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

### Lowest Common Ancestor of a BST

Write a function `lowest_common_ancestor(root, p, q)` that takes the root of a binary **search** tree along with two nodes `p` and `q` that are guaranteed to exist somewhere in it, and returns their lowest common ancestor node — the deepest node that has both `p` and `q` in its subtree (a node counts as its own ancestor).

For example, in the BST built from `[6, 2, 8, 0, 4, 7, 9, None, None, 3, 5]`, the lowest common ancestor of the nodes with values `2` and `8` is the node `6`, since neither is a descendant of the other. The lowest common ancestor of `2` and `4` is the node `2` itself, since `4` sits inside `2`'s subtree.

---

### Tests

<ul>
<li id="test-1"><code>lowest_common_ancestor(build_tree([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5]), node(2), node(8))</code> should return the node <code>6</code></li>
<li id="test-2"><code>lowest_common_ancestor(build_tree([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5]), node(2), node(4))</code> should return the node <code>2</code></li>
<li id="test-3"><code>lowest_common_ancestor(build_tree([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5]), node(3), node(5))</code> should return the node <code>4</code></li>
<li id="test-4"><code>lowest_common_ancestor(build_tree([2, 1]), node(2), node(1))</code> should return the node <code>2</code></li>
<li id="test-5"><code>lowest_common_ancestor(build_tree([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5]), node(7), node(9))</code> should return the node <code>8</code></li>
<li id="test-6"><code>lowest_common_ancestor(build_tree([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5]), node(0), node(5))</code> should return the node <code>2</code></li>
<li id="test-7">Performance: 2,000 queries on a 131,071-node BST, within 1 second</li>
</ul>

<details class="border border-red-500 px-4 cursor-pointer">
<summary class="select-none">Solution</summary>

```python
def lowest_common_ancestor(root, p, q):
    node = root
    while node:
        if p.val < node.val and q.val < node.val:
            node = node.left
        elif p.val > node.val and q.val > node.val:
            node = node.right
        else:
            return node
```

**Brute force:** ignore the ordering and treat it like any binary tree: from the root, step into whichever child contains both `p` and `q`, searching the subtrees to find out. Each search can walk a whole subtree, so one query costs `O(n)` or more.

**Bottleneck:** in a BST you never need to search for a node: its value tells you which side it's on.

**Optimal idea:** walk down from the root. If both values are smaller than the current node, both nodes are in the left subtree, so the answer is too. If both are larger, go right. Otherwise they split here, or one of them is this node, so this is the answer.

**Why it's correct:** while both values are on the same side, the current node is a common ancestor but its child on that side is a deeper one. At the first node where they split, `p` and `q` are in different subtrees (or one is the node itself), so no deeper node holds both.

**Complexity:** `O(h)` time, one step per level: `O(log n)` on a balanced BST. `O(1)` extra space with the loop.

**Common mistakes:** returning `node.val` instead of the node. Using `<=` and `>=` in the comparisons, which walks past the node when it is `p` or `q` itself. Searching both subtrees as in a plain binary tree, which works but throws away the BST ordering.

</details>
