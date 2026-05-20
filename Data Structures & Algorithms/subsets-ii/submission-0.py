class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        out = []
        def backtrack(i, sub):
            if i >= len(nums):
                s = sorted(sub)
                if s not in out:
                    out.append(s.copy())
                    return
            else:
                sub.append(nums[i])
                backtrack(i+1, sub)
                sub.pop()
                backtrack(i+1, sub)

        backtrack(0, [])
        return out
