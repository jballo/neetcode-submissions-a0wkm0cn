# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        if len(pairs) <= 1:
            return pairs

        self.quickSortHelper(pairs, 0, len(pairs) - 1)
        return pairs

    def quickSortHelper(self, pairs, left, right):
        if right <= left:
            return

        lPtr = left
        pivot = pairs[right]

        for i in range(left, right):
            if pairs[i].key < pivot.key:
                temp = pairs[i]
                pairs[i] = pairs[lPtr]
                pairs[lPtr] = temp
                lPtr += 1
        
        pairs[right] = pairs[lPtr]
        pairs[lPtr] = pivot

        self.quickSortHelper(pairs, left, lPtr -1)
        self.quickSortHelper(pairs, lPtr + 1, right)

