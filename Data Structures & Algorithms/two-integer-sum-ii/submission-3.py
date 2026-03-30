class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        L, R = 0, (len(numbers) - 1)
        # [1, 2, 3, 4], target = 3
        #  L = 0
        # R = 3
        sumNum = None
        while L < R and sumNum != target:
            sumNum = numbers[L] + numbers[R]
            if sumNum > target:
                R-= 1
            elif sumNum < target:
                L += 1

        return [L+1, R+1]

