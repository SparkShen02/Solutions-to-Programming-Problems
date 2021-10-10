# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    '''
    Use two pointers to get to the middle of the linked list and split it into two lists. Then, reverse the second list. Lastly, compare the two linked lists. 
    Time complexity: O(n), Space complexity: O(1). 
    '''
    def isPalindrome(self, head: ListNode) -> bool:
        # Split the linked list into two lists
        n = 0
        slow = fast = head
        while fast != None:
            if fast.next == None:
                break
            slow = slow.next
            fast = fast.next.next
        firstList, secondList = head, slow

        # Reverse the second list, insert every node before the last node
        lastNode = None
        cur = secondList
        while cur != None:
            temp = cur.next
            cur.next = lastNode
            lastNode = cur
            cur = temp
        secondList = lastNode

        # Compare the two linked lists
        while secondList != None:
            if firstList.val != secondList.val:
                return False
            firstList, secondList = firstList.next, secondList.next
        return True
        