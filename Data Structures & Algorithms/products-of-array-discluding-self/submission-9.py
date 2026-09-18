class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1] * len(nums)
        postfix = [1] * len(nums)
        prePtr = 0
        postPtr = len(nums) - 1

        for i in range(len(nums)):
            if i == 0:
                prefix[prePtr] = nums[prePtr]
                postfix[postPtr] = nums[postPtr]
            else:
                prefix[prePtr] = prefix[prePtr - 1] * nums[prePtr]
                postfix[postPtr] = postfix[postPtr + 1] * nums[postPtr]

            prePtr += 1
            postPtr -= 1
        

        prodArr = [0] * len(nums)

        for i in range(len(nums)):
            if i == 0:
                prodArr[i] = postfix[i + 1]
            elif i == len(nums) - 1:
                prodArr[i] = prefix[i - 1]
            else:
                prodArr[i] = prefix[i - 1] * postfix[i + 1]

        return prodArr