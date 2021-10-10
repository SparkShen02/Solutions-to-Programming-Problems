# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    '''
    Repeatedly compare the first nodes of the two lists and insert the one with a smaller value to the merged list.
    Time complexity: O(n), Space complexity: O(1). 
    '''
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        preHead = ListNode()
        curNode = preHead
        while l1 != None and l2 != None:
            if l1.val < l2.val:
                curNode.next = l1
                curNode = curNode.next
                l1 = l1.next
            else:
                curNode.next = l2
                curNode = curNode.next
                l2 = l2.next

        # Insert the remaining nodes of the remaining list to the merged list
        if l1 != None:
            curNode.next = l1
        if l2 != None:
            curNode.next = l2

        return preHead.next
