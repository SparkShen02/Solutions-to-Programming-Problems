# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        if not head:
            return
        vec = list()
        cur=head
        while cur:
            vec.append(cur)
            cur=cur.next
        i,j=0,len(vec)-1
        while i<j:
            vec[i].next=vec[j]
            i+=1
            if i==j:
                break
            vec[j].next=vec[i]
            j-=1
        vec[i].next=None
