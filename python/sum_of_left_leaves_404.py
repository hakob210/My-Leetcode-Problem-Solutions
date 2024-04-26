class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def is_leaf(node):
            return node and not node.left and not node.right

        def dfs(node, is_left):
            if not node:
                return 0
            if is_leaf(node) and is_left:
                return node.val
            return dfs(node.left, True) + dfs(node.right, False)

        return dfs(root, False)

def list_to_tree(lst):
    if not lst:
        return None
    nodes = [None if val is None else TreeNode(val) for val in lst]
    for i, node in enumerate(nodes):
        if node:
            left_child_idx = 2 * i + 1
            right_child_idx = 2 * i + 2
            if left_child_idx < len(nodes):
                node.left = nodes[left_child_idx]
            if right_child_idx < len(nodes):
                node.right = nodes[right_child_idx]
    return nodes[0]





sol = Solution()
tree_root = list_to_tree([3,9,20,None,None,15,7])
print(sol.sumOfLeftLeaves(tree_root))

