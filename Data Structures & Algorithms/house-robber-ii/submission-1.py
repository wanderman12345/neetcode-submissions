class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        dp0 = [-1] * (len(nums)-1)
        dp1 = [-1] * (len(nums)-1)
        one = nums.copy()
        two = nums.copy()
        one.pop()
        two.pop(0)
        print(two)
        def recur0(ind):
            if ind >= len(one):
                return 0
            if dp0[ind] != -1:
                return dp0[ind]

            take = one[ind]+recur0(ind+2)
            skip = recur0(ind+1)
            dp0[ind] = max(take, skip)
            return dp0[ind]

        def recur1(ind):
            if ind >= len(two):
                return 0
            if dp1[ind] != -1:
                return dp1[ind]

            take = two[ind]+recur1(ind+2)
            skip = recur1(ind+1)
            dp1[ind] = max(take, skip)
            return dp1[ind]

        

        return max(recur0(0), recur1(0))

    

        