# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def divisor(a,b):
            minimum=min(a,b)
            for i in range(minimum,-1,-1):
                if a%i==0 and b%i==0:
                    return i
        first=head
        second=head.next
        while second != None:
            val=divisor(first.val,second.val)
            new_node=ListNode(val)
            new_node.next=second
            first.next=new_node
            first=second
            second=second.next
        return head
            

