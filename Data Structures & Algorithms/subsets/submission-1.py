class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
    
        s = []
        def backtracking(i):
            if i == len(nums):
                res.append(s.copy())
                return 
        
            backtracking(i+1)
            s.append(nums[i])
            backtracking(i+1)
            s.pop()

        backtracking(0)
        return res
