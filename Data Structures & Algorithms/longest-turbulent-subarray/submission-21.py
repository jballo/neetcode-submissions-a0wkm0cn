class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        maxLen = 1
        L, R = 0, 1
        sign = None

        while R < len(arr):
            if arr[R-1] > arr[R] and sign != ">":
                maxLen = max(maxLen, R - L + 1)
                R += 1
                sign = ">"
            elif arr[R-1] < arr[R] and sign != "<":
                maxLen = max(maxLen, R - L + 1)
                R += 1
                sign = "<"
            else:
                R = R + 1 if arr[R-1] == arr[R] else R
                L = R - 1
                sign = None

        return maxLen