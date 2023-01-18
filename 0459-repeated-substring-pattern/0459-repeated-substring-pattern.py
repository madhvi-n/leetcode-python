class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        substring = ''
        n = len(s)
        
        for i in range(n // 2):
            substring += s[i]
            if n % len(substring) == 0:
                if substring * (n // len(substring)) == s:
                    return True
        return False