class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # convert into set and check if lengths are the same. If not has duplicate
        return not len(set(nums)) == len(nums)
         