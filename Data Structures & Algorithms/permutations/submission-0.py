class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        out = []
        def backtrack(track, i):
            if len(track) == len(nums):
                out.append(track.copy())
                return

            for j in range(len(nums)):
                if nums[j] not in track:
                    track.append(nums[j])
                    backtrack(track, i+1)
                    track.pop()

        backtrack([], 0)
        return out



        