# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    '''
    Divide and conquer. 
    mergeKLists(lists):
        Respectively merge lists[0] with lists[1], lists[2] with lists[3], ..., and save the merged lists in-place in lists
        mergeKLists(lists)
    Time complexity: O(knlog(k)), Space complexity: O(log(k)) (from recursion calls) where k is the # of linked lists and n is the max length of a linked list. 
    '''
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists:
            return None

        def helper(lists, start, end):
            if start == end:
                return lists[start]
            merged = start # points after the end of the merged lists
            for i in range(start, end, 2):
                lists[merged] = self.mergeTwoLists(lists[i], lists[i+1])
                merged += 1
            if (end-start+1) % 2 != 0: # the last linked list is not paired and merged
                lists[merged] = lists[end]
                merged += 1
            return helper(lists, start, merged-1)
        return helper(lists, 0, len(lists)-1)

    '''
    Repeatedly compare the first nodes of the two linked lists and insert the one with a smaller value to the merged list.
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