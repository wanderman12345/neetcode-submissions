class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        orders = {}
        # go through entire list and split word into letters and store as key, value is the word itself
        for i in range(len(strs)):
            word = tuple(sorted(strs[i]))
            orders[word] = []

        for i in range(len(strs)):
            word = tuple(sorted(strs[i]))
            orders[word].append(strs[i])
        
        output = []
        # go through all values and put them in a list
        for eachVal in orders.values():
            output.append(eachVal)

        return output
        