class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        count = 0
        
        if len(s) < 3:
            return 0
        
        for i in range(len(s)):
            m = set(s[i: i + 3])
            if len(m) == 3:
                count += 1
        
        return count