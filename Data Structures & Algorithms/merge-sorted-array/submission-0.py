class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1copy = nums1.copy()
        one = 0
        two = 0
        i = 0
        while one < m and two < n:
            if nums1copy[one] < nums2[two]:
                nums1[i] = nums1copy[one]
                one += 1
            else:
                nums1[i] = nums2[two]
                two += 1
            i += 1

        while one < m:
            nums1[i] = nums1copy[one]
            one += 1
            i += 1

        while two < n:
            nums1[i] = nums2[two]
            two += 1
            i += 1

    



        