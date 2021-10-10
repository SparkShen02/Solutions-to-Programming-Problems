def getNode(head,position):
        node=head
        for i in range(position-1):
            node=node.next
        return node
def printList(head):
    result=[]
    while head is not None:
        result.append(head.val)
        head=head.next
    print(result)
"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
class Solution:
    """
    @param head: ListNode head is the head of the linked list 
    @param m: An integer
    @param n: An integer
    @return: The head of the reversed ListNode
    """
    def reverseBetween(self, head, m, n):
        if m==n:
            return head
        if m is 1:
            start=head
        else:
            preNode=getNode(head,m-1)
            start=preNode.next
        end=getNode(head,n)
        postNode=end.next
        end.next=None
        
        pre=None
        cur=start
        nex=cur.next
        while nex is not None:
            cur.next=pre
            pre=cur
            cur=nex
            nex=cur.next
        cur.next=pre
        printList(end)
        
        start.next=postNode
        if m is 1:
            return end
        preNode.next=end
        return head