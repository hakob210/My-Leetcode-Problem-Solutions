class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def smallestFromLeaf(self, root):
        """
        :type root: TreeNode
        :rtype: str
        """
        def dfs(node, path):
            if not node:
                return
            path.append(chr(ord('a') + node.val))
            if not node.left and not node.right:
                leaf_str = ''.join(path[::-1])
                self.smallest = min(self.smallest, leaf_str) if self.smallest else leaf_str
            dfs(node.left, path)
            dfs(node.right, path)
            path.pop()

        self.smallest = None
        dfs(root, [])
        return self.smallest

if __name__ == "__main__":
    # Test Case 1
    root1 = TreeNode(0)
    root1.left = TreeNode(1)
    root1.right = TreeNode(2)
    root1.left.left = TreeNode(3)
    root1.left.right = TreeNode(4)
    root1.right.left = TreeNode(3)
    root1.right.right = TreeNode(4)
    
    sol = Solution()
    print("Test Case 1:", sol.smallestFromLeaf(root1))

    root2 = TreeNode(25)
    root2.left = TreeNode(1)
    root2.right = TreeNode(3)
    root2.left.left = TreeNode(1)
    root2.left.right = TreeNode(3)
    root2.right.left = TreeNode(0)
    root2.right.right = TreeNode(2)

    print("Test Case 2:", sol.smallestFromLeaf(root2))

