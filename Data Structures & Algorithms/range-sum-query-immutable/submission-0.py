class NumArray:

    def __init__(self, nums: List[int]):
        self.prefixSums = []
        tot = 0
        for num in nums:
            tot += num
            self.prefixSums.append(tot)

    def sumRange(self, left: int, right: int) -> int:
        sumToLeft = self.prefixSums[right]
        subTractBy = self.prefixSums[left - 1] if left > 0 else 0
        return (sumToLeft - subTractBy)


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)