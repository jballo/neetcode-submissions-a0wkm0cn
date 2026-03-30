# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        arr = []
        self.binarySortHelper(arr, root)
        return arr[k - 1]

    def binarySortHelper(self, arr, root):
        if not root:
            return
        
        self.binarySortHelper(arr, root.left)
        arr.append(root.val)
        self.binarySortHelper(arr, root.right)