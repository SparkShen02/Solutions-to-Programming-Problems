# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    '''
    Depth-first search. 
    Time complexity: O(n), Space complexity: O(n). 
    '''
    def numColor(self, root: TreeNode) -> int:
        color = set()
        s = [root]
        while len(s) != 0:
            cur = s.pop()
            color.add(cur.val)
            if cur.left != None:
                s.append(cur.left)
            if cur.right != None:
                s.append(cur.right)
        return len(color)