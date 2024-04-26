class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def addOneRow(self, root, val, depth):
        """
        :type root: TreeNode
        :type val: int
        :type depth: int
        :rtype: TreeNode
        """
        if depth == 1:
            new_root = TreeNode(val)
            new_root.left = root
            return new_root
        self._addOneRow(root, val, depth, 1)
        return root
    
    def _addOneRow(self, node, val, depth, current_depth):
        if node is None:
            return
        if current_depth == depth - 1:
            left_child = TreeNode(val)
            right_child = TreeNode(val)
            left_child.left = node.left
            right_child.right = node.right
            node.left = left_child
            node.right = right_child
            return
        self._addOneRow(node.left, val, depth, current_depth + 1)
        self._addOneRow(node.right, val, depth, current_depth + 1)





root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(6)
root.left.left = TreeNode(3)
root.left.right = TreeNode(1)
root.right.left = TreeNode(5)
sol = Solution()
new_root = sol.addOneRow(root, 1, 2)
print(new_root)

