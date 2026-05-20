class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # go through nums and store frequencies in dict
        C = Counter(nums)
        l = sorted(list(C.items()), key = lambda x : x[1], reverse= True)
        out = []
        for i in range(k):
            out.append(l[i][0])
        return out
        