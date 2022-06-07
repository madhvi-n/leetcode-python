from collections import Counter

class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        license_count = collections.Counter([char.lower() for char in licensePlate if char.isalpha()])
        
        result = None
        for word in words:
            if not result or len(word) < len(result):
                word_count = collections.Counter(word)
                if all([word_count[key] >= license_count[key] for key in license_count]):
                    result = word
        return result
        
                
        
        