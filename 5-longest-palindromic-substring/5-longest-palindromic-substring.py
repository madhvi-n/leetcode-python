class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        for index in range(len(s)):        
            odd  = self.palindrome_at(s, index, index)
            even = self.palindrome_at(s, index, index + 1)

            res = max(res, odd, even, key=len)
        return res
 
    # starting at l,r expand outwards to find the biggest palindrome
    def palindrome_at(self, s, left, right):    
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left+1:right]

        