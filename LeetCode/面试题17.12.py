# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

'''
                                B                           A
Recursion. For a binary tree  A   C  , convert it to  null       B    . More specifically, convert
                                                             null  C

             root                         converted-left-tree
left-subtree      right-subtree  ->  null                     root
                                                         null      converted-right-subtree  .

Time complexity: O(n), Space complexity: O(n) (from recursion calls). 
'''
class Solution:
    # Return start and end of the converted tree.
    def convert(self, root):
        if (root.left == None):
            if (root.right != None):
                startRight, endRight = self.convert(root.right)
                root.right = startRight
                return root, endRight
            else:
                return root, root

        startLeft, endLeft = self.convert(root.left)
        endLeft.left = None
        endLeft.right = root
        root.left = None

        if (root.right == None): # and root.left != None
            return startLeft, root

        startRight, endRight = self.convert(root.right)
        root.right = startRight

        return startLeft, endRight

    def convertBiNode(self, root: TreeNode) -> TreeNode:
        if (root == None):
            return root;
        return self.convert(root)[0]