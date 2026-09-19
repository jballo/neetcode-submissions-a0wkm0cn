class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for word in strs:
            encoded += str(len(word)) + "#" + word

        print("encoded: ", encoded)
        return encoded

    def decode(self, s: str) -> List[str]:
        decoded = []
        i = 0
        j = 0
        # 
        while i < len(s):
            word = ""
            length = 0
            while j < len(s) and s[j] != "#":
                j += 1
            length = int(s[i:j])
            decodedStr = s[j+1: j+length+1]
            decoded.append(decodedStr)
            i = j + length + 1
            j = i

        return decoded