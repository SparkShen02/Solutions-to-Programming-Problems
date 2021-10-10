# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    '''
    Recursion. preorderTraversal(node) = [node.val] + preorderTraversal(node.left) + preorderTraversal(node.right). 
    Time complexity: O(n), Space complexity: O(height) (from recursion calls). 
    '''
    def preorderTraversal(self, node: TreeNode) -> List[int]:
        ans = []
        if node == None:
            return ans
        return [node.val] + self.preorderTraversal(node.left) + self.preorderTraversal(node.right)