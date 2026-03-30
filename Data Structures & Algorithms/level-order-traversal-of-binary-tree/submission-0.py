# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = []
        levels = []
        if root:
            queue.append(root)
        
        # queue:
        # <- [4,5,6,7] <-
        # levels: [[1], [2,3]]
        # arr = [4, 5, 6, 7]


        while len(queue) > 0:
            arr = []
            nodeCnt = len(queue) # 4
            for i in range(nodeCnt):
                node = queue.pop(0) 
                arr.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            levels.append(arr)
        return levels