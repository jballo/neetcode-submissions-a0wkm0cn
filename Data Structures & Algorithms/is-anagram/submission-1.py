class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        storA = [0] * 26
        storB = [0] * 26
        for char in s:
            index = ord(char) - ord('a')
            storA[index] += 1
        
        for char in t:
            index = ord(char) - ord('a')
            storB[index] += 1

        for i in range(26):
            if storA[i] != storB[i]:
                return False
    
        return True