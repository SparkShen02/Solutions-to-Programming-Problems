# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    '''
    Recursion. height(node) = max(height(node.left), height(node.right)) + 1.
    Time complexity: O(n), Space complexity: O(height) (from recursion calls). 
    '''
    ans = True
    def isBalanced(self, root: TreeNode) -> bool:
        def height(node):
            if node == None:
                return 0
            l, r = height(node.left), height(node.right)
            if abs(l-r) > 1:
                self.ans = False
            return max(l, r) + 1
        height(root)
        return self.ans
