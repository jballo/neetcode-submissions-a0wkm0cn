# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        postArr = []
        stack = [root]
        visitedStack = [False]

        while stack:
            root, visited = stack.pop(), visitedStack.pop()
            if root:
                if visited:
                    postArr.append(root.val)
                else:
                    stack.append(root)
                    visitedStack.append(True)
                    stack.append(root.right)
                    visitedStack.append(False)
                    stack.append(root.left)
                    visitedStack.append(False)
        
        return postArr