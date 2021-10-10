# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    '''
    Recursion. 
    Time complexity: O(n), Space complexity: O(height) (from recursion calls). 
    '''
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root == None:
            return None
        temp = self.invertTree(root.right)
        root.right = self.invertTree(root.left)
        root.left = temp
        return root