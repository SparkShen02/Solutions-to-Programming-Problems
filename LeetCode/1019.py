# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    '''
    Traverse the linked list and use a stack to store the nodes (index, value) that haven't reached a larger node.
    Time complexity: O(n), Space complexity: O(n).
    '''
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        ans = []
        s = []
        i, cur = 0, head
        while cur != None:
            ans.append(0)
            while len(s) != 0 and cur.val > s[-1][1]:
                ans[s[-1][0]] = cur.val
                s.pop()
            s.append((i, cur.val))
            
            i += 1
            cur = cur.next
        return ans