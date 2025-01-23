# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        res=float('inf')
        arr=[]
        def helper(node):
            if not node:
                return
            helper(node.left)
            arr.append(node.val)
            helper(node.right)
        helper(root)
        print(arr)
        for i in range(len(arr)-1):
            val=arr[i+1]-arr[i]
            res=min(res,val)
        return res


