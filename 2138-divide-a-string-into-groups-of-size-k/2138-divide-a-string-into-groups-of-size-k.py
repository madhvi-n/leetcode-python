class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        # Initialize an empty list to hold the parts
        parts = []
        
        for i in range(0, len(s), k):
            parts.append(s[i:i+k])
        
        for index, part in enumerate(tuple(parts)):
            if len(part) < k:
                parts[index] = part + (k - len(part)) * fill
        return parts