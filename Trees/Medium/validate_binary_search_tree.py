# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def auxIsValidBST(self, root: Optional[TreeNode], leftBound: int, rightBound: int) -> bool:
        if root == None:
            return True
        if leftBound >= root.val or rightBound <= root.val:
            return False
        
        leftResult = self.auxIsValidBST(root.left, leftBound, root.val)
        rightResult = self.auxIsValidBST(root.right, root.val, rightBound)

        return leftResult and rightResult

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.auxIsValidBST(root, -(2**32), 2**32)
        