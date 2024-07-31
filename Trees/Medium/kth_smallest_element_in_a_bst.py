# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode], k: int, orderedNumbers: List[int]) -> None:
        if not root:
            return

        self.inorderTraversal(root.left, k, orderedNumbers)
        if len(orderedNumbers) == k:
            return
        orderedNumbers.append(root.val)
        if len(orderedNumbers) == k:
            return
        self.inorderTraversal(root.right, k, orderedNumbers)

        return

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        orderedNumbers = []
        self.inorderTraversal(root, k, orderedNumbers)

        return orderedNumbers[-1]
