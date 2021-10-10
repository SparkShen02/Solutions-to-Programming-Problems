# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    '''
    Column addition method. 
    Time complexity: O(n), Space complexity: O(n). 
    '''
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        ans = ListNode()
        curAns = ans
        nextPlusOne = False
        while (l1 != None or l2 != None or nextPlusOne):
            num1 = l1.val if (l1 != None) else 0
            num2 = l2.val if (l2 != None) else 0

            numSum = num1 + num2
            if (nextPlusOne):
                numSum += 1
            if (numSum < 10):
                curAns.val = numSum
                nextPlusOne = False
            else:
                curAns.val = numSum % 10
                nextPlusOne = True

            if (l1 != None):
                l1 = l1.next
            if (l2 != None):
                l2 = l2.next
            if (l1 != None or l2 != None or nextPlusOne): # there is a next number 
                curAns.next = ListNode()
                curAns = curAns.next
            
        return ans