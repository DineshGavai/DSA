# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def invert(node):
            if not node:
                return
            current=node
            temp_left= current.left if current.left else None
            temp_right= current.right if current.right else None
            current.left=temp_right
            current.right=temp_left
            invert(current.left)
            invert(current.right)
        invert(root)
        return root

