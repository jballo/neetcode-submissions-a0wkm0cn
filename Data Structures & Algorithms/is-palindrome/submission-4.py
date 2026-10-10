class Solution:
    def isAlphanumeric(self, char):
        alpha = set(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6','7', '8', '9'])
        return char in alpha

    def isPalindrome(self, s: str) -> bool:
        
        lPtr = 0
        rPtr = len(s) - 1


        while lPtr < rPtr:
            closestlPtr = lPtr
            closestrPtr = rPtr
            while closestlPtr < closestrPtr and not self.isAlphanumeric(s[closestlPtr].lower()):
                closestlPtr += 1
            
            while closestlPtr < closestrPtr and not self.isAlphanumeric(s[closestrPtr].lower()):
                closestrPtr -= 1
            
            if closestlPtr < closestrPtr and s[closestlPtr].lower() != s[closestrPtr].lower():
                return False

            lPtr = closestlPtr + 1
            rPtr = closestrPtr - 1


        return True

            