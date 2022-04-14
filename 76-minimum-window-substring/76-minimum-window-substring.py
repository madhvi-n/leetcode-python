class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # 1. Use two pointers: start and end to represent a window.
        # 2. Move end to find a valid window.
        # 3. When a valid window is found, move start to find a smaller window.
        
        if t == "":
            return ""
        
        countT, window = {}, {}
        
        # count chars in t string
        for char in t:
            countT[char] = 1 + countT.get(char, 0)
            
        # keep track of chars in window
        have, need = 0, len(countT)
        res, length = [-1, -1], float("inf")
        
        left = 0
        
        for right in range(len(s)):
            c = s[right]
            window[c] = 1 + window.get(c, 0)
            
            if c in countT and window[c] == countT[c]:
                have += 1
            
            while have == need:
                # update our result
                curr_window = right - left + 1
                if curr_window < length:
                    res = [left, right]
                    length = curr_window
                # pop from left of our window
                window[s[left]] -= 1
                if s[left] in countT and window[s[left]] < countT[s[left]]:
                    have -= 1
                left += 1
        left, right = res
        return s[left: right+1] if length != float("inf") else ""