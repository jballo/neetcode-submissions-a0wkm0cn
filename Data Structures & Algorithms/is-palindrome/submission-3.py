class Solution:
    def isPalindrome(self, s: str) -> bool:
        L = 0
        R = (len(s) - 1)
        

        while L < R:
            if not ((ord(s[L]) >= 65 and ord(s[L]) <= 122) or (ord(s[L]) >= 48 and ord(s[L]) <= 57)):
                L += 1
                continue
            elif not ((ord(s[R]) >= 65 and ord(s[R]) <= 122) or (ord(s[R]) >= 48 and ord(s[R]) <= 57)):
                R -= 1
                continue
            elif s[L].lower() != s[R].lower():
                return False
            L += 1
            R -= 1
        return True