# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    '''
    Recursion. f(node) returns the max path sum of a path that starts from node and goes downwards. f(node) = node.val + max(0, f(node.left), f(node.right)). 
    For each node n, the max path sum of a path whose highest node is n = n.val + max(0, f(n.left), f(n.right), f(n.left)+f(n.right)).
    Time complexity: O(n), Space complexity: O(height). 
    '''
    def maxPathSum(self, root: TreeNode) -> int:
        def f(node):
            if node == None:
                return 0
            left, right = f(node.left), f(node.right)
            self.ans = max(self.ans, node.val + max(0, left, right, left+right))
            return node.val + max(0, left, right)
        
        self.ans = root.val
        f(root)
        return self.ans