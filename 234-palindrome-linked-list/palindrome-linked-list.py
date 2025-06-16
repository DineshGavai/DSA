# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow=head
        fast=head
        while fast != None and fast.next != None:
            fast=fast.next.next
            slow=slow.next

        prev=None
        while slow:
            next_node=slow.next
            slow.next=prev
            prev=slow
            slow=next_node
        
        first =head
        second = prev
        while second:
            if first.val != second.val:
                return False
            first=first.next
            second=second.next
        return True
