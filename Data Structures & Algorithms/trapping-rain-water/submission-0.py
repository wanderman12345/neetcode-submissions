class Solution:
    def trap(self, height: List[int]) -> int:
        l = []
        r = []
        if len(height) == 1:
            return 0
        
        maxLeft = height[0]
        for eachHeight in height:
            l.append(maxLeft)
            maxLeft = max(eachHeight, maxLeft)

        maxRight = height[-1]
        for j in range(len(height)-1,-1,-1):
            r.append(maxRight)
            maxRight = max(maxRight, height[j])

        r = r[::-1]

        out = 0
        for i in range(len(height)):
            minimum = min(l[i], r[i])
            total = minimum - height[i]
            if total > 0:
                out += total 
        
        return out
    


        