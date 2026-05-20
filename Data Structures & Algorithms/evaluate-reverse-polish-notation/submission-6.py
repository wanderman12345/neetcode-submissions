class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # once we see an operation complete operation and push val to stack
        stack = []
        for t in tokens:
            if t == "+":
                a = stack.pop()
                b = stack.pop()
                s = int(a) + int(b)
                stack.append(str(s))
            elif t == "*":
                c = stack.pop()
                d = stack.pop()
                s = int(c) * int(d)
                stack.append(str(s))
            elif t == "-":
                a = stack.pop()
                b = stack.pop()
                s = int(b) - int(a)
                stack.append(str(s))
            elif t == "/":
                a = stack.pop()
                b = stack.pop()
                s = int(int(b) / int(a))
                stack.append(str(s))
            else:
                stack.append(t)
        
        return int(stack[-1])
            


        
        