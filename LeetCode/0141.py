# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    '''
    Use two pointers, one moves 1 step at a time while the other moves 2 steps at a time. See if the fast pointer will reach the slow pointer from behind. 
    Time complexity: O(n), Space complexity:O(1). 
    '''
    def hasCycle(self, head: ListNode) -> bool:
        slow = fast = head
        while True:
            if fast == None or fast.next == None:
                return False
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                return True
