class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        charCounter = Counter(chars)
        count = 0
        
        for word in words:
            wordCounter = Counter(word)
            
            for char in wordCounter:
                if wordCounter[char] > charCounter[char]:
                    break
            else:
                count += len(word)
        
        return count
            