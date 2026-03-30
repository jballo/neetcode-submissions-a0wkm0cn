
class Solution:
    def isValid(self, s: str) -> bool:
        stor = {
            '(': ')',
            '{': '}',
            '[': ']'
        }
        # [']', ')']
        closedMatch = []

        for char in s:
            if char in stor:
                closedMatch.append(stor[char])
            else:
                if len(closedMatch) < 1 or (char != closedMatch[len(closedMatch) - 1]):
                    return False
                closedMatch.pop()
        
        if len(closedMatch) != 0:
            return False

        return True