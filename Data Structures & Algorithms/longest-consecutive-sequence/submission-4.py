class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        check = 1
        maximum = 1
        if len(nums) == 0:
            return 0
        if len(nums) >= 2:
            for i in range(len(nums)-1):
                if nums[i+1] - nums[i] <= 1:
                    if nums[i+1] != nums[i]:
                        check += 1
                else:
                    check = 1

                maximum = max(maximum, check)
        
        return maximum
        

        