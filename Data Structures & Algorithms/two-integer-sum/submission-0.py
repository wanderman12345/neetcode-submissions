class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        Visited = set()
        indices = {}
        for i in range(len(nums)):
            if target-nums[i] in Visited:
                return [indices[target-nums[i]], i]
            else:
                Visited.add(nums[i])
                indices[nums[i]] = i        
        
        