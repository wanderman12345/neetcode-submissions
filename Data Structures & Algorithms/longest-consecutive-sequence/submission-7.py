class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # nums = [2,3,4,4,5,10,20]
        nums.sort()
        if len(nums) < 2:
            return len(nums)
        print(nums)
        count = 1
        prev = 0
        cur = 1
        localCount = 1
        for i in range(1,len(nums)):
            if nums[cur] - nums[prev] == 1:
                localCount += 1
            elif nums[cur] - nums[prev] > 1:
                localCount = 1
            count = max(localCount, count)
            prev += 1
            cur += 1

        return count
            


        

        