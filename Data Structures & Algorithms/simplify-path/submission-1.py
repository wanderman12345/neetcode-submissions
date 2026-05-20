class Solution:
    def simplifyPath(self, path: str) -> str:
        # add directories to the stack based on filename and pop if you see ...
        stack = []
        p = path.split("/")
        print(p)
        for e in p:
            if e == "..":
                if stack:
                    stack.pop()
            elif e == ".":
                continue
            elif e == '':
                continue 
            else:
                stack.append(e)
        out = "/"
        for i in range(len(stack)):
            out += stack[i]
            if i != len(stack)-1:
                out += "/"
        
        return out
        
        



        