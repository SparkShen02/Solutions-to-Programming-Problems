"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param: root: the root of binary tree
    @param: target: An integer
    @return: all valid paths
    """
    def binaryTreePathSum(self, r, target):
        from copy import deepcopy
        
        def dfs( r, path_sum, path, res):
            if r is None:
                return 
        
            path.append(r.val)
            path_sum += r.val
            # A valid path is from root node to any of the leaf nodes.
            # accumerate from root and end at leaves r.left is None and r.right is None 
            if r.left is None and r.right is None and path_sum == target:
                res.append(deepcopy(path))
                
            dfs(r.left,path_sum, path, res)
            dfs(r.right,path_sum, path, res)
            
            path.pop()
            
        path_sum, path, res = 0, [], []
        dfs(r,path_sum,path, res)
        return res
