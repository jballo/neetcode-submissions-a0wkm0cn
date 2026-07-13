class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        button = [[], 
            [], 
            ['a', 'b', 'c'],
            ['d', 'e', 'f'],
            ['g', 'h', 'i'],
            ['j', 'k', 'l'],
            ['m', 'n', 'o'],
            ['p', 'q', 'r', 's'],
            ['t', 'u', 'v'],
            ['w', 'x', 'y', 'z']
        ]

        combos = []

        def helper(i, combo):
            if i >= len(digits):
                comboString = ''
                for letter in combo:
                    comboString += letter
                combos.append(comboString)
                return
            
            # print("i: ", i)
            # print("digits[i]: ", digits[i])
            row = int(digits[i])
            for j in range(0, len(button[row])):
                combo.append(button[row][j])
                helper(i + 1, combo)
                combo.pop()
        
        helper(0, [])
        print("combos: ", combos)
        
        return combos