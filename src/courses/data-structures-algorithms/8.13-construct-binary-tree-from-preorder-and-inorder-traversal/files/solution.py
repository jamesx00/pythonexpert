class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def tree_to_list(root):
    """Level-order serialize back to a list, trailing Nones trimmed."""
    if not root:
        return []
    result = []
    queue = [root]
    while queue:
        node = queue.pop(0)
        if node is None:
            result.append(None)
            continue
        result.append(node.val)
        queue.append(node.left)
        queue.append(node.right)
    while result and result[-1] is None:
        result.pop()
    return result


def build_tree_from_traversals(preorder, inorder):
    index = {val: i for i, val in enumerate(inorder)}
    next_root = iter(preorder)

    def build(lo, hi):
        if lo > hi:
            return None
        root = TreeNode(next(next_root))
        mid = index[root.val]
        root.left = build(lo, mid - 1)
        root.right = build(mid + 1, hi)
        return root

    return build(0, len(inorder) - 1)
