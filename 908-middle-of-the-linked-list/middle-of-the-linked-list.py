# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cnt=0
        curr=head
        while curr != None:
            curr=curr.next
            cnt+=1
        
        temp=head
        for i in range(0,cnt//2):
            temp=temp.next
        return temp
        


