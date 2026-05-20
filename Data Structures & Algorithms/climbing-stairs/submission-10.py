class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        bu = [0 for i in range(n+1)]
        bu[1] = 1
        bu[2] = 2
        for i in range(3, n+1):
            bu[i] = bu[i-1] + bu[i-2]
        
        return bu[n]


        