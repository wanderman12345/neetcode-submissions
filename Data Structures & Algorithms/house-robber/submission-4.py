class Solution:
    def rob(self, nums: List[int]) -> int:
        ar = [-1 for i in range(len(nums))]
        def recur (i, nums):
            if i >= len(nums):
                return 0
            else:
                if ar[i] != -1:
                    return ar[i]

                cur = recur(i+1, nums)
                n = recur(i+2, nums) + nums[i]
                if cur > n:
                    ar[i] = cur
                    return ar[i]
                else:
                    ar[i] = n
                    return ar[i]
            
        return recur(0, nums)

        



        