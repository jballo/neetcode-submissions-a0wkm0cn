class TreeNode:
    def __init__(self, sum, l, r):
        self.sum = sum
        self.l = l
        self.r = r
        self.L = None
        self.R = None

class SegmentTree:
    
    def __init__(self, nums: List[int]):
        self.root = self.buildTree(nums, 0, len(nums)-1)

    def buildTree(self, nums, l, r):
        if l == r:
            return TreeNode(nums[l], l, r)
        
        m = l + ((r - l) // 2)

        leftRoot = self.buildTree(nums, l, m)
        rightRoot = self.buildTree(nums, m+1, r)
        root = TreeNode(leftRoot.sum + rightRoot.sum, l, r)
        root.L = leftRoot
        root.R = rightRoot
        return root
    
    def update(self, index: int, val: int) -> None:
        self.update_helper(self.root, index, val)

    def update_helper(self, root, index, val):
        if root.l == root.r:
            root.sum = val
            return
        
        m = root.l + ((root.r - root.l) // 2)
        
        if index <= m:
            self.update_helper(root.L, index, val)
        else:
            self.update_helper(root.R, index, val)

        root.sum = root.R.sum + root.L.sum
        return

    def query(self, L: int, R: int) -> int:
        return self.query_helper(self.root, L, R)

    # 0,2
    # [3, 4, 8, 9]
    # [3, 4] [8, 9]
    # [3],[4] [8] [9]

    def query_helper(self, root, l, r):
        if root.l >= l and root.r <= r:
            return root.sum
        elif root.r < l or root.l > r:
            return 0
        else:
            return self.query_helper(root.L, l, r) + self.query_helper(root.R, l, r)

