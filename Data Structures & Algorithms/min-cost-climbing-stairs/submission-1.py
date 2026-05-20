class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        def recur(ind):
            if ind >= len(cost):
                return 0

            if ind == -1:
                return min(recur(ind+2), recur(ind+1))
            else:
                return cost[ind] + min(recur(ind+2), recur(ind+1))

        return recur(-1)

        
        