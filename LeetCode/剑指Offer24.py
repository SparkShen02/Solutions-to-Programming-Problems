# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    '''
    Insert every element before the last element. 
    Time complexity: O(n), Space complexity: O(n). 
    '''
    def reverseList(self, head: ListNode) -> ListNode:
        lastNode = None
        curNode = head
        while (curNode != None):
            # Insert curNode before lastNode
            nextNode = curNode.next
            curNode.next = lastNode
            lastNode = curNode
            curNode = nextNode
        return lastNode