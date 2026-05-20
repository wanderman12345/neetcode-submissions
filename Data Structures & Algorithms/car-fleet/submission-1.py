class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # (1,3) (3,3)
        # (0,10) (1,5) (4,3) (7,3)
        # Create an array with pos, time and sort. 
        fleet = 0
        times = []
        for i in range(len(position)):
            p, s = position[i], speed[i]
            t = (target - p) / s
            times.append((p,t))
        times.sort()

        # Then go backwards and count total fleet size.
        print(times)
        i = len(position)-1
        time = -1
        while i >= 0:
            if time < times[i][1]:
                fleet += 1
                time = times[i][1]
            i -= 1

        return fleet

        

