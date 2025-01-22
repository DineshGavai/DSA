# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter=0
        def helper(node):
            if not node:
                return 0
            l_height=helper(node.left)
            r_height=helper(node.right)
        
            self.diameter=max(self.diameter,l_height+r_height)

            return 1+max(l_height,r_height)
        helper(root)
        return self.diameter