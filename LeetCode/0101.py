# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    '''
    Recursion. 
    Time complexity: O(n), Space complexity: O(symmetric height) (from recursion calls). 
    '''
    def isSymmetric(self, root: TreeNode) -> bool:
        def compare(leftNode, rightNode):
            if leftNode == None and rightNode == None:
                return True
            if leftNode == None or rightNode == None:
                return False
            return leftNode.val == rightNode.val and compare(leftNode.right, rightNode.left) and compare(leftNode.left, rightNode.right)

        return compare(root.left, root.right)