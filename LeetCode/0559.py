"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    '''
    Recursion. 
    maxDepth(node) = 1 + max(maxDepth(child) for every child of node)
    Time complexity: O(n), Space complexity: O(height of tree). 
    '''
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        maxChildDepth = 0
        for child in root.children:
            maxChildDepth = max(maxChildDepth, self.maxDepth(child))
        return maxChildDepth + 1