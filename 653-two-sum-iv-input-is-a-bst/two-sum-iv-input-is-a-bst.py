# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        # if not root:
        #     return []
        arr=[]
        
        q=deque([root])
        while q:
            n=q.popleft()
            arr.append(n.val)
            if n.left:
                q.append(n.left)
            if n.right:
                q.append(n.right)

        for i in range(len(arr)):
            for j in range(i+1,len(arr)):
                if arr[i]+arr[j]==k:
                    return True
        return False

       
            