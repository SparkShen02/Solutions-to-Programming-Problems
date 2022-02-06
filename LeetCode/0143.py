# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    '''
    Use a slow pointer and a fast pointer to locate the center of the linked list. Then, reverse the right half of the linked list. Lastly, merge the left half and the reversed right half of the linked list. 
    Time complexity: O(n), Space complexity: O(1). 
    '''
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # Locate the center of the linked list
        slow, fast = head, head
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
        rightHead = slow.next
        slow.next = None

        # Reverse the right half of the linked list (insert every node before the previous node)
        cur = rightHead
        prev = None
        while cur != None:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        rightHead = prev

        # Merge
        curLeft = head
        curRight = rightHead
        while curRight != None:
            nextLeft = curLeft.next
            nextRight = curRight.next
            curLeft.next = curRight
            curRight.next = nextLeft
            curLeft = nextLeft
            curRight = nextRight
        return head
