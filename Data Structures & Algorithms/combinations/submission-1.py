class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        combos = []

        def helper(i, combo):
            if len(combo) == k:
                combos.append(combo.copy())
                return

            if i > n:
                return
            
            for j in range(i, n + 1):
                combo.append(j)
                helper(j + 1, combo)
                combo.pop()


        helper(1, [])
        return combos