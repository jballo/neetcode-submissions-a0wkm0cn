class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixArr = [0] * len(nums)
        suffixArr = [0] * len(nums)

        prefix = 1
        for i in range(len(nums)):
            prefix *= nums[i]
            prefixArr[i] = prefix

        suffix = 1
        for i in range(len(nums) - 1, -1, -1):
            suffix *= nums[i]
            suffixArr[i] = suffix

        print(prefixArr)

        
        for i in range(len(nums)):
            leftProduct = prefixArr[i - 1] if i - 1 >= 0 else 1
            rightProduct = suffixArr[i + 1] if i + 1 < len(nums) else 1
            nums[i] = leftProduct * rightProduct

        return nums


        