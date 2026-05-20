class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1 = 0
        rob2 = 0
        if len(nums) == 1:
            return nums[0]
        for i in range(len(nums)-1):
            temp = max(rob2, rob1 + nums[i])
            rob1 = rob2
            rob2 = temp
        m1  = rob2

        rob1 = 0
        rob2 = 0
        for i in range(1, len(nums)):
            temp = max(rob2, rob1 + nums[i])
            rob1 = rob2
            rob2 = temp

        m2 = rob2
        return max(m1, m2)
        
        