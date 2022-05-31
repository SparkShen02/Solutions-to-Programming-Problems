# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    '''
    Recursion.
    buildTree(pre-order of node, in-order of node)  =                                                              node
                                                        buildTree(pre-order of node.left, in-order of node.left)          buildTree(pre-order of node.right, in-order of node.right)
    
    Pre-order traversal of node = node + pre-order traversal of node.left + pre-order traversal of node.right.
    In-order traversal of node = in-order traversal of node.left + node + in-order traversal of node.right.

    Use a dictionary d to store the elements in the in-order traversal with their indexes. 

    Time complexity: O(n), Space complexity: O(n). 
    '''
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        d = {}
        for i in range(len(inorder)):
            d[inorder[i]] = i

        def recur(startOfPreorder, endOfPreorder, startOfInorder, endOfInorder):
            if startOfInorder > endOfInorder:
                return None
            
            nodeVal = preorder[startOfPreorder]
            nodeInd = d[nodeVal] - startOfInorder

            startOfInorderLeft, endOfInorderLeft = startOfInorder, startOfInorder+nodeInd-1
            startOfInorderRight, endOfInorderRight = startOfInorder+nodeInd+1, endOfInorder
            startOfPreorderLeft, endOfPreorderLeft = startOfPreorder+1, startOfPreorder+nodeInd
            startOfPreorderRight, endOfPreorderRight = startOfPreorder+nodeInd+1, endOfPreorder

            return TreeNode(nodeVal, recur(startOfPreorderLeft, endOfPreorderLeft, startOfInorderLeft, endOfInorderLeft), recur(startOfPreorderRight, endOfPreorderRight, startOfInorderRight, endOfInorderRight))
        
        return recur(0, len(preorder)-1, 0, len(inorder)-1)