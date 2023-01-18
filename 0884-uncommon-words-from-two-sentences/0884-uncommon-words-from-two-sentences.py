class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        frequency = dict()
        
        for word in s1.split():
            frequency[word] = 1 + frequency.get(word, 0)
        
        for word in s2.split():
            frequency[word] = 1 + frequency.get(word, 0)
        
        return [key for key,val in frequency.items() if val == 1]