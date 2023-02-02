class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        s1, s2 = len(str1), len(str2)
        
        def valid(k):
            if s1 % k or s2 % k:
                return False
            
            n1, n2 = s1 // k, s2 // k
            
            base = str1[:k]
            
            return str1 == n1 * base and str2 == n2 * base
        
        for i in range(min(s1, s2), 0, -1):
            if valid(i):
                return str1[:i]
            
        return ""