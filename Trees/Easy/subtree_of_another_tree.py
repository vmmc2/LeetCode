# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subroot: Optional[TreeNode]) -> bool:
        if subroot == None:
            return True
        if root == None:
            return False
        if self.isSameTree(root, subroot):
            return True
        return self.isSubtree(root.left, subroot) or self.isSubtree(root.right, subroot)

    def isSameTree(self, root: Optional[TreeNode], subroot: Optional[TreeNode]) -> bool:
        if root == None and subroot == None:
            return True
        elif root != None and subroot != None and root.val == subroot.val:
            return self.isSameTree(root.left, subroot.left) and self.isSameTree(root.right, subroot.right)
        else:
            return False
        