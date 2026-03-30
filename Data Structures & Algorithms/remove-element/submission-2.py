class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l = 0
        # val = 2
        # l = 5
        # i = 7
        # [0,1,3,0,4,0,4,2]

        for i in range(0, len(nums)):
            if nums[i] != val:
                nums[l] = nums[i]
                l += 1

        return l
             