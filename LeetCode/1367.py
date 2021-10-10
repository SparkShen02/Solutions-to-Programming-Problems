# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    '''
    Recursion. 
    isSubPath(head, root) = rootStartsSubPath(head, root) || isSubPath(head, root.left) || isSubPath(head, root.right)
    '''
    def isSubPath(self, head: ListNode, root: TreeNode) -> bool:
        if head == None:
            return True
        if root == None:
            return False
        return self.rootStartsSubPath(head, root) or self.isSubPath(head, root.left) or self.isSubPath(head, root.right)

    def rootStartsSubPath(self, head, root):
        if head == None:
            return True
        if root == None:
            return False
        if head.val == root.val:
            return self.rootStartsSubPath(head.next, root.left) or self.rootStartsSubPath(head.next, root.right)
        else:
            return False