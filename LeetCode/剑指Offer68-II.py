# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    '''
    Run DFS and record each node's parent node. 
    Start from p, go up to the root node. Mark each node on the way as an ancestor of p. 
    Start from q, go up to the root node. If reached an ancestor of p, return the ancestor. 
    Time complexity: O(n), Space complexity: O(n). 
    '''
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        parent = { root: None }
        s = [root]
        while len(s) != 0:
            cur = s.pop()
            if cur.left != None:
                parent[cur.left] = cur
                s.append(cur.left)
            if cur.right != None:
                parent[cur.right] = cur
                s.append(cur.right)
        
        ancestorOfP = set()
        while p != None:
            ancestorOfP.add(p)
            p = parent[p]

        while q != None:
            if q in ancestorOfP:
                return q
            q = parent[q]
        