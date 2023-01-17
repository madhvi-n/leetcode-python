class Solution:
    def minimumMoves(self, s: str) -> int:
        # initialize minMoves as 0
        # scan string from left to right
        # If char at current index is X, increment minMoves by 1 and increment index by 3 
        # since window is 3 any X in this window will by flipped to 'O' in 1 count
        # else increment index by 1
        
        minMoves = i = 0
        while i < len(s): 
            if s[i] == "X": 
                minMoves += 1
                i += 3
            else: i += 1
        return minMoves