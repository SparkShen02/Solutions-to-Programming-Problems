"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""
class Solution:
    '''
    In-order traversal using recursion. Store the last-reached node as a instance attribute (like a global variable). 
    Time complexity: O(n), Space complexity: O(height) (from recursion calls). 
    '''
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if root == None:
            return None

        def recur(node):
            if node == None:
                return

            recur(node.left)

            if self.lastNode == None:
                self.head = node
            else:
                self.lastNode.right = node
                node.left = self.lastNode
            self.lastNode = node

            recur(node.right)

        self.lastNode = None
        recur(root)
        self.head.left = self.lastNode
        self.lastNode.right = self.head
        return self.head
