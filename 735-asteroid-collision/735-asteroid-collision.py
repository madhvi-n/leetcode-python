class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        
        for num in asteroids:
            #collision occurs when stack top is positive and num is negative
            while stack and num < 0 and stack[-1] > 0:
                diff = num + stack[-1]
                
                # if diff is negative, stack top gets destroyed
                if diff < 0:
                    stack.pop()
                # if diff is positive, num asteriod gets destroyed
                elif diff > 0:
                    num = 0
                # if both are equal and diff is zero, both gets destroyed
                else:
                    num = 0
                    stack.pop()
                    
            if num:
                stack.append(num)
        return stack