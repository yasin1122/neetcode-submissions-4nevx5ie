import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # piles contains # of bananas in each pile
        # h = # of hours to eat em all
        # k = bananas per hour rate
        # max = max(piles), min = 1

        left, right = 1, max(piles)
        res = right

        while left <= right:
            k = (left + right) // 2
            hours = 0

            for pile in piles:
                hours += math.ceil(pile / k)

            if hours <= h:
                res = k
                right = k - 1
            else:
                left = k + 1

        return res
