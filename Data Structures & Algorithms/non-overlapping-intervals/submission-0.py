class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        out = [intervals[0]]
        # [1,2]
        # [1,4]
        count = 0
        for i in range(1, len(intervals)):
            if out[-1][1] > intervals[i][0]:
                count += 1
                out[-1][1] = min(intervals[i][1], out[-1][1])
            else:
                out.append(intervals[i])
        
        return count

            

            

    







        





