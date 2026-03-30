class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        L, R = 0, (len(numbers) - 1)
        # [1, 2, 3, 4], target = 3
        #  L = 0
        # R = 3
        while L < R:
            sumNum = numbers[L] + numbers[R]
            if sumNum == target:
                return [L+1, R+1]
            elif sumNum > target:
                R -= 1
                continue
            else:
                L += 1

