class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def mergeSort(l, r):
            i = 0
            j = 0
            out = []
            while i < len(l) and j < len(r):
                if l[i] < r[j]:
                    out.append(l[i])
                    i += 1
                else:
                    out.append(r[j])
                    j += 1
            
            while i < len(l):
                out.append(l[i])
                i += 1
            
            while j < len(r):
                out.append(r[j])
                j += 1
            
            return out

        if len(nums) <= 1:
            return nums
        m = len(nums) // 2
        left = self.sortArray(nums[:m])
        right = self.sortArray(nums[m:])
        return mergeSort(left, right)

    