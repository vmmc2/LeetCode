# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def auxMaxPathSum(self, root: Optional[TreeNode]) -> (int, int):
        if not root:
            return (float("-inf"), float("-inf"))
        else:
            left = self.auxMaxPathSum(root.left)
            right = self.auxMaxPathSum(root.right)

            print(left)
            print(right)

            maxSum = max(root.val, root.val + left[1], root.val + right[1], root.val + left[1] + right[1], left[0], right[0])
            maxSumPassingThroughNode = max(root.val + left[1], root.val + right[1], root.val)

            return (maxSum, maxSumPassingThroughNode)


    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        answer = self.auxMaxPathSum(root)

        return answer[0]