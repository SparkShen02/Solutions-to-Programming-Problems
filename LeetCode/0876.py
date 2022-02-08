# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    '''
    Use a slow pointer and a fast pointer to get to the middle of the linked list. 
    Time complexity: O(n), Space complexity: O(1). 
    '''
    def middleNode(self, head: ListNode) -> ListNode:
        slow, fast = head, head
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
        return slow