class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # calculate all points to origin
        # create min Heap and return k elements
        dist = []
        for x,y in points:
            d = math.sqrt(x**2+y**2)
            heapq.heappush(dist, (-d, (x,y)))
            if len(dist) > k:
                heapq.heappop(dist)

        out = []
        for i in range(k):
            x,y = heapq.heappop(dist)[1]
            out.append([x,y])

        return out



        