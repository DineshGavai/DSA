# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        freq=set()
        curr=head
        i=0
        while curr != None:
            if curr not in freq:
                freq.add(curr)
                curr=curr.next
            else:
                return curr
        
        return None
