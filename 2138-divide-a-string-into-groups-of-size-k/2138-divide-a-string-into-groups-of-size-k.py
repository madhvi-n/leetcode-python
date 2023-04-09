class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        # Initialize an empty list to hold the parts
        # Start iterating through string from 0 through len(s) with step k
        # If length of substring is less than k, add fill
        
        parts = []
        
        for i in range(0, len(s), k):
            curr = s[i:i+k]
            if len(curr) < k:
                curr = curr + (k - len(curr)) * fill
            parts.append(curr)
        return parts