class Solution:
    def isValid(self, s: str) -> bool:
        # store the opening brackets

        openBrackStor = []

        closeBrackMap = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        for char in s:
            if char not in closeBrackMap:
                openBrackStor.append(char)
            else:
                if openBrackStor and closeBrackMap[char] == openBrackStor[-1]:
                    openBrackStor.pop()
                else:
                    return False
        
        if openBrackStor:
            return False

        return True
        