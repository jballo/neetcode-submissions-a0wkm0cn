class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        maxLen = 0  # 3
        cache = set() # { x, y, z}
        L = 0 # 1
        # zxysy

        # s = "zxyzxyz"
        # R = 3


        for R in range(len(s)):
            if s[R] not in cache:
                cache.add(s[R])
                maxLen = max(maxLen, R - L + 1)
                continue
            while s[R] in cache:
                cache.remove(s[L])
                L += 1
            cache.add(s[R]) 
        
        return maxLen
            
                 

