class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        out = []
        track = {}
        for i, n in enumerate(nums):
                newPos = (i+k) % len(nums)
                track[newPos] = n
            
        for j in range(len(nums)):
            out.append(track[j])
        
        nums[:] = out



       
        




        