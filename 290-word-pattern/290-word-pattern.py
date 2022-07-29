class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words, wordsToPattern = s.split(' '), {}

        if len(pattern) != len(words): 
            return False
        
        if len(set(pattern)) != len(set(words)): 
            return False 

        for i, word in enumerate(words):
            if word not in wordsToPattern: 
                wordsToPattern[word] = pattern[i]
            
            elif wordsToPattern[word] != pattern[i]: 
                return False

        return True