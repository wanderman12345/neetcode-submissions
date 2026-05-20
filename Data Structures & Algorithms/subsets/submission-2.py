class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        out = []
        def backtrack(track, i):
            if i == len(nums):
                out.append(track.copy())
                return 
            track.append(nums[i])
            backtrack(track, i+1)
            track.pop()
            backtrack(track, i+1)
        backtrack([], 0)
        return out

        