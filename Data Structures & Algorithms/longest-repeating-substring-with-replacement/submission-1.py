class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # we can have an empty string?
        maxLen = 0
        L, R = 0, 0
        frequency = [0] * 26
            
        while R < len(s):
            frequency[ord(s[R]) - ord("A")] += 1
            mostFrequentCharIndex = 0
            for i in range(len(frequency)):
                if frequency[i] >= frequency[mostFrequentCharIndex]:
                    mostFrequentCharIndex = i
            # window - mostFreuentChar
            swaps = (R - L + 1) - frequency[mostFrequentCharIndex]
            while swaps > k:
                frequency[ord(s[L]) - ord("A")] -= 1
                L += 1
                mostFrequentCharIndex = 0
                for i in range(len(frequency)):
                    if frequency[i] >= frequency[mostFrequentCharIndex]:
                        mostFrequentCharIndex = i
                swaps = (R - L + 1) - frequency[mostFrequentCharIndex]
            maxLen = max(maxLen, R - L + 1)

            R += 1

        return maxLen
                
            