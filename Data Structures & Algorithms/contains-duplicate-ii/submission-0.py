class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        track = {}
        for i in range(len(nums)):
            if nums[i] not in track:
                track[nums[i]] = i
            else:
                if abs(track[nums[i]]-i) <= k:
                    return True
                track[nums[i]] = i
        
        return False
                    