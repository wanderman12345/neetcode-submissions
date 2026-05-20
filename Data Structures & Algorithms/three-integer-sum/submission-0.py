class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # less than three return empty
        if len(nums) < 3:
            return []
        # greater than or equal to three perform traversal and two sum on it
        else:
            unique = []
            out = []
            for i in range(len(nums)):
                target = -1 * nums[i]
                visited = set()
                indices = {}
                for j in range(i+1,len(nums)):
                    if target - nums[j] in visited:
                        k = indices[target-nums[j]]
                        r =  {nums[i],nums[k],nums[j]}
                        if r not in unique:
                            out.append([nums[i],nums[k],nums[j]])
                            unique.append(r)
                    else:
                        visited.add(nums[j])
                        indices[nums[j]] = j
        
        return out
                    

                        
                    

                    

