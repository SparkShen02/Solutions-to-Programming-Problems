# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    '''
    Recursion. subtreeSum(node) = node.val + subtreeSum(node.left) + subtreeSum(node.right). Record each subtree sum to a dictionary that counts the frequency. 
    Time complexity: O(n), Space complexity: O(n). 
    '''
    maxCount = -1
    def findFrequentTreeSum(self, root: TreeNode) -> List[int]:
        count = {}

        def subtreeSum(node):
            if node == None:
                return 0

            curSum = node.val + subtreeSum(node.left) + subtreeSum(node.right)
            if curSum not in count:
                count[curSum] = 0
            else:
                count[curSum] += 1
            self.maxCount = max(self.maxCount, count[curSum])

            return curSum
        
        subtreeSum(root)
        return [curSum for curSum in count if count[curSum] == self.maxCount]