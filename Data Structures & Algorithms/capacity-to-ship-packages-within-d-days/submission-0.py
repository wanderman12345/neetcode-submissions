class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l = max(weights)
        r = sum(weights)
        res = r
        while l <= r:
            m = (l+r)//2
            # check to see if this result works
            print(m)
            d = 1
            t = 0
            for i in range(len(weights)):
                if t + weights[i] > m:
                    d += 1
                    t = 0
                t += weights[i]

            if d <= days:
                res = m
                r = m - 1
            else:
                l = m + 1
        
        return res






        