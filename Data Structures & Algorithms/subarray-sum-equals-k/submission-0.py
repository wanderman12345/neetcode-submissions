class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        freq = defaultdict(int)
        freq[0] = 1
        count = 0
        total = 0
        for n in nums:
            total += n
            diff = total - k
            count += freq[diff]
            freq[total] += 1
        
        return count

        