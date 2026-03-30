# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        queue = []
        vals = []

        if root:
            queue.append(root) 


        while len(queue) > 0:
            rightMostVal = None
            nodeCnt = len(queue)
            for i in range(nodeCnt):
                parent = queue.pop(0)
                rightMostVal = parent.val
                if parent.left:
                    queue.append(parent.left)
                if parent.right:
                    queue.append(parent.right)
            vals.append(rightMostVal)

        return vals
