class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        maxLength = -inf
        
        for sentence in sentences:
            maxLength = max(maxLength, len(sentence.split()))
            
        return maxLength