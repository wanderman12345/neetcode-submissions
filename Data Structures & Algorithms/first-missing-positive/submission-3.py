class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        if max(nums) <= 0:
            return 1
        if min(nums) > 1:
            return 1
        nums = set(nums)
        for n in range(min(nums), max(nums)):
            if n not in nums and n > 0:
                return n
        
        return max(nums)+1