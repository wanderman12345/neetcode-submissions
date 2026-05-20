class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for eachOperation in operations:
            if eachOperation == "+":
                stack.append(int(stack[-1])+int(stack[-2]))
            elif not eachOperation.isalpha():
                stack.append(eachOperation)
            elif eachOperation == "C":
                stack.pop()
            elif eachOperation == "D":
                stack.append(int(stack[-1])*2)
        
        total = 0
        for i in stack:
            total += int(i)
        return total
        