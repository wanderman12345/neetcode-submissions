class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        out = []
        def backtrack(n, i):
            if i == len(nums):
                out.append(n.copy())
                return
            n.append(nums[i])
            backtrack(n, i+1)
            n.pop()
            backtrack(n, i+1)
        
        backtrack([], 0)
        return out
        
                
