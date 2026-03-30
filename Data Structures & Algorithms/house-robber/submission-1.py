class Solution:
    def rob(self, nums: List[int]) -> int:
        houseOne, houseTwo = 0, 0
        # [2,9,8,3,6]
        for num in nums:
            temp = max(num + houseOne, houseTwo)
            houseOne = houseTwo
            houseTwo = temp

        return houseTwo
            