# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    '''
    Recursion. 
    Determine the answer from each subtree's height and lowest-leftmost value. 
    Time complexity: O(n), Space complexity: O(height of tree) (from recursion calls). 
    '''
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        def helper(node):
            if not node:
                return 0, None
            if not node.left and not node.right:
                return 1, node.val
            leftHeight, leftBotLeft = helper(node.left)
            rightHeight, rightBotLeft = helper(node.right)
            if leftHeight >= rightHeight:
                return leftHeight+1, leftBotLeft
            else:
                return rightHeight+1, rightBotLeft
        height, botLeft = helper(root)
        return botLeft