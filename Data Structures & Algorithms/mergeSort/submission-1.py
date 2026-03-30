# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        if len(pairs) <= 1:
            return pairs

        return self.mergeSortHelper(pairs, 0, len(pairs) - 1)

    def mergeSortHelper(self, pairs, start, end):
        if (end - start + 1 == 1):
            return pairs

        middle = (end + start) // 2
        # part left side
        self.mergeSortHelper(pairs, start, middle)
        # part right side
        self.mergeSortHelper(pairs, middle + 1, end)

        # merge both sides
        self.merge(pairs, start, middle, end)
        
        return pairs

    def merge(self, pairs, start, middle, end):
        # create left side copy
        leftCopy = pairs[start:middle+1]
        # create right side copy
        rightCopy = pairs[middle+1:end+1]

        # left copy index
        lPtr = 0
        # right copy index
        rPtr = 0
        # pairs pointer
        i = start

        # condition to compair left and right copy values
        while i < len(pairs) and lPtr < len(leftCopy) and rPtr < len(rightCopy):
            if leftCopy[lPtr].key <= rightCopy[rPtr].key:
                pairs[i] = leftCopy[lPtr]
                lPtr += 1
            else:
                pairs[i] = rightCopy[rPtr]
                rPtr += 1
            i += 1

        # iterate through remaining values on either copy
        while i < len(pairs) and lPtr < len(leftCopy):
            pairs[i] = leftCopy[lPtr]
            lPtr += 1
            i += 1
        
        while i < len(pairs) and rPtr < len(rightCopy):
            pairs[i] = rightCopy[rPtr]
            rPtr += 1
            i += 1
        


