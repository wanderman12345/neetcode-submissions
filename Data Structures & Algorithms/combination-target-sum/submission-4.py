class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        out = []
        unique = set()
        def backtrack(track, i):
            if sum(track) > target:
                return
            elif sum(track) == target:
                sortedTrack = sorted(track)
                if tuple(sortedTrack) not in unique:
                    out.append(sortedTrack.copy())
                    unique.add(tuple(sortedTrack))
                    return
            for j in range(len(nums)):
                track.append(nums[j])
                backtrack(track, i+1)
                track.pop()
        
        backtrack([],0)
        return out
        