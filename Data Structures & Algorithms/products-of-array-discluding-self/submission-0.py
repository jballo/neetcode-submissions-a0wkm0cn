class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prodOfAll = 1
        zeroCount = 0
        
        for i in range(len(nums)):
            prodOfAll = prodOfAll * nums[i] if nums[i] != 0 else prodOfAll
            zeroCount = zeroCount + 1 if nums[i] == 0 else zeroCount


        for i in range(len(nums)):
            if zeroCount >= 2:
                nums[i] = 0
            elif zeroCount == 1:
                nums[i] = prodOfAll if nums[i] == 0 else 0
            else:
                nums[i] = int(prodOfAll / nums[i])
        return nums