class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return self.binarySearch(nums, 0, len(nums) - 1, target)

    def binarySearch(self, nums, left, right, target):
        if right < left:
            return -1
        
        middle = (left + right) // 2

        if target > nums[middle]:
            return self.binarySearch(nums, middle + 1, right, target)
        elif target < nums[middle]:
            return self.binarySearch(nums, left, middle - 1, target)

        return middle