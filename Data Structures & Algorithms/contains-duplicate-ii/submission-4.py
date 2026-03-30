class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        cache = {} # {2: 0, 1: 1}
        # [2, 1, 2], k = 3
        # 1

        for i in range(0, len(nums)):
            if nums[i] not in cache:
                cache[nums[i]] = i
                continue

            if abs(i - cache[nums[i]]) <= k:
                return True
            
            cache[nums[i]] = i
            
        return False