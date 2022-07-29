class Solution:
    def longestPalindrome(self, s: str) -> int:
        hashmap = {}
        
        for char in s:
            hashmap[char] = 1 + hashmap.get(char, 0)
        
        ans = 0
        for value in hashmap.values():
            ans += value // 2 * 2
            if ans % 2 == 0 and value % 2 == 1:
                ans += 1
        return ans