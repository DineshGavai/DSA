# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def tree1(node):
            if not node:
                return []
            res=[]
            res+=tree1(node.left) 
            res+=tree1(node.right)

            if not node.left and not node.right:
                res.append(node.val)
            return res
        
        res1=tree1(root1)
        res2=tree1(root2)
        return res1==res2
