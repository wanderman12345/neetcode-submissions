class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return nums[0]
        elif len(nums) == 2:
            return max(nums)
        else:
            mem = []
            mem.append(nums[0])
            mem.append(max(nums[0], nums[1]))
            for i in range(2, len(nums)):
                mem.append(max(nums[i] + mem[i-2], mem[i-1]))
            return mem[-1]

        

        