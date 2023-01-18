class Solution:
    def maximumValue(self, strs: List[str]) -> int:
#         maxVal = -inf
        
#         for word in strs:
#             if word.isdigit():
#                 maxVal = max(maxVal, int(word))
#             else:
#                 maxVal = max(maxVal, len(word))
                
#         return maxVal
        
        return max(int(c) if c.isdigit() else len(c) for c in strs)