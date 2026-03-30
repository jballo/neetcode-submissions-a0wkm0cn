# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        states = []*len(pairs)

        for i in range(0, len(pairs)):
            l = i - 1
            r = i
            while l >= 0 and pairs[l].key > pairs[r].key:
                temp = pairs[l]
                pairs[l] = pairs[r]
                pairs[r] = temp
                l -= 1
                r -= 1
            states.append(pairs[:])
        
        return states