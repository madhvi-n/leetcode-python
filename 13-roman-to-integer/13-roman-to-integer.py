class Solution:
    def romanToInt(self, s: str) -> int:
        # largest to smallest: add them up
        # smallest to largest: subtract them
        
        roman = {'M': 1000,'D': 500 ,'C': 100,'L': 50,'X': 10,'V': 5,'I': 1}
        
        result = 0
        
        for i in range(len(s)):
            if i + 1 < len(s) and roman[s[i]]< roman[s[i+1]]:
                result -= roman[s[i]]
            else:
                result += roman[s[i]]
        return result