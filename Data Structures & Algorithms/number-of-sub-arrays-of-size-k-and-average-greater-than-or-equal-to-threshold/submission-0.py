class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        subArrCnt = 0 # 2
        curTotal = 0 # 15
        # [2,2,2,2,5,5,5,8], k = 3,  threshold = 4
        # 

        for i in range(k):
            curTotal += arr[i]
        
        if curTotal / k >= threshold:
            subArrCnt += 1

        for i in range(k, len(arr)):
            curTotal -= arr[i - k]
            curTotal += arr[i]
            if curTotal / k >= threshold:
                subArrCnt += 1
            
        return subArrCnt
