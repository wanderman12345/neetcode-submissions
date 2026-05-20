class Solution:
    def maxArea(self, heights: List[int]) -> int:
        volume = 0
        for i in range(len(heights)):
            for j in range(i+1, len(heights)):
                width = j-i
                height = min(heights[j], heights[i])
                calc = width*height
                volume = max(volume, calc)
        
        return volume
        