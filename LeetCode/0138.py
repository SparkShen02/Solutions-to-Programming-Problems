"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    '''
    For each original node, copy a new code to its right. Then, copy the random pointers. Lastly, detach the original and the new linked list. 
    Time complexity: O(n), Space complexity: O(n) (the resulting list). 
    '''
    def copyRandomList(self, head: 'Node') -> 'Node':
        if head == None:
            return None

        cur = head
        while cur != None:
            newCur = Node(cur.val)
            newCur.next = cur.next
            cur.next = newCur
            cur = newCur.next
        
        # Copy the random pointers
        cur = head
        while cur != None:
            if cur.random == None:
                cur.next.random = None
            else:
                cur.next.random = cur.random.next
            cur = cur.next.next

        # Detach
        newHead = head.next
        cur = head
        while cur != None:
            if cur.next.next == None:
                break
            newCur = cur.next
            cur.next = newCur.next
            newCur.next = newCur.next.next
            cur = cur.next
        
        return newHead
            

