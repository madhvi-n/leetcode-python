class Solution:
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:
        vowels = ('a', 'e', 'i', 'o', 'u')
        count = 0
        
        for i in range(left, right + 1):
            curr = words[i]
            
            if curr[0] in vowels and curr[-1] in vowels:
                count += 1
        return count