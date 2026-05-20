class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        freq = defaultdict(int)
        for n in nums:
            if len(freq.values()) < 3:
                freq[n] += 1
            else:
                newcount = defaultdict(int)
                for n, c in freq.items():
                    if c > 1:
                        newcount[n] = c-1
                freq = newcount
        
        res = []
        for n in freq.keys():
            if nums.count(n) > len(nums) // 3:
                res.append(n)
        
        return res


                

        