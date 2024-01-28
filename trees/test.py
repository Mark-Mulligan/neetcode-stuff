from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        max_depth = 0

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return None
        else:
            print(root.val)

        if root.right:
            self.maxDepth(root.right)
        if root.left:
            self.maxDepth(root.left)


branch_2 = TreeNode(2)
branch_3 = TreeNode(3, branch_2)
branch_6 = TreeNode(6)
tree_root = TreeNode(5, branch_3, branch_6)

solution = Solution()
answer = solution.maxDepth(tree_root)
