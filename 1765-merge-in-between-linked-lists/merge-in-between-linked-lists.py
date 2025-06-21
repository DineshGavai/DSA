# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        left,right=list1,list1
        i=0
        while i < b:
            right=right.next
            i+=1
        i=0
        while i < a-1:
            left=left.next
            i+=1
        curr=list2
        while curr.next != None:
            curr=curr.next
        left.next=list2
        curr.next=right.next
        return list1
        

        