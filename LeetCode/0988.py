# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    '''
    Depth-first search / backtrack. Construct all the strings and compare them to find the minimum. 
    The candidates for the next level consists of (the current string + the char represented by the left child) and (the current string + the char represented by the right child). 
    Use a list to keep track of the current string and use join() to form the string when a leaf node is reached. This lowers the time & space complexity of concatenating strings. 
    Time complexity: O(n), Space complexity: O(n). 
    '''
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        num2char = "abcdefghijklmnopqrstuvwxyz"

        def dfs(node, curStr):
            if not node.left and not node.right: # a leaf node is reached
                self.ans = min(self.ans, "".join(curStr)[::-1])
            if node.left:
                curStr.append(num2char[node.left.val])
                dfs(node.left, curStr)
                curStr.pop() # restore the current string
            if node.right:
                curStr.append(num2char[node.right.val])
                dfs(node.right, curStr)
                curStr.pop() # restore the current string

        self.ans = "~"
        dfs(root, [num2char[root.val]])
        return self.ans