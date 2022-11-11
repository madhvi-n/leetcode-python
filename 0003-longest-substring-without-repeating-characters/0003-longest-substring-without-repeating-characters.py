class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        res = 0
        left = 0
        
        for right in range(len(s)):
            # If char at right is in char_set, slide the window. 
            # Remove left char from char_set and increment left
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
            char_set.add(s[right])
            res = max(res, right - left + 1)
        return res