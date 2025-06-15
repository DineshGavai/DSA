# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        curr=head
        stack=[]
        temp=0
        while curr != None:
            if curr.val==0:
                if temp != 0:
                    stack.append(temp)
                temp=0
            temp+=curr.val
            curr=curr.next
        head=ListNode(stack[0])
        dummy=head
        head.next=None
        for i in range(1,len(stack)):

            new_node=ListNode(stack[i])
            head.next=new_node
            new_node.next=None
            head=new_node
        return dummy
        

            
