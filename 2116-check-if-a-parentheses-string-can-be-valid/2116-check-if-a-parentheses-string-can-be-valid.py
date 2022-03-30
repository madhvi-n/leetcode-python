class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        if len(s) % 2 == 1: 
            return False
        
        total = open_count = closed_count = 0
        for i in range(len(s) - 1, -1, -1):
            if locked[i] == '0': 
                total += 1
            elif s[i] == '(': 
                open_count += 1
            elif s[i] == ')': 
                closed_count += 1
            if total - open_count + closed_count < 0: 
                return False
            
        total = open_count = closed_count = 0
        for i in range(len(s)):
            if locked[i] == '0': 
                total += 1
            elif s[i] == '(': 
                open_count += 1
            elif s[i] == ')': 
                closed_count += 1
            if total + open_count - closed_count < 0: 
                return False
        return True