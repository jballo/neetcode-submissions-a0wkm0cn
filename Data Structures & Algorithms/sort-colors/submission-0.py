class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # nums = [ 0, 1, 1, 2 ]
        # [1, 2, 1]
        # numsPtr = 4

        colorCnt = [0, 0, 0]

        for i in range (0, len(nums)):
            colorCnt[nums[i]] += 1
        
        numsPtr = 0
        for i in range(0, len(colorCnt)):
            for j in range(0, colorCnt[i]):
                nums[numsPtr] = i
                numsPtr += 1
        
        return nums
