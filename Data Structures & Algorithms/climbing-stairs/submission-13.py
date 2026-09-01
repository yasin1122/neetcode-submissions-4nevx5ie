from functools import cache
class Solution:
    @cache
    def climbStairs(self, n: int) -> int:
        i, j = 1, 1
        while n > 1:
            n -= 1
            i, j = i + j, i

        return i

        if n <= 2:
            return n
        
        return self.climbStairs(n - 1) + self.climbStairs(n - 2)