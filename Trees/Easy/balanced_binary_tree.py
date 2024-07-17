# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        result = [True]

        def dfs(root: Optional[TreeNode]) -> int:
            if root == None:
                return -1
            else:
                leftSubtreeHeight = 1 + dfs(root.left)
                rightSubtreeHeight = 1 + dfs(root.right)
                heightDiff = max(leftSubtreeHeight, rightSubtreeHeight) - min(leftSubtreeHeight, rightSubtreeHeight)
                if heightDiff > 1:
                    result[0] = False
                return max(leftSubtreeHeight, rightSubtreeHeight)

        dfs(root)

        return result[0]
