class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        # Create a charVal hashmap which stores index of each char
        # Initialize left and right pointers as 0 and create a frequency array of length 26
        
        max_len = 0
        n = len(s)
        char_val = {chr(i): i - 97 for i in range(97, 123)}

        for unique_char_count in range(1, len(Counter(s)) + 1):
            left = 0
            right = 0

            char_freq = [0] * 26
            cnt_chars_with_freq_1_or_more = 0
            cnt_chars_with_freq_k_or_more = 0

            while 0 <= right < n:
                if cnt_chars_with_freq_1_or_more <= unique_char_count:
                    char = char_val[s[right]]
                    char_freq[char] += 1
                    if char_freq[char] == 1:
                        cnt_chars_with_freq_1_or_more += 1
                    if char_freq[char] == k:
                        cnt_chars_with_freq_k_or_more += 1
                    right += 1
                else:
                    char = char_val[s[left]]
                    left += 1
                    if char_freq[char] == k:
                        cnt_chars_with_freq_k_or_more -= 1
                    char_freq[char] -= 1
                    if char_freq[char] == 0:
                        cnt_chars_with_freq_1_or_more -= 1

                if cnt_chars_with_freq_1_or_more == unique_char_count and cnt_chars_with_freq_k_or_more == unique_char_count:
                    max_len = max(max_len, right - left)
        return max_len


