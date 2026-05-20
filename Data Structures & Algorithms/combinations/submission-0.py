class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # create a list from 1 - n
        nums = [i for i in range(1, n+1)]
        out = []
        unique = set()
        def backtrack(track, i):
            if len(track) == k:
                s = sorted(track)
                if tuple(s) not in unique:
                    unique.add(tuple(s))
                    out.append(s.copy())
                return
            if i >= len(nums):
                return
            
            track.append(nums[i])
            backtrack(track, i+1)
            track.pop()
            backtrack(track, i+1)


        backtrack([], 0)
        
        return out
            
        