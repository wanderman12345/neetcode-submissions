class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        out = []
        def BackTracking(totalList, i):
            total = sum(totalList)
            if total > target or i == len(nums)+1:
                return
            if total == target:
                if totalList not in out:
                    out.append(totalList.copy())
            
            if i < len(nums):
                BackTracking(totalList, i+1)
                totalList.append(nums[i])
                BackTracking(totalList, i)
                BackTracking(totalList, i+1)
                totalList.pop()
                
        BackTracking([], 0)
        return out
            
