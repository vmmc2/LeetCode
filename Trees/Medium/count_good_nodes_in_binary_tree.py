# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def dfs(self, root: TreeNode, maxStack: List[tuple], numGoodNodes: List[int]) -> None:
        if root == None:
            return

        if len(maxStack) == 0:
            maxStack.append((root.val, root.val))
            numGoodNodes[0] += 1
        elif root.val >= maxStack[-1][1]:
            maxStack.append((root.val, root.val))
            numGoodNodes[0] += 1
        else:
            largestVal = maxStack[-1][1]
            maxStack.append((root.val, largestVal))

        self.dfs(root.left, maxStack, numGoodNodes)
        self.dfs(root.right, maxStack, numGoodNodes)
        
        maxStack.pop()

        return

    def goodNodes(self, root: TreeNode) -> int:
        numGoodNodes = [0]
        maxStack = []

        self.dfs(root, maxStack, numGoodNodes)

        return numGoodNodes[0]
