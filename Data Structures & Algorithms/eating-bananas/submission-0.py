import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # [ 1 , 4, 3, 2, ]
        # 1 + 4 + 3 + 2 = 10 x
        # 2 + 2 + 2 + 1= 8 good

        # match: binary search pattern for the rate
        # find max pile
        maxPile = -1

        for pile in piles:
            if pile > maxPile:
                maxPile = pile

        # left starting rate 1 # 1
        left = 1
        # right -> max pile # 
        right = maxPile

        # set minRate to -1
        minRate = -1
        # binary search algorithm
        while left <= right:
            # rate is left + right / 2
            rate = (left + right) // 2
            sumHours = 0
            # ceil of pile/rate
            # add the ceil(pile/rate) to sumHours per pile
            for pile in piles:
                sumHours += math.ceil(pile / rate)

            # if sumHours less than h, update lowestRate to current rate
            if sumHours <= h:    
                # -> move right pointer down
                minRate = rate
                right = rate - 1
            else:
                # else
                # move left pointer up
                left = rate + 1

        # return lowestratee
        return minRate
        