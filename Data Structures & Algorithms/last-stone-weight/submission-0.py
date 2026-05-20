class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # pop two elements if exist. compute and add back. 
        s = []
        for eachStone in stones:
            s.append(-1*eachStone)
        heapq.heapify(s)
        while len(s) > 1:
            one = -1*heapq.heappop(s)
            two = -1*heapq.heappop(s)

            # if one element return, if no element return 0
            if one > two:
                n = one-two
                heapq.heappush(s, -1*n)
        
        return -1*s[0] if s else 0
            
        