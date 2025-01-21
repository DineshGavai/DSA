# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return 
        q=deque()
        q.append(root)
        temp_set=set()
        while q:
            node=q.popleft()
            temp_set.add(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        return True if len(temp_set) == 1 else False


        
