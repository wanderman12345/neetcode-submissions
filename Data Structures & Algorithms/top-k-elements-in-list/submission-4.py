class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        CountFrequency = Counter(nums)
       # {1: 1, 2: 2, 3 : 3}
        SortedPair  = sorted(CountFrequency.items(), key = lambda x: x[1], reverse = True)
        count = 0
        out = []
        for eachKey, eachVal in SortedPair:
            if count == k:
                break
            out.append(eachKey)
            count += 1
        return out
        