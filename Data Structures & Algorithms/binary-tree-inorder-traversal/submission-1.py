# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        arr = []
        self.traversalHelper(arr, root)
        return arr

    def traversalHelper(self, arr, root):
        if not root:
            return
        
        self.traversalHelper(arr, root.left)
        arr.append(root.val)
        self.traversalHelper(arr, root.right)