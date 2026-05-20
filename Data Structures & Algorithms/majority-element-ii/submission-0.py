class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        counter = Counter(nums)
        out = []
        for num,value in counter.items():
            if value > len(nums)/3:
                out.append(num)
    
        return out
        