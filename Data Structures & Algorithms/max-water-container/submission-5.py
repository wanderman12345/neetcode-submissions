class Solution:
    def maxArea(self, heights: List[int]) -> int:
        def vol(left, right):
            width = right-left
            height = min(heights[right], heights[left])
            return width*height

        val = 0
        volume = 0
        l = 0 
        r = len(heights)-1
        while l <= r:
            volume = vol(l,r)
            val = max(val, volume)
            if heights[l] > heights[r]:
                r -=1
            else:
                l += 1

        return val