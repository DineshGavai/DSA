# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        nodes=[]
        def inorder(node):
            if node==None:
                return
            inorder(node.left)
            nodes.append(node.val)
            inorder(node.right)
        inorder(root)
        
        new_root=TreeNode(nodes[0])
        current=new_root
        for i in range(1,len(nodes)):
            new_node=TreeNode(nodes[i])
            current.right=new_node
            current=new_node
        return new_root