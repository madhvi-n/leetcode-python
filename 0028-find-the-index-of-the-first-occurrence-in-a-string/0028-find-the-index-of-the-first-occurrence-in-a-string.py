class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        index = -1
        
        if needle in haystack:
            index = haystack.find(needle)
        return index