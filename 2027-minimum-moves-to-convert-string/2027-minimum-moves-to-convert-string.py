class Solution:
    def minimumMoves(self, s: str) -> int:
        minMoves = i = 0
        while i < len(s): 
            if s[i] == "X": 
                minMoves += 1
                i += 3
            else: i += 1
        return minMoves