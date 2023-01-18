class Solution:
    def checkString(self, s: str) -> bool:
        
        if len(s) == 1:
            return True
        
        lastSeen = s[0]
        
        for i in range(len(s)):
            if lastSeen == s[i]:
                continue
            
            if lastSeen == 'b' and s[i] == 'a':
                return False
            
            lastSeen = s[i]
        return True
                
            