class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        ans = 0
        columnTitle = reversed(columnTitle)
        for index, letter in enumerate(columnTitle):
            digit = ord(letter) - 64
            ans += digit * 26 ** index
        
        return ans
        
        