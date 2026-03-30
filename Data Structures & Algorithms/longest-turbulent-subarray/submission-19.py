class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        # what is the expected time/space complexity?
        # minimum size of arr?
        # is a size of 1 an acceptable turbulent subarray?
        # can we assume an empty subarray is not a valid turbulent subarray?


        # slididng window
        maxLen = 1
        L = 0
        R = 1
        sign = None

        while R < len(arr):
            if arr[R - 1] > arr[R] and sign != ">":
                maxLen = max(maxLen, R - L + 1)
                sign = ">" 
                R += 1
            elif arr[R - 1] < arr[R] and sign != "<":
                maxLen = max(maxLen, R - L + 1)
                sign = "<"
                R += 1
            else:
                R = (R+1) if arr[R-1] == arr[R] else R
                L = R - 1
                sign = None

        return maxLen