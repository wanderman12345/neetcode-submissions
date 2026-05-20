class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
    
        def backtracking(i, s):
            if i == len(nums):
                res.append(s.copy())
                return 
        
            backtracking(i+1, s.copy())
            s.append(nums[i])
            backtracking(i+1, s.copy())

        backtracking(0, [])
        return res
