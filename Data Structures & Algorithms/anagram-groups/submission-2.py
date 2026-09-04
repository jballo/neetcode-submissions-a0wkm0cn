class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groupings = {}


        for word in strs:
            rep = [0] * 26
            for c in word:
                index = ord(c) - ord('a')
                rep[index] += 1

            stringRep = ''
            for i in range(26):
                stringRep = stringRep + '#' + str(rep[i])
            
            if stringRep not in groupings:
                groupings[stringRep] = []

            groupings[stringRep].append(word)
        

        groups = []

        for key in groupings:
            group = []

            for word in groupings[key]:
                group.append(word)

            groups.append(group)
        return groups