class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        for i in range(len(s)):
            if s[i] == "(" or s[i] == "{" or s[i] == "[":
                stack.append(s[i])
            elif s[i] == ")" or s[i] == "}" or s[i] =="]":
                if stack:
                    if s[i] == ")":
                        if stack[-1] == "(":
                            stack.pop() 
                        else:
                            return False
                    if s[i] == "]":
                        if stack[-1] == "[":
                            stack.pop() 
                        else:
                            return False
                    if s[i] == "}":
                        if stack[-1] == "{":
                            stack.pop() 
                        else:
                            return False
                else:
                    return False
        print(stack)
        return len(stack) == 0
            
            