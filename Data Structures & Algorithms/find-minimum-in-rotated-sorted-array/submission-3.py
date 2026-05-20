class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r = 0,len(nums)-1
        minz=float('inf')
        while(l<=r):
            mid = l + (r-l)//2
            if nums[r] <= nums[mid]:
                l = mid + 1
            else:
                r = mid - 1

            minz = min(minz, nums[mid])

        return minz
            