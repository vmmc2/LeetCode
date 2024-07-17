# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        result = [0]

        def dfs(root, heightFromRoot):
            if root == None:
                return [0, -1] # diameter, height (considering the current node as the root)
            else:
                leftChildInfo = dfs(root.left, result)
                rightChildInfo = dfs(root.right, result)
                maxHeightFromRoot = 1 + max(leftChildInfo[1], rightChildInfo[1])
                maxDiameterFromRoot = leftChildInfo[1] + 1 + rightChildInfo[1] + 1

                result[0] = max(result[0], maxDiameterFromRoot)
                return [maxDiameterFromRoot, maxHeightFromRoot]

        dfs(root, [0, -1])

        return result[0]
