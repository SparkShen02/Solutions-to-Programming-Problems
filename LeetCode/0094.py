# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    '''
    Recursion. inorderTraversal(node) = inorderTraversal(node.left) + [node.val] + inorderTraversal(node.right).
    Time complexity: O(n), Space complexity: O(height). 
    '''
    def inorderTraversal(self, node: TreeNode) -> List[int]:
        ans = []
        if node == None:
            return ans
        return self.inorderTraversal(node.left) + [node.val] + self.inorderTraversal(node.right)