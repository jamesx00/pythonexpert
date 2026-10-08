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
    return None


def build_tree_from_traversals(preorder, inorder):
    if not preorder:
        return None
    root_val = preorder[0]
    root = TreeNode(root_val)
    idx = inorder.index(root_val)
    left_inorder = inorder[:idx]
    right_inorder = inorder[idx + 1:]
    left_preorder = preorder[1:1 + len(left_inorder)]
    right_preorder = preorder[1 + len(left_inorder):]
    root.left = build_tree_from_traversals(left_preorder, left_inorder)
    root.right = build_tree_from_traversals(right_preorder, right_inorder)
    return root
