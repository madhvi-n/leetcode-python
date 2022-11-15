class Solution:
    def reverseWords(self, s: str) -> str:
        string = s.lstrip().rstrip().split()
        
        left, right = 0, len(string) - 1
        
        while left < right:
            string[left], string[right] = string[right], string[left]
            left, right = left + 1, right - 1
            
        res = " ".join(string)
        return res.rstrip()