# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        #understand
        # plan
        # base case: current node is empty - > return new Node with the desired value
        if not root:
            return TreeNode(val)
        
        # if the current root node is less than the desired value -> 
        if val < root.val:
            # root's left node the insert function call with root.left as the input and target value as input
            root.left = self.insertIntoBST(root.left, val)
            # else
        else:
            # root's right node the insert function call with the root's right as the input and the target node
            root.right = self.insertIntoBST(root.right, val)

        # return root
        return root

        # review
        
        # evaluate