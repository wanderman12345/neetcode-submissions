class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = s.split(" ")
        newWords = []
        for eachWord in words:
            if eachWord != "":
                newWords.append(eachWord)
        return len(newWords[-1])