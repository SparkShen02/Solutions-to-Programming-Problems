# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    '''
    Run a level-order traversal (breath-first search). 
    At each level, return false if "not all nodes are as far left as possible" or "numNodes != 2**levelNum and this is not the last level. "
    Time complexity: O(n), Space complexity: O(n). 
    '''
    def isCompleteTree(self, root: TreeNode) -> bool:
        from queue import Queue
        q = Queue()
        q.put(root)
        levelNum = -1
        while not q.empty():
            levelNum += 1
            hasNone = False
            isLast = True
            numNodes = 0
            for _ in range(q.qsize()):
                cur = q.get()
                if cur == None:
                    hasNone = True
                else:
                    if hasNone:
                        return False
                    numNodes += 1
                    q.put(cur.left)
                    q.put(cur.right)
                    if cur.left != None or cur.right != None:
                        isLast = False
            if numNodes != 2**levelNum and not isLast:
                return False
            if isLast:
                return True
