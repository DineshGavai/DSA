# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        self.index = 0
        
        def helper(bound):
            if self.index == len(preorder) or preorder[self.index] > bound:
                return None
            
            root_val = preorder[self.index]
            self.index += 1
            root = TreeNode(root_val)
            
            root.left = helper(root_val)
            root.right = helper(bound)
            
            return root
        
        return helper(float('inf'))