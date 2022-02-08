# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    '''
    Use a hash table (set) to record the nodes that has been reached. 
    Time complexity: O(n), Space complexity: O(n). 
    '''
    def detectCycle(self, head: ListNode) -> ListNode:
        reached = set()
        cur = head
        while cur != None:
            if cur in reached:
                return cur
            reached.add(cur)
            cur = cur.next
        return None