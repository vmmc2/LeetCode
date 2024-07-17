# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root == None:
            return None

        leftChild = self.invertTree(root.left)
        rightChild = self.invertTree(root.right)

        root.left = rightChild
        root.right = leftChild

        return root
