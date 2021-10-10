# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    '''
    Reverse the input linked lists, then do a normal addition. 
    Time complexity: O(n), Space complexity: O(n) (the resulting linked list). 
    '''
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l1 = self.reverseLinkedList(l1)
        l2 = self.reverseLinkedList(l2)
        
        cur, prev = None, None
        adjustNum = 0
        while l1 != None or l2 != None:
            if l1 == None:
                num = l2.val
            elif l2 == None:
                num = l1.val
            else:
                num = l1.val + l2.val
            num += adjustNum
            cur = ListNode(num % 10, prev)

            adjustNum = 0 if num < 10 else 1
            prev = cur
            l1 = l1.next if l1 != None else l1
            l2 = l2.next if l2 != None else l2

        return ListNode(1, cur) if adjustNum == 1 else cur

    '''
    Insert each node before the previous node. 
    Time complexity: O(n), Space complexity: O(1). 
    '''
    def reverseLinkedList(self, l):
        cur, prev = l, None
        while cur != None:
            nextCur = cur.next
            cur.next = prev
            prev = cur
            cur = nextCur
        return prev
