# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        vals = []
        self.helper(vals, root)
        return vals
    
    def helper(self, vals, root):
        if not root:
            return
        
        self.helper(vals, root.left)
        vals.append(root.val)
        self.helper(vals, root.right)
        return