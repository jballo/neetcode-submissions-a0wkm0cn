class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqCounter = {}


        for num in nums:
            if num not in freqCounter:
                freqCounter[num] = 0
            freqCounter[num] += 1

        # print(freqCounter)
        frequencies = []

        for _ in range(len(nums) + 1):
            frequencies.append([])

        for key in freqCounter:
            frequencies[freqCounter[key]].append(key)

        
        kFreq = []
        i = len(nums) - 1
        j = 0
        while len(kFreq) < k:
            # print("i: ", i)
            # print("j: ", j)
            if j >= len(frequencies[i]):
                j = 0
                i -= 1
                continue
            
            kFreq.append(frequencies[i][j])
            j += 1
        # print("kFreq: ", kFreq)
        return kFreq

        

        