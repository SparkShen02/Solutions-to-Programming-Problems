# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    '''
    Recursion. maxDepth(node) = 1 + max(maxDepth(node.left), maxDepth(node.right)).
    Time complexity: O(n), Space complexity: O(height) (from recursion calls). 
    '''
    def maxDepth(self, root: TreeNode) -> int:
        if root == None:
            return 0
        else:
            return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
