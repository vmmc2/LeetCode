# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightDfs(self, root, currLevel: int, answer: List[int]) -> None:
        if root == None:
            return

        if currLevel == len(answer):
            answer.append(root.val)

        self.rightDfs(root.right, currLevel + 1, answer)
        self.rightDfs(root.left, currLevel + 1, answer)

        return

    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        currLevel = 0
        answer = []

        self.rightDfs(root, currLevel, answer)

        return answer
        