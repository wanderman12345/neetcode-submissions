class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
    # keep track of prefix sums and when they equal k count it in the total
        prefix = defaultdict(int)
        prefix[0] = 1
        count = 0
        total = 0
        for i in range(len(nums)):
            total += nums[i]
            if total-k in prefix.keys():
                count += prefix[total-k]
            prefix[total] += 1
        
        return count
            


        
        


    