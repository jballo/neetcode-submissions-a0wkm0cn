class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1] * len(nums)
        postfix = [1] * len(nums)

        for i in range(len(nums)):
            if i == 0:
                prefix[i] = nums[i]
                continue
            
            prefix[i] = nums[i] * prefix[i - 1]
        
        # print("prefix: ", prefix)

        for j in range(len(nums) - 1, -1, -1):
            if j == len(nums) - 1:
                postfix[j] = nums[j]
                continue
            
            postfix[j] = nums[j] * postfix[j + 1]

        # print("postfix: ", postfix)
        

        prodArr = [0] * len(nums)

        for i in range(len(nums)):
            if i == 0:
                prodArr[i] = postfix[i + 1]
            elif i == len(nums) - 1:
                prodArr[i] = prefix[i - 1]
            else:
                prodArr[i] = prefix[i - 1] * postfix[i + 1]

        return prodArr