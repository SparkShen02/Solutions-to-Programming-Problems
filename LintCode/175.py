"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: a TreeNode, the root of the binary tree
    @return: nothing
    """
    def invertBinaryTree(self, root):
        if root is not None:
            temp=root.left
            root.left=root.right
            root.right=temp
            self.invertBinaryTree(root.right)
            self.invertBinaryTree(root.left)