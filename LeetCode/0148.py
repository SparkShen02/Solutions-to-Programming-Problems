# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    '''
    Mergesort. Why not quicksort? Implementing quicksort for a singly-linked list is feasible but not convenient. Why not heapsort? Cannot easily access an element at a particular index. 
    Use a fast and a slow pointer to get the mid-node of the linked list. 
    Time complexity: O(nlog(n)), Space complexity: O(log(n)) (from recursion calls). 
    '''
    def sortList(self, head: ListNode) -> ListNode:
        if head == None:
            return head
        if head.next == None: # there's only one element
            return head

        slow = fast = head
        while fast.next != None:
            fast = fast.next
            if fast.next == None:
                break
            fast = fast.next
            slow = slow.next

        leftEnd, rightStart = slow, slow.next
        leftEnd.next = None # seperate the two parts
        left = self.sortList(head)
        right = self.sortList(rightStart)
        return self.mergeTwoLists(left, right)

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