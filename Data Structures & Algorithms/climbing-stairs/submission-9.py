class Solution:
    def climbStairs(self, n: int) -> int:
        ar = [-1 for i in range(n+1)]
        ar[1] = 1
        if len(ar) > 2:
            ar[2] = 2

        def recur(s):
            if ar[s] != -1:
                return ar[s]
           
            ar[s] = recur(s-1) + recur(s-2)
            return ar[s]

        return recur(n)


        