# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        preOrderArr = [] #[1, 2, 4, 5, 3, 6, 7]
        stack = [] #bottom [] top

        while root or stack:
            if root:
                preOrderArr.append(root.val)
                if root.right:
                    stack.append(root.right)
                root = root.left
            else:
                root = stack.pop()


        return preOrderArr
    