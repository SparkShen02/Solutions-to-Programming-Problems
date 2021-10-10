# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    '''
    Recursion. postorderTraversal(node) = postorderTraversal(node.left) + postorderTraversal(node.right) + [node.val]. 
    Time complexity: O(n), Space complexity: O(height). 
    '''
    def postorderTraversal(self, node: TreeNode) -> List[int]:
        ans = []
        if node == None:
            return ans
        return self.postorderTraversal(node.left) + self.postorderTraversal(node.right) + [node.val]