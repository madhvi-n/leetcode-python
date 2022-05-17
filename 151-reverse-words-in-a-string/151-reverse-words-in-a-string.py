class Solution:
    def reverseWords(self, s: str) -> str:
        stack = s.lstrip().rstrip().split()
        
        res = ""
        
        for word in stack[::-1]:
            res = res + word + " "
        
        return res.rstrip()