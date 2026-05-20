class Solution:
    def isPalindrome(self, s: str) -> bool:
        newWord = ""
        for eachChar in s:
            if eachChar.isalnum():
                newWord += eachChar.lower()
        
        reversedWord = newWord[::-1]
        return reversedWord == newWord

        