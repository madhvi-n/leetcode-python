class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        result = []
        
        for i in range(0, len(s), k):
            curr = s[i:i+k]
            
            if len(curr) < k:
                sub = fill * (k - len(curr))
                curr += sub
            
            result.append(curr)
        return result