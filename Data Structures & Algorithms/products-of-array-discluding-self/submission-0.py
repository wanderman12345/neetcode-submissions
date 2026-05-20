class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        out = []
        left = [1]
        right = [1]

        # nums = [1,2,4,6]
        # left = [1, 1, 2, 8]
        for i in range(len(nums)-1):
            left.append(nums[i]*left[i])
        
        rightVar = 1
        for i in range(len(nums)-1,0,-1):
            rightVar = rightVar * nums[i]
            right.insert(0, rightVar)
        
        for j in range(len(nums)):
            out.append(left[j]*right[j])

        return out