# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        k=0
        curr=head
        while curr != None:
            k+=1
            curr=curr.next
        if k == n:
            return head.next
        n=k-n

        first=head
        second=head.next
        i=1
        while i < n:
            print(second.val)
            first=first.next
            second=second.next
            i+=1
        first.next=second.next
        return head
        

