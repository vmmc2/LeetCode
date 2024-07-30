# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def dfs(self, level: int, root: TreeNode, nodeToLevel: Dict, levels: List[int]) -> None:
        if root == None:
            return

        nodeToLevel[root] = level

        if level > levels[0]: levels[0] = level

        self.dfs(level + 1, root.left, nodeToLevel, levels)
        self.dfs(level + 1, root.right, nodeToLevel, levels)

        return

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None:
            return []

        levels = [-1]        
        nodeToLevel = {}
        self.dfs(0, root, nodeToLevel, levels)
        
        answer = [[] for i in range(levels[0] + 1)]
        
        for key, value in nodeToLevel.items():
            answer[value].append(key.val)

        return answer
