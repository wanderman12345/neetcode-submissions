class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = []
        self.k = k
        for i in range(len(nums)):
            if len(self.heap) < self.k:
                heapq.heappush(self.heap, nums[i])
            else:
                if nums[i] > self.heap[0]:
                    heapq.heapreplace(self.heap, nums[i])
        
    def add(self, val: int) -> int:
        if len(self.heap) == self.k:
            if val > self.heap[0]:
                heapq.heapreplace(self.heap, val)
        else:
            heapq.heappush(self.heap, val)
        
        return self.heap[0]

        
