class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        combinations = []
        
        def helper(i, curCombo):
            if len(curCombo) == k:
                combinations.append(curCombo.copy())
                return

            if i > n:
                return

            curCombo.append(i)

            helper(i + 1, curCombo)
            curCombo.pop()
            helper(i + 1, curCombo)


        helper(1, [])

        return combinations