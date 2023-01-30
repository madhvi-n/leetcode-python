class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""
        
        char_count = {}
        for char in t:
            char_count[char] = char_count.get(char, 0) + 1
        
        left, right = 0, 0
        min_len = float("inf")
        min_start = 0
        count = len(char_count)
        
        while right < len(s):
            if s[right] in char_count:
                char_count[s[right]] -= 1
                if char_count[s[right]] == 0:
                    count -= 1
            while count == 0:
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    min_start = left
                if s[left] in char_count:
                    char_count[s[left]] += 1
                    if char_count[s[left]] > 0:
                        count += 1
                left += 1
            right += 1
        return "" if min_len == float("inf") else s[min_start: min_start + min_len]