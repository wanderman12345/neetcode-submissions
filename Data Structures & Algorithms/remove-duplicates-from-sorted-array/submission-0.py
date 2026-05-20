class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        duplicates = set()
        out = []
        for n in nums:
            if n not in duplicates:
                out.append(n)
            duplicates.add(n)
        nums[:] = out
        return len(nums)
