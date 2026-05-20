class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        out = []
        nums.sort()
        uniqueSet = set()
        for i in range(len(nums)-2):
            target = -1*nums[i]
            track = {}
            if nums[i] > 0:
                break
            for j in range(i+1, len(nums)):
                if target - nums[j] in track.keys():
                    s = [nums[i], nums[j], target - nums[j]]
                    if nums[i] + nums[j] + target - nums[j] >  0:
                        break
                    s.sort()
                    if tuple(s) not in uniqueSet:
                        uniqueSet.add(tuple(s))
                        out.append(s)

                if nums[j] not in track.keys():
                    track[nums[j]] = j

        return out