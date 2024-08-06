# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    def preorderTraversal(self, root, preorder):
        if not root:
            preorder.append('N')
            return

        preorder.append(str(root.val))
        self.preorderTraversal(root.left, preorder)
        self.preorderTraversal(root.right, preorder)

        return

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        preorder = []
        self.preorderTraversal(root, preorder)
        preorder = ",".join(preorder)

        return preorder
        
    def buildTree(self, preorder):
        if not preorder:
            return None
        
        root_val = preorder.pop(0)
        if root_val == 'N':
            return None
        else:
            root = TreeNode(val=int(root_val))
            root.left = self.buildTree(preorder)
            root.right = self.buildTree(preorder)

            return root

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        preorder = data.split(',')
        root = self.buildTree(preorder)

        return root
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))