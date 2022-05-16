# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    '''
    In-order traversal using recursion. 
    Time complexity: O(n), Space complexity: O(height of the tree) (from recursion calls). 
    '''
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> TreeNode:
        self.ans = None
        self.nextIsAns = False

        def inOrder(node):
            if not node:
                return
            inOrder(node.left)
            if self.ans:
                return
            if self.nextIsAns:
                self.ans = node
                return
            if node == p:
                self.nextIsAns = True
            inOrder(node.right)
        
        inOrder(root)
        return self.ans