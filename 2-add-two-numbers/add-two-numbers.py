# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        arr1=[]
        arr2=[]
        q1=deque([l1])
        q2=deque([l2])
        
        while q1 or q2:
            if q1:
                node1=q1.popleft()
                arr1.append(f"{node1.val}")
                if node1.next:
                    q1.append(node1.next)
            if q2:
                node2=q2.popleft()
                arr2.append(f"{node2.val}")
                if node2.next:
                    q2.append(node2.next)

        a=int("".join(reversed(arr1)))
        b=int("".join(reversed(arr2)))
        c=a+b
        
        arr = [int(digit) for digit in str(c)][::-1]
        res=ListNode(arr[0])
        current=res
        for i in range(1,len(arr)):
            current.next=ListNode(arr[i])
            current=current.next
        return res
        

        