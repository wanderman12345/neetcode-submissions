class Solution:
    def trap(self, height: List[int]) -> int:
        l = [0]
        largest = float('-inf')
        for i in range(len(height)-1):
            if height[i] > largest:
                largest = height[i]
            l.append(largest)
        r = [0]
        largest = float('-inf')
        for i in range(len(height)-1, 0,  -1):
            if height[i] > largest:
                largest = height[i]
            r.append(largest)
        r = r[::-1]
        total = 0
        for i in range(len(l)):
            minimum = min(l[i], r[i])
            if minimum - height[i] > 0:
                total += minimum - height[i]

        return total

            
         
        