class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for a in asteroids:
            if a < 0:
                while stack and a < 0 and stack[-1] > 0:
                    if stack[-1] + a < 0:
                        stack.pop()
                    elif stack and stack[-1] + a == 0:
                        stack.pop()
                        a = 0
                    elif stack and stack[-1] + a > 0:
                        a = 0
            
            if a != 0:
                stack.append(a)
        
        return stack


                    
                


            

            