class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        '''here we have a hash map that keeps track of at most 2 items as that 
           is the largest we can get for anything n//3 count'''

        count = defaultdict(int)
        '''we add if less than 3. Once it reaches 3.
        we add then remove everything with just one frequency and decrement'''
        for n in nums:
            if len(count.values()) < 3:
                count[n] += 1
            else:
                newcount = defaultdict(int)
                for n, c in count.items():
                    if c > 1:
                        newcount[n] = c - 1
                count = newcount
        
        res = []
        for n in count:
            if nums.count(n) > len(nums) // 3:
                res.append(n)

        return res







