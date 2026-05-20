class Solution:
    def rob(self, nums: List[int]) -> int:          
        dp = [0 for i in range(len(nums))]
        dp[0] = nums[0]
        if len(nums) > 1:
            dp[1] = max(nums[0], nums[1])
        
        for j in range(2, len(nums)):
            rob1 = dp[j-2]
            rob2 = dp[j-1]
            dp[j] = max(rob1+nums[j], rob2)
            rob1 = rob2
            rob2 = dp[j]

        print(dp)
        return dp[-1]
            

        