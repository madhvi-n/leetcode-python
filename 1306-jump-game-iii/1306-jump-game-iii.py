class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        # This is a graph question, we can take a stack and keep exploring the 
        # right and left child of the parent, we need to verify that both these
        # childs are valid and then only we can put them back into the stack for
        # further processing, also keep checking that if at any point of time
        # you have reached value 0, then True else False
        
        # Starting from start in stack and marking start as seen
        stack = [start]
        seen = set([start])
        
        while stack:
            initPos = stack.pop()

            # Check if you have already reached there
            if arr[initPos] == 0:
                return True
            
            # Check it's left and right child
            left = initPos - arr[initPos]
            right = initPos + arr[initPos]
            
            # Check if left is valid and not in our hashet to avoid cycles
            if 0 <= left < len(arr) and left not in seen:
                seen.add(left)
                stack.append(left)
                
            # Check if right is valid and not in our hashet to avoid cycles
            if 0 <= right < len(arr) and right not in seen:
                seen.add(right)
                stack.append(right)
                
        return False