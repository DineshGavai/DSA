# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        temp1=list1
        temp2=list2
        dummy=ListNode()
        res=dummy

        while temp1 is not None and temp2 is not None:
            if temp1.val <= temp2.val:
                res.next=temp1
                temp1=temp1.next
            else:
                res.next=temp2
                temp2=temp2.next
            res=res.next
        
        if temp1 is not None:
            res.next=temp1
        if temp2 is not None:
            res.next=temp2
            
        return dummy.next

            