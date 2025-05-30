# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        
        max_elem=nums.index(max(nums))
        node=TreeNode(nums[max_elem])

        node.left=self.constructMaximumBinaryTree(nums[:max_elem])
        node.right=self.constructMaximumBinaryTree(nums[max_elem+1:])

        return node


       
