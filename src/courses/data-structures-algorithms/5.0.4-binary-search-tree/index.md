---
lesson_name: "Warm-up: Binary Search Tree"
code_editor: True
code_execution: True
adding_file_allowed: False
difficulty: medium
target_complexity:
  time: O(h) per operation
  space: O(h)
hints:
  - "For each operation, compare the key with the current node: which subtree could it possibly be in? For `delete`, what can replace a node that has **two** children without breaking the left-smaller, right-larger rule?"
  - "Follow *Binary Search Tree* in *Build-It-Yourself Data Structures Basics*. A recursive helper that **returns the new root of a subtree** handles every case: `node.left = self._delete(node.left, key)`. When you find the key: no left child → return `node.right`; no right child → return `node.left`; two children → copy in the smallest key of the right subtree, then delete that key from the right subtree."
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

### Warm-up: Binary Search Tree

Build a **binary search tree** of unique keys. Every node's left subtree holds only smaller keys, and its right subtree only larger keys. The tree is made of `Node` objects with `key`, `left` and `right`, and `self.root` is the top node (`None` for an empty tree).

Implement:

- `insert(key)`: add `key` in the position the BST rule gives it. If the key is already in the tree, do nothing.
- `contains(key)`: return `True` if `key` is in the tree, otherwise `False`.
- `inorder()`: return a list of the keys in in-order (left subtree, node, right subtree), which for a BST is sorted order.
- `delete(key)`: remove `key` if it's in the tree, otherwise do nothing. Handle all three cases:
  - a **leaf**: just remove it;
  - a node with **one child**: replace it with that child;
  - a node with **two children**: replace its key with its **in-order successor** (the smallest key in its right subtree), then delete that successor from the right subtree.

The tests check the tree's **shape**, not only its keys, by reading your nodes in preorder (node, left subtree, right subtree). For example, inserting `5, 3, 8, 1, 4` gives the preorder `[5, 3, 1, 4, 8]`.

---

### Tests

<ul>
<li id="test-1">insert 5, 3, 8, 1, 4: <code>inorder()</code> should return <code>[1, 3, 4, 5, 8]</code></li>
<li id="test-2">insert 5, 3, 8, 1, 4: the tree's keys in preorder should be <code>[5, 3, 1, 4, 8]</code></li>
<li id="test-3">insert 5, 3, 8, 1, 4: <code>contains(4)</code> should be <code>True</code> and <code>contains(6)</code> <code>False</code></li>
<li id="test-4"><code>contains(1)</code> on an empty tree should be <code>False</code></li>
<li id="test-5">insert 5, 5, 3: the duplicate should be ignored, so <code>inorder()</code> is <code>[3, 5]</code></li>
<li id="test-6">delete a leaf: insert 5, 3, 8, 1, 4, delete 1: preorder should be <code>[5, 3, 4, 8]</code></li>
<li id="test-7">delete a node with one child: insert 5, 3, 8, 1, delete 3: preorder should be <code>[5, 1, 8]</code></li>
<li id="test-8">delete a node with two children: insert 5, 3, 8, 1, 4, 7, 9, delete 3: preorder should be <code>[5, 4, 1, 8, 7, 9]</code></li>
<li id="test-9">delete the root: insert 5, 3, 8, 7, 9, 6, delete 5: its in-order successor <code>6</code> should become the root, preorder <code>[6, 3, 8, 7, 9]</code></li>
<li id="test-10">deleting a missing key should change nothing: insert 5, 3, 8, delete 4: preorder should stay <code>[5, 3, 8]</code></li>
<li id="test-11">delete the only node: insert 5, delete 5: <code>inorder()</code> should be <code>[]</code>; then insert 2: <code>inorder()</code> should be <code>[2]</code></li>
</ul>

<details class="border border-red-500 px-4 cursor-pointer">
<summary class="select-none">Solution</summary>

```python
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, node, key):
        if node is None:
            return Node(key)
        if key < node.key:
            node.left = self._insert(node.left, key)
        elif key > node.key:
            node.right = self._insert(node.right, key)
        return node

    def contains(self, key):
        node = self.root
        while node is not None:
            if key == node.key:
                return True
            node = node.left if key < node.key else node.right
        return False

    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, node, key):
        if node is None:
            return None
        if key < node.key:
            node.left = self._delete(node.left, key)
        elif key > node.key:
            node.right = self._delete(node.right, key)
        elif node.left is None:
            return node.right
        elif node.right is None:
            return node.left
        else:
            successor = node.right
            while successor.left is not None:
                successor = successor.left
            node.key = successor.key
            node.right = self._delete(node.right, successor.key)
        return node

    def inorder(self):
        keys = []

        def visit(node):
            if node is not None:
                visit(node.left)
                keys.append(node.key)
                visit(node.right)

        visit(self.root)
        return keys
```

**Brute force:** a plain unsorted list of keys. `insert` and `delete` are easy, but `contains` scans every key (`O(n)`), and `inorder` has to sort (`O(n log n)`). A sorted list makes `contains` a binary search, but then every insert and delete shifts items (`O(n)`).

**Bottleneck:** a list has to choose between fast search (sorted) and fast updates (unsorted).

**Optimal idea:** a BST keeps the keys "sorted" through its shape. Each comparison sends you left or right and rules out a whole subtree, like binary search, but inserting or deleting only changes a few links.

**Why it's correct:** `insert` and `contains` follow the only path where the key can be, given the BST rule. For `delete`: a leaf or a one-child node can be replaced by its only subtree (or `None`), because that subtree is already on the correct side of every ancestor. For a node with two children, the in-order successor is larger than everything in the left subtree and smaller than everything else in the right subtree, so putting its key in the node keeps the rule everywhere. The successor has no left child (it's the leftmost node of the right subtree), so deleting it afterwards is one of the easy cases. Returning the new subtree root from `_delete` makes deleting the root work the same way as deleting any other node.

**Complexity:** every operation walks one path from the root, so it's `O(h)`, where `h` is the tree's height. That's `O(log n)` when the tree is balanced, but `O(n)` when keys arrive in sorted order and the tree becomes a chain. `inorder` is `O(n)`. Space is `O(n)` for the nodes, plus `O(h)` for the recursion.

**Common mistakes:** forgetting to reassign the result of the recursive call (`node.left = self._delete(node.left, key)`), so the deleted node stays linked in the tree. Not updating `self.root` when the root is deleted. In the two-children case, deleting the successor from the whole tree instead of from the right subtree, or using the in-order **predecessor** when the tests expect the successor (both keep a valid BST, but the shape differs). Inserting duplicates as new nodes.

</details>
