class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(left, right):
            i, j = 0, 0
            out = []
            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    out.append(left[i])
                    i += 1
                else:
                    out.append(right[j])
                    j += 1
            out.extend(left[i:])
            out.extend(right[j:])
            return out

        if len(nums) <= 1:
            return nums
        
        m = len(nums) // 2
        left = self.sortArray(nums[:m])
        right = self.sortArray(nums[m:])
        return merge(left, right)


        