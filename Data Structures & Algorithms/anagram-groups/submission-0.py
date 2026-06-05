class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        tableLists = {}
        for i in range(len(strs)):
            sortedWord = ''.join(sorted(strs[i]))
            if sortedWord not in tableLists:
                tableLists[sortedWord] = []
            tableLists[sortedWord].append(strs[i])

        
        groupings = []

        for key in tableLists:
            group = []
            for word in tableLists[key]:
                group.append(word)

            groupings.append(group)

        return groupings
        

        