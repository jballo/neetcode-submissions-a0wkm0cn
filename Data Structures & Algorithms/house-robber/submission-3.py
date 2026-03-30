class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        hOne, hTwo = 0, nums[0]
        # 0, 2
        # 2, 9
        # 9, 10
        # 10, 12
        # 12, 13
        # 13, 18

        for i in range(len(nums) - 1):
            temp = hTwo
            hTwo = max((nums[i+1] + hOne), hTwo)
            hOne = temp
        return hTwo

        