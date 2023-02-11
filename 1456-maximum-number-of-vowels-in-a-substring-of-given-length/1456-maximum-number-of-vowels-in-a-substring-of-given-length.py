class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set(['a', 'e', 'i', 'o', 'u'])
        
        max_vowels = 0
        curr_vowels = 0
        
        # traverse through string
        # for each index, if current char is vowel, increment count
        # if index exceed window, check if last character in prev window is vowel
        # if yes, reduce count of curr_vowel
        # for each iteration, keep track of max vowels
        
        for i in range(len(s)):
            if i >= k and s[i - k] in vowels:
                curr_vowels -= 1
            if s[i] in vowels:
                curr_vowels += 1
            max_vowels = max(max_vowels, curr_vowels)
        return max_vowels