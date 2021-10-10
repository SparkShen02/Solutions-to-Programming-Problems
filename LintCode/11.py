"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: param root: The root of the binary search tree
    @param k1: An integer
    @param k2: An integer
    @return: return: Return all keys that k1<=key<=k2 in ascending order
    """
    def searchRange(self, root, k1, k2):
        needToGo=[]
        result=[]
        if root is None:
            return result
        needToGo.append(root)
        while needToGo:
            current=needToGo.pop()
            print(current.val)
            if k1<=current.val<=k2:
                result.append(current.val)
            if current.left is not None:
                needToGo.append(current.left)
            if current.right is not None:
                needToGo.append(current.right)
        return result