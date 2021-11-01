# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    '''
    Recursion.
    buildTree(in-order of node, post-order of node)  =                                                              node
                                                        buildTree(in-order of node.left, post-order of node.left)          buildTree(in-order of node.right, post-order of node.right)
    
    In-order traversal of node = in-order traversal of node.left + node + in-order traversal of node.right. 
    Post-order traversal of node = post-order traversal of node.left + post-order traversal of node.right + node. 

    Use a dictionary d to store the elements in the in-order traversal with their indexes. 

    Time complexity: O(n), Space complexity: O(n). 
    '''
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        d = {}
        for i in range(len(inorder)):
            d[inorder[i]] = i

        def recur(startOfInorder, endOfInorder, startOfPostorder, endOfPostorder):
            if startOfInorder > endOfInorder:
                return None
            
            nodeVal = postorder[endOfPostorder]
            nodeInd = d[nodeVal] - startOfInorder

            startOfInorderLeft, endOfInorderLeft = startOfInorder, startOfInorder+nodeInd-1
            startOfInorderRight, endOfInorderRight = startOfInorder+nodeInd+1, endOfInorder
            startOfPostorderLeft, endOfPostorderLeft = startOfPostorder, startOfPostorder+nodeInd-1
            startOfPostorderRight, endOfPostorderRight = startOfPostorder+nodeInd, endOfPostorder-1

            return TreeNode(nodeVal, recur(startOfInorderLeft, endOfInorderLeft, startOfPostorderLeft, endOfPostorderLeft), recur(startOfInorderRight, endOfInorderRight, startOfPostorderRight, endOfPostorderRight))
        
        return recur(0, len(inorder)-1, 0, len(postorder)-1)