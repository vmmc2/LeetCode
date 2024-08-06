# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        answer = []

        def preorderTraversal(root):
            if not root:
                answer.append("N")
                return

            answer.append(str(root.val))
            preorderTraversal(root.left)
            preorderTraversal(root.right)

            return

        preorderTraversal(root)
        answer = ",".join(answer)

        return answer

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        preorder = data.split(",")
        self.idx = 0

        def preorderTraversal():
            if preorder[self.idx] == "N":
                self.idx += 1
                return None

            root = TreeNode(int(preorder[self.idx]))
            self.idx += 1
            root.left = preorderTraversal()
            root.right = preorderTraversal()

            return root

        root = preorderTraversal()

        return root
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))