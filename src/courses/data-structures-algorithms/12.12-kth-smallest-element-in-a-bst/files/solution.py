class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_tree(values):
    """Level-order build from a list, None marks a missing child (LeetCode style)."""
    if not values or values[0] is None:
        return None
    it = iter(values)
    root = TreeNode(next(it))
    queue = [root]
    while queue:
        node = queue.pop(0)
        try:
            left_val = next(it)
        except StopIteration:
            break
        if left_val is not None:
            node.left = TreeNode(left_val)
            queue.append(node.left)
        try:
            right_val = next(it)
        except StopIteration:
            break
        if right_val is not None:
            node.right = TreeNode(right_val)
            queue.append(node.right)
    return root


def kth_smallest(root, k):
    return None


def kth_smallest(root, k):
    order = []

    def inorder(node):
        if node is None:
            return
        inorder(node.left)
        order.append(node.val)
        inorder(node.right)

    inorder(root)
    return order[k - 1]
