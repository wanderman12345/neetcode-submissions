class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = []
        for i in range(len(cost)):
            dp.append(-1)
        def recur(ind):
            if ind >= len(cost):
                return 0

            if dp[ind] != -1:
                return dp[ind]

            if ind == -1:
                return min(recur(ind+2), recur(ind+1))
            else:
                dp[ind] = cost[ind] + min(recur(ind+2), recur(ind+1))
                return dp[ind]

        return recur(-1)

        
        