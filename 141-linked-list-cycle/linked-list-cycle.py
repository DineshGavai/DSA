# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        temp=set()
        curr=head
        while curr != None:
            
            if curr.next in temp:
                return True
            temp.add(curr.next)
            curr=curr.next
        return False
        
        