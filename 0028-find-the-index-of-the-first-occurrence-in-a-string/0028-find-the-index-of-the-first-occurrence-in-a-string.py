class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
#         index = -1
        
#         if needle in haystack:
#             index = haystack.find(needle)
#         return index

        k = len(needle)
        for i in range(len(haystack)):
            if haystack[i:i+k] == needle:
                return i
        return -1